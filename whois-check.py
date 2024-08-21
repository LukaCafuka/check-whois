import argparse
from functions import *

def main():

    parser = argparse.ArgumentParser(
        prog='CheckWhois',
        description='Batch check whois information of domains',
    )
    parser.add_argument('input', help='input file containing domains')
    parser.add_argument('-o', '--output', help='output file name', default='output.txt', required=False)
    parser.add_argument('-t', '--time', type=int, default=120, help='grace period in seconds')
    parser.add_argument('-r', '--retries', type=int, default=3, help='number of retries')

    args = parser.parse_args()

    parseFile(inputFile=args.input, outputFile=args.output, retries=args.retries, delay=args.time)

if __name__ == '__main__':
    main()