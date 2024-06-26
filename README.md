# Simple Whois Domain Batch Checker
A simple python script to check domains from a file
- The input file should be a text file, and every domain should be seperated by `\n` (Enter button)
- The program will first prompt you to enter the path to the input file, that to the output, this also includes the names of the files themselves

This script sometimes returns domains as avalable, when in fact they are not, will try to fix that or if you know the issue, please open pull request.

If you are wondering why the script takes so long to scan a single domain, it is to avoid getting blocked from whois server, as every whois server times you out because they are exploited

### I plan on making this more usable in the future