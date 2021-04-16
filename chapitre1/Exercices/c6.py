couleurJeans= input("Veuillez indiquer La couleur préférée de vos pantalons : ")
couleurChemise= input("Veuillez indiquer La couleur préférée de vos chemises : ")

print("Votre Couleur préférée pour votre pantalon est : " + couleurJeans + " Et contient : " + str(len(couleurJeans)) + " Caractères")
print("Votre Couleur préférée pour vos chemises est : " + couleurChemise + " Et contient : " + str(len(couleurChemise)) + " Caractères")
print("Le nombre de caractères des deux couleur est : " + str(len(couleurJeans+couleurChemise)))