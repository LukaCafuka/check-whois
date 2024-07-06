# Simple Whois Domain Batch Checker
### <br> To run the script execute `python whois-check.py [ARGUMENTS]`
A simple python script to check domains from a file 
<br> The input file should be a text file, and every domain should be seperated by `\n` (Enter button)
<br>The program has a set of arguments, some are mandatory and others are optional
 - The script requires an input path
 - The `-h` flag displays useful info on how to use the script
 - Optional flags are: `-t` `-o` `-r`

This script sometimes returns domains as avalable, when in fact they are not, will try to fix that or if you know the issue, please open pull request.

If you are wondering why the script takes so long to scan a single domain, it is to avoid getting blocked from whois server, as every whois server times you out because they are exploited

### I plan on making this more usable in the future