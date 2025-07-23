print("Convertisseur de Température")

print("1 - Convertir Celsuis vers Farenheit")
print("2 - Convertir Farenheit vers Celsuis")

choix = input("Option (1 ou 2) :")
if choix == '1':
    celsuis = float(input("Entrer la temperature en Celsuis : "))
    print("Conversion en fareinheit :")
    farenheit = (celsuis * 9/5) + 32
    print("La valeur en Celsuis est de", celsuis,"°C vaut en Farenheit", farenheit,"°C.")
elif choix == '2':
    farenheit = float(input("Entrer la temperature en Celsuis : "))
    print("Conversion en fareinheit :")
    celsuis = (farenheit - 32) * 5/9
    print("La valeur en Farenheit est de", farenheit,"°C vaut en Celsuis", celsuis,"°C.") 
else:
    print("Choix invalide, veuillez entrer 1 ou 2.")
