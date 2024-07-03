import whois, logging, datetime, time

logging.basicConfig(level=logging.INFO)

def checkDomain(domain, retries=3, delay=60):
    for attempt in range(retries):
        try:
            domainInfo = whois.whois(domain)
            if domainInfo.creation_date == None and domainInfo.domain_name == None:
                return True, None, None, None, None
            else:
                return False, domainInfo.registrant_name, domainInfo.creation_date, domainInfo.updated_date, domainInfo.expiration_date
        except Exception as e:
            logging.warning(f"Attempt {attempt + 1} failed for {domain}: {e}")
            time.sleep(delay)

def main():
    txtInput = input("Input the domains txt filename path: ")
    with open(txtInput, "r") as file:
        domains = file.readlines()

    txtOutput = input ("Enter output txt filename path: ")
    if not txtInput:
        txtInput = "output"

    date = datetime.date.today().strftime('%Y-%m-%d')

    with open(date + "-" + txtOutput + ".txt", "w") as outputFile:
        for domain in domains:
            domain = domain.strip()
            avalable, registrant_name, creation_date, updated_date, expiration_date = checkDomain(domain)
            if avalable is None:
                output = f"Error checking {domain}: Max retries exceeded\n"
            else:
                output = (
                    f"Domain: {domain}\n"
                    f"Avalable: {avalable}\n"
                    f"Registrant: {registrant_name}\n"
                    f"Creation Date: {creation_date}\n"
                    f"Updated Date: {updated_date}\n"
                    f"Expiration Date: {expiration_date}\n"
                )
            logging.info(output.strip())
            outputFile.write(output + "\n")
            time.sleep(60)

if __name__ == __name__:
    main()