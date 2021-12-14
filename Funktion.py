#Oskar Svedlund
#TEINF-20
#2021-12-14
#Substitute santa

# measurements = []
# with open("wishlist.txt", "r", encoding="utf8") as wishlist:
#     for line in wishlist: 
#         measurements.append(int(line))



namn = input("Vad är ditt namn?: ")

wishlist = input("Vad vill du att din önskelista ska heta?: ")

wishlist + ".txt"




with open(wishlist, "w", encoding="utf8") as wishlist:
            
    print("skriv # om du vill sluta lägga till saker i listan.")

    while True:
        wish = input("Vad vill du lägga till i önskelistan?: ")
                
        if '#' in wish:
            break

        else: wishlist.write(f"{wish}\n")

while True:
    menu = input("Skriv 2 om du vill lägga på listan, eller 3 om du vill läsa upp den.")

    
    
    if menu == "2":
        with open(wishlist, "a", encoding="utf8") as wishlist:
            
            print("skriv # om du vill sluta lägga till saker i listan.")

            while True:
                wish = input("Vad vill du lägga till i önskelistan?: ")
                
                if '#' in wish:
                    break

                else: wishlist.write(f"{wish}\n")
            
    if menu =="3":
         with open(wishlist, "r", encoding="utf8") as wishlist:
             for wish in wishlist.readlines():
                 print(wish, end="")
