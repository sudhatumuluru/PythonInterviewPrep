import re
regex=re.compile(r'\d{3}-\d{3}-\d{4}')
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group()) # prints only first occurence of the pattern
print(regex.findall('call me at 408-540-7056, or fax me at 854-565-6345'))