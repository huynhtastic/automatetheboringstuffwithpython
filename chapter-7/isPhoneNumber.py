def isPhoneNumber(text):
  if len(text) != 12: # not a phone number
    return False
  for i in range(0, 3): # check for area code
    if not text[i].isdecimal():
      return False
  if text[3] != '-': # check for hypen
    return False
  for i in range(4, 7): # check for first 3 numbers
    if not text[i].isdecimal():
      return False
  if text[7] != '-': # check for hypen
    return False
  for i in range(8, 12): # check for last 4 numbers
    if not text[i].isdecimal():
      return False
  return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
print('Done')