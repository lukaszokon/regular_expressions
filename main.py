import re


def check_email(ciag_znakow: str):
    if len(ciag_znakow) > 255:
        return False
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, ciag_znakow)

if __name__ == '__main__':
    adres = 'jan.kowalski@sda.pl'
    print(check_email(adres))
