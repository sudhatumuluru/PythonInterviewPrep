import re
regex=re.compile(r'\d{3}-\d{3}-\d{4}')
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group()) # prints only first occurence of the pattern
print(regex.findall('call me at 408-540-7056, or fax me at 854-565-6345')) # prints all occurences of the pattern

# to get only first 3 letters match object - use group(1), group(2), group(3)
# group(0) - returns total match object (total number)

regex=re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # grouping elements with brackets ( ) - 3 groups
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group(0))
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group(1))
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group(1,2))
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group(2))
print(regex.search('call me at 408-540-7056, or fax me at 854-565-6345').group(3))
regex=re.compile(r'(\d{3})-(\d{3}-\d{4})')  # grouping elements with brackets ( ) - 2 groups
areaCode, mainNumber = regex.search('call me at 408-540-7056, or fax me at 854-565-6345').groups()
print "areaCode :" + areaCode
print "mainNumber :" + mainNumber

#(415) 555-4242 - if there is no dash and () is included ----add \ between  ()
phoneNumRegex=re.compile(r'(\(\d{3}\)) (\d{3}-\{4})')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
if mo is not None:
    print("mo.group(1) : " + mo.group(1))
    print("mo.group(2) : " + mo.group(2))

#The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print mo2.group()
mo3 = heroRegex.findall('Tina Fey and Batman.')
if mo3 is not None:
    print mo3

# To match any of the strings 'Batman', 'Batmobile', 'Batcopter', and 'Batbat'
betRegex = re.compile(r'Bat(man|mobile|copter|bat)')
pMatch = betRegex.findall("Batman is a good movie but i liked Batbat character in it but not Batcopter")
print pMatch
pMatch = betRegex.search("Batman is a good movie but i liked Batbat character in it but not Batcopter")
print pMatch.group()

# Optional Matching with the Question Mark:
# Sometimes there is a pattern that you want to match only optionally. The ? character flags the
# group that precedes it as an optional part of the pattern.
# The '?' character flags the group that precedes it as an optional part of the pattern
print '????????????????????????????????????????????????????????'
batRegex=re.compile(r'bat(wo)?man')  # The (wo)? part of the regular expression means that the pattern wo is an optional group.
mo1 = batRegex.search('The Adventures of batman')
print mo1.group()
mo2 = batRegex.search('The Adventures of batwoman')
print mo2.group()

# Matching Zero or More with the Star:
print '**********************************************************'
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
print mo2.group()


