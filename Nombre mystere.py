import random

nombre = random.randint(1, 100)
essai = 1
while True:
    proposition = (int(input("Trouver le numéro mystere:")))
    if nombre != proposition:
        essai += 1
    if proposition == nombre:
        print("Bravo,tu as trouvé en",essai,"Tentatives")
        break
    elif proposition < nombre:
        print("Trop petit")
    else:
        print("Trop Grand")
