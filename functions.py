import datetime
import logging
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


def parseFile(inputFile, outputFile, retries, delay):
    with open(inputFile, "r") as file:
        domains = file.readlines()

    date = datetime.date.today().strftime('%Y-%m-%d')

    if os.path.isfile(outputFile + "-" + date + ".txt"):
        logging.error(f"Output filename {outputFile} already exists")
        return

    try:
        with open(outputFile + "-" + date + ".txt", "w") as outputFile:
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