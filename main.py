import re


def check_ip(adres: str):
    pattern = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
    digits = re.split(r'\.', adres)
    for digit in digits:
        if int(digit) > 255:
            return False
    return re.fullmatch(pattern, adres)


def check_email(ciag_znakow: str):
    if len(ciag_znakow) > 255:
        return False
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, ciag_znakow)


if __name__ == '__main__':
    adres = '192.168.255.255'
    print(check_ip(adres))
