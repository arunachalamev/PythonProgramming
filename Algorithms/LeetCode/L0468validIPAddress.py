def validIPAddress(IP):
    def IPv4(s):
        try: return str(int(s)) == s and 0<= int(s) <= 255 
        except: return False

    def IPv6(s):
        if len(s) > 4: return False
        try: return int(s,16) >=0 and s[0] != '-'
        except: return False

    if IP.count('.') == 3 and all (IPv4(i) for i in IP.split('.')):
        return "IPv4"

    if IP.count(':') == 7 and all (IPv6(i) for i in IP.split(':')):
        return "IPv6"

    return "Neither"

print(validIPAddress("172.1.1.1"))
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(validIPAddress('255.255.255.256'))
