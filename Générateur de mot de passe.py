import random, string
print("Générateur de mot de passe")
longueur = int(input("Entrer la longueur du mot de passe :"))
print("ok")
_lower = input("Miniscules ? (oui/non) :") == "oui"
_upper = input("Majuscules ? (oui/non) :") == "oui"
_digits = input("Chiffres ? (oui/non) :") == "oui"
_symbols = input("Spéciaux ? (oui/non) :") == "oui"
caracteres = ""
if _lower:
    caracteres += string.ascii_lowercase
if _upper:
    caracteres += string.ascii_uppercase
if _digits:
    caracteres += string.digits
if _symbols:
    caracteres += string.punctuation 
if  caracteres == "":
    print("Aucun type de caractère sélectionné, arrêt du programme")
    exit()
mot_de_passe = ""
for i in range(1,longueur):
    mot_de_passe += random.choice(caracteres)
print("Mot de passe de ", longueur,"caractere :",mot_de_passe)
