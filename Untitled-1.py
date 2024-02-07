def ip_to_binary(ip_address):
    ip_parts = ip_address.split('.')
    binary_ip = ""
    for part in ip_parts:
        binary_part = bin(int(part))[2:].zfill(8)
        binary_ip += binary_part + "."
    binary_ip = binary_ip[:-1]
    return binary_ip

def binary_to_ip(binary_ip):
    binary_parts = binary_ip.split('.')
    decimal_ip = []
    for part in binary_parts:
        decimal_part = str(int(part, 2))
        decimal_ip.append(decimal_part)
    ip_address = ".".join(decimal_ip)
    return ip_address

def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'Třída A'
    elif 128 <= first_octet <= 191:
        return 'Třída B'
    elif 192 <= first_octet <= 223:
        return 'Třída C'
    elif 224 <= first_octet <= 239:
        return 'Třída D'
    else:
        return 'Není standardní třída'

cislo1list = []
cislo2list = []
cislo3list = []
cislo4list = []

moznost = False

while not moznost:
    print("1) Převést IP adresu z desítkového na binární formát(např. 255.195.60.0)")
    print("2) Převést IP adresu z binárního na desítkový formát(např. 10101010.11110000.00001111.11001100)")
    volba = input("Zvolte jak chcete počítat (1/2): ")
    if volba == '1' or volba == '2':
        moznost = True
    else:
        print("Zadali jste špatnou možnost!")

if volba == '1':
    print("Napište Adresu postupně(např. 255.195.60.0):")
    moznost = False
    while not moznost:
        cislo1 = input("1: ")
        cislo2 = input("2: ")
        cislo3 = input("3: ")
        cislo4 = input("4: ")
        ip_address = f"{cislo1}.{cislo2}.{cislo3}.{cislo4}"
        ip_parts = ip_address.split('.')
        if len(ip_parts) == 4:
            valid = True
            for part in ip_parts:
                if not (0 <= int(part) <= 255):
                    valid = False
                    break
            if valid:
                moznost = True
                cislo1list.append(cislo1)
                cislo2list.append(cislo2)
                cislo3list.append(cislo3)
                cislo4list.append(cislo4)
            else:
                print("Zadali jste špatnou možnost!")
        else:
            print("Zadali jste špatnou možnost!")

    ip_address = f"{cislo1list[0]}.{cislo2list[0]}.{cislo3list[0]}.{cislo4list[0]}"
    binary_ip = ip_to_binary(ip_address)

    print("Binární reprezentace IP adresy:", binary_ip)
    ip_class = get_ip_class(ip_address)
    print("Třída IP adresy:", ip_class)

elif volba == '2':
    print("Napište binární reprezentaci IP adresy postupně (např. 10101010.11110000.00001111.11001100):")
    moznost = False
    while not moznost:
        binary_parts = []
        for i in range(4):
            part = input(f"{i + 1}: ")
            binary_parts.append(part)
        binary_ip = ".".join(binary_parts)
        if all(part == '0' or part == '1' for part in binary_parts):
            moznost = True
        else:
            print("Zadali jste špatnou možnost!")

    ip_address = binary_to_ip(binary_ip)
    print("Standardní IP adresa:", ip_address)
    ip_class = get_ip_class(ip_address)
    print("Třída IP adresy:", ip_class)
