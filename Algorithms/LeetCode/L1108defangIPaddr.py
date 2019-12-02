# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address):
    temp = address.split('.')
    return '[.]'.join(temp)

print (defangIPaddr("1.1.1.1"))