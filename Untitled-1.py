def ip_to_binary(ip_address):
    # Rozdělení IP adresy na části pomocí teček
    ip_parts = ip_address.split('.')
    
    # Inicializace prázdného řetězce pro binární reprezentaci IP adresy
    binary_ip = ""
    
    # Procházení jednotlivých částí IP adresy
    for part in ip_parts:
        # Převod části IP adresy na binární formát a přidání nul dopředu (pokud je potřeba)
        binary_part = bin(int(part))[2:].zfill(8)
        
        # Přidání binární části do celkové binární IP adresy s oddělovačem "."
        binary_ip += binary_part + "."
    
    # Odstranění poslední tečky ze výsledné binární IP adresy
    binary_ip = binary_ip[:-1]
    
    return binary_ip

cislo1list = []
cislo2list = []
cislo3list = []
cislo4list = []

moznost = False

while moznost == False:
    print("1) 255.255.255.255")
    print("2) 11111111.11111111.00000000.00000000")
    volba = int(input("Zvolte jak chcete počítat: "))
    if volba == 1 or volba == 2:
        moznost = True
    else:
        print("Zadali jste špatnou možnost!")
moznost = False
if volba == 1:
    print("Napište Adresu(např. 255.255.255.255):")

    while moznost == False :   
        cislo1 = int(input("1:"))        
        if cislo1 <0 or cislo1>255:
            print("Zadali jste špatnou možnost!")
            
        else:
            moznost = True
    moznost = False
    while moznost == False :   
        cislo2 = int(input("2:"))        
        if cislo2 <0 or cislo2>255:
            print("Zadali jste špatnou možnost!")  
        else:
            moznost = True    
    moznost = False
    while moznost == False :   
        cislo3 = int(input("3:"))    
        if cislo3 <0 or cislo3>255:
            print("Zadali jste špatnou možnost!")
            
        else:
            moznost = True
    moznost = False
    while moznost == False :   
        cislo4 = int(input("4:"))
        if cislo4 <0 or cislo4>255:
            print("Zadali jste špatnou možnost!")
        else:
            
            moznost = True

    # Převedení vstupní IP adresy na binární formát
    ip_address = f"{cislo1}.{cislo2}.{cislo3}.{cislo4}"
    binary_ip = ip_to_binary(ip_address)
    
    # Výpis binární reprezentace IP adresy
    print("Binární reprezentace IP adresy:", binary_ip)
