import re

def getEmailInfo(email):
    """
    Extracts the first name, last name, and domain name from an email using regular expressions.
    """
    namePattern = re.compile(r'([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)')
    domainPattern = re.compile(r'@([a-zA-Z]+\.[a-zA-Z]+)')
    
    nameMatch = namePattern.search(email)
    domainMatch = domainPattern.search(email)
    
    if nameMatch and domainMatch:
        firstName, lastName = nameMatch.groups()
        domainName = domainMatch.group(1)
        return firstName, lastName, domainName
    else:
        return None

def removeDigits(string):
    """
    Removes all digits from a string.
    """
    return ''.join(char for char in string if not char.isdigit())

userEmail = input("Enter email: ")
info = getEmailInfo(userEmail)

if info:
    firstName, lastName, domainName = info
    print(f'First Name: {removeDigits(firstName)}')
    print(f'Last Name: {removeDigits(lastName)}')
    print(f'Domain Name: {domainName}')
else:
    print('Invalid email ID')
