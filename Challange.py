print("IP adres")
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

else:
    print("Napište Adresu(např.11111111.11111111.00000000.00000000 ):")

    while moznost == False :   
        cislo1 = str(input("1:"))        
        moznost = True
    for cisloh1 in cislo1:
     cislo1list.append(cislo1)
    print(cislo1list)
    while moznost==False: 
        if cislo1list[0] == "1" or cislo1list[0]=="0" or cislo1list[1] == "1" or cislo1list[1]=="0" or cislo1list[2] == "1" or cislo1list[2]=="0" or cislo1list[3] == "1" or cislo1list[3]=="0" or cislo1list[4] == "1" or cislo1list[4]=="0" or cislo1list[6] == "1" or cislo1list[6]=="0" or cislo1list[7] == "1" or cislo1list[7]=="0" or cislo1list[8] == "1" or cislo1list[8]=="0" or cislo1list[5] == "1" or cislo1list[5]=="0":
            moznost=True
        else:
            print("Zadali jste špatnou možnost!")

    
    
    
    
    
    
    
    
    
   
