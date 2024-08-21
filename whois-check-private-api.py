import argparse
from functions import readLine, checkDomainAPI, parseFileAPI


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='CheckWhois - WhoisXMLAPI API',
        description='Batch check whois information of domains using WHOISXML API',
    )
    parser.add_argument('input', help='input file containing domains')
    parser.add_argument('-o', '--output', help='output file name for full data', default='full_output.txt', required=False)

    args = parser.parse_args()

    input_file = args.input
    full_output_file = args.output
    summary_output_file = "summary" + args.output
    api_key = readLine("API-KEY.txt", 2)

    parseFileAPI(input_file, full_output_file, summary_output_file, api_key)
