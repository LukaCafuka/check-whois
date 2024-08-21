import datetime
import logging
import requests
import itertools
import os.path
import time
import whois as pywhois
logging.basicConfig(level=logging.INFO)


def checkDomain(domain, retries, delay):
    for attempt in range(retries):
        try:
            domainInfo = pywhois.whois(domain)
            if domainInfo.creation_date is None and domainInfo.domain_name is None:
                return True, None, None, None, None
            else:
                return (False, domainInfo.registrant_name, domainInfo.creation_date,
                        domainInfo.updated_date, domainInfo.expiration_date)
        except Exception as e:
            logging.warning(f"Attempt {attempt + 1} failed for {domain}: {e}")
            time.sleep(delay)

def generateCombination(extension, repeat):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    combinations = [''.join(c) + extension for c in itertools.product(characters, repeat)]


    output_file = "generateddomains.txt"
    with open(output_file, 'w') as f:
        f.write('\n'.join(combinations))

    print(f"{output_file} has been generated with {len(combinations)} domains.")

def checkDomainAPI(domain, apiKey):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={apiKey}&domainName={domain}&outputFormat=JSON&da=2"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as e:
        return f"Error retrieving WHOIS for {domain}: {e}"


def readLine(filePath, lineNumber):
    try:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            if lineNumber <= len(lines):
                return lines[lineNumber - 1].strip()
            else:
                return f"Error: The file has only {len(lines)} lines."
    except FileNotFoundError:
        return f"Error: The file {filePath} does not exist."

def parseFile(inputFile, outputFile, retries, delay):
    with open(inputFile, "r") as file:
        domains = file.readlines()

    date = datetime.date.today().strftime('%Y-%m-%d')

    if os.path.isfile(outputFile + "-" + date + ".txt"):
        logging.error(f"Output filename {outputFile} already exists")
        return

    try:
        with open(outputFile + "-" + date + ".txt", "w", encoding='utf-8') as outputFile:
            for domain in domains:
                domain = domain.strip()
                available, registrant_name, creation_date, updated_date, expiration_date = checkDomain(domain, retries,
                                                                                                       delay)
                if available is None:
                    output = f"Error checking {domain}: Max retries exceeded\n"
                else:
                    output = (
                        f"Domain: {domain}\n"
                        f"Available: {available}\n"
                        f"Registrant: {registrant_name}\n"
                        f"Creation Date: {creation_date}\n"
                        f"Updated Date: {updated_date}\n"
                        f"Expiration Date: {expiration_date}\n"
                    )
                logging.info(output.strip())
                outputFile.write(output + "\n")
                time.sleep(delay)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def parseFileAPI(inputFile, fullOutputFile, summaryOutputFile, apiKey):
    with open(inputFile, 'r') as f:
        domains = [line.strip() for line in f.readlines()]

    with open(fullOutputFile, 'w') as fullOutFile, open(summaryOutputFile, 'w') as summary_out_file:
        for domain in domains:
            print(f"Checking WHOIS for domain: {domain}")
            whois_info = checkDomainAPI(domain, apiKey)

            fullOutFile.write(f"Domain: {domain}\n")
            fullOutFile.write(whois_info)
            fullOutFile.write("\n" + "=" * 60 + "\n")

            for line in whois_info.splitlines():
                if 'domainName' in line or 'domainAvailability' in line:
                    summary_out_file.write(line + "\n")

            print(f"{whois_info}")

    print(f"Full WHOIS information saved to {fullOutputFile}")
    print(f"Domain availability summary saved to {fullOutputFile}")