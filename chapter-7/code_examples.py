import re

# pattern grouping
print('*Pattern grouping with parentheses')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1)) # '415'
print(mo.group(2)) # '555-4242'
print(mo.group(0)) # '415-555-4242'
print(mo.group()) # '415-555-4242'

# all groups at once
print(mo.groups()) # ('415', '555-4242')

# matching in a group with pipe
print('\n*Matching a group with pipe character')
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group()) # 'Batman'
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group()) # 'Tina Fey'

# optional matching with ?
print('\n*Optional match with the Question Mark')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # 'Batwoman'

# matching zero or more with *
print('\n*Matching zero or more with the Star')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # 'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group()) # ' Batwowowowoman'

# matching 1 or more wth +
print('\n*Matching one or more with the Plus')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group()) # 'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group()) # 'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None) # True

# matching specific repetitions with curly brackets
print('\n*Matching specific repetitions with curly brackets')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group()) # 'HaHaHa'
mo2 = haRegex.search('Ha')
print(mo2 == None) # True

# Greedy and Nongreedy Matching
print('\n*Greedy and Nongreedy Matching')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) # 'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group()) # 'HaHaHa'

# the findall() method
print('\n*The findall() Method')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # ['415-555-9999, '212-555-0000']
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # [('415', '555', '1122'), ('212', '555', '0000')]

#pg 158
# Character classes
# \d = (0|1|2|3|4|5|6|7|8|9) or [0-9]
# \D = ^\d
# \w = [a-zA-Z\d_]
# \W = [^a-zA-Z\d_]
# \s = [\t\s\n]
# \S = [^\t\s\n]
print('\n*Character Classes')
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# Making Your Own Character Classes
print('\n*Making Your Own Character Classes')
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.')) # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# The Caret and Dollar Sign Characters
print('\n*The Caret and Dollar Sign Characters')
beginsWithHello = re.compile(r'^Hello') # SRE_Match object
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello') == None) # True
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42')) # SRE_Match object
print(endsWithNumber.search('Your number is forty two.') == None) # True
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890')) # SRE_Match object
print(wholeStringIsNum.search('12345xyz67890') == None) # True
print(wholeStringIsNum.search('12 34567890') == None) # True

# The Wildcard Character
print('\n*The Wild Card Character')
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.')) # ['cat', 'hat', 'sat', 'lat', 'mat']

# Matching everything with dot-star
print('\n*Matching everything with dot-star')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1)) # 'Al'
print(mo.group(2)) # 'Sweigart'

# pg 185pdf/161