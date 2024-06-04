# Simple Whois Domain Batch Checker
A simple python script to check domains from a file
- The file should be called `domains.txt` and should include domains to check sperated by `\n` (Enter button)
- The file has to be in the same directory as the script

This script sometimes returns domains as avalable, when in fact they are not, will try to fix that or if you know the issue, please open pull request.

If you are wondering why the script takes so long to scan a single domain, it is to avoid getting blocked from whois server, as every whois server times you out because they are exploited

### I plan on making this more usable in the future