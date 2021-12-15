#Oskar Svedlund
#TEINF-20
#2021-12-14
#Substitute santa

# measurements = []
# with open("wishlist.txt", "r", encoding="utf8") as wishlist:
#     for line in wishlist: 
#         measurements.append(int(line))



name = input("Vad är ditt namn?: ")

wishlist = input("Vad vill du att din önskelista ska heta?: ")


# mesurements=[]
with open(wishlist, "w", encoding="utf8") as wl:
    
    wl.write(f"{name}\nÖNSKELISTA\n")

    print("skriv # om du vill sluta lägga till saker i listan.")

    while True:
        wish = input("Vad vill du lägga till i önskelistan?: ")
                
        if '#' in wish:
            break

        else: wl.write(f"{wish}\n")

while True:
    menu = input("Skriv 2 om du vill lägga på listan, eller 3 om du vill läsa upp den: ")
    if menu == "barlistor":
        lists = input("Vill du kolla på naughtylist eller koolbarn?")

        if lists == "naughtylist":
            with open("naughtylist", "a", encoding="utf8") as naughtylist:
                for line in naughtylist.readlines():
                    print(line, end="")


    
    
    elif menu == "2":
        with open(wishlist, "a", encoding="utf8") as wl:
            
            print("skriv # om du vill sluta lägga till saker i listan.")

            while True:
                wish = input("Vad vill du lägga till i önskelistan?: ")
                
                if '#' in wish:
                    break

                else: wl.write(f"{wish}\n")
            
    elif menu =="3":
        with open(wishlist, "r", encoding="utf8") as wl:
            
    #         for i in range(0, len(mesurements)):
    #             print(f"Hej, {mesurements[i]}")



            for wish in wl.readlines():
                print(wish, end="")

