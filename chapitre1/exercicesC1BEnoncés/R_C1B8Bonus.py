# Les trois fonction suivante, CalculateTax, EuroChange et ApplyReduction sont LES fonctions qui devaient être présente chez tout le monde au minimum, ce sont les plus classiques
# Et obligatoire dans ce type de projet, bien sur les noms pourraient différer chez-vous
def CalculateTax(_price,_rate): # USA : 7,5 / EU : 21 / MN : 10
    _fullPrice = _price + (_price*(_rate/100))
    return _fullPrice

# Dans notre programme, appeler cette fonction EuroChange() fait sens, car on par toujours de l'euro vers une autre monnaie, j'ai donc mis ces noms là pour ne pas vous
# perdre, MAIS, on voit très bien que si on commencait du dollar vers l'euro, il n'y aurait strictement rien à changer dans notre algorithme, on pourrait donc appeler cette fonction
# Change() tout simplement, car elle s'occupe simplement à l'aide d'un taux de change de transformer une monnaie en une autre
def EuroChange(_euro,_changeRate): # *1,19 * 3395
    _convertedEuro = _euro * _changeRate
    return _convertedEuro

def ApplyReduction(_price,_reduction):
    _finalPrice = _price-_reduction
    return _finalPrice

def Display(_price,_priceWithTax,_finalPrice,_moneyName):
    # Ce qui se passe dans cette fonction pourrait se passer dans "CalculateAll()" en terme de répétition, mais pas en terme de fonction. Ces deux fonctions ont deux rôles différents
    # Ce n'est pas une erreur dans CE CAS bien précis de ne pas splitter ces deux fonctions comme fait ici, mais dans un projet plus grand, ça serait une erreur, car on pourrait
    # Avoir à un moment envie d'utiliser la fonction display sans appeler au par avant la fonction CalculateAll
    print("\nPrix en " + _moneyName + " :")
    print("\t-Sans TVA : " + str(_price))
    print("\t-Avec TVA : " + str(_priceWithTax))
    print("\t-Après réduction : " + str(_finalPrice))
    
def CalculateAll(_priceInEuro,_reductionInEuro,_changeRate,_TVAValue,_moneyName):
    # Cela crée cela dit un autre problème, si on veut appeler la fonction CalculateAll() SANS la fonction Display(), on ne peut pas, malheureusement avec le peu de matière que l'on
    # A vu pour le moment, c'est impossible. mais plus tard on pourrait utiliser l'orienté objet (meilleur solution) ou une condition avec des booléens pour régler ce soucis
    _price = EuroChange(_priceInEuro,_changeRate)
    _priceWithTax = CalculateTax(_price,_TVAValue)
    _reduction = EuroChange(_reductionInEuro,_changeRate)
    _finalPrice = ApplyReduction(_priceWithTax,_reduction)
    Display(_price,_priceWithTax,_finalPrice,_moneyName)

def ShowResult(_euroPrice,_reduction):
    print("Vous avez acheté un article a " + str(_euroPrice) + "euros sans taxes. Il y a une réduction de " + str(_reduction) + "euros brut dessus")
    CalculateAll(_euroPrice,_reduction,1,21,"euros")
    CalculateAll(_euroPrice,_reduction,1.19,7.5,"dollars")
    CalculateAll(_euroPrice,_reduction,3395,10,"Tugrik")
    
    # Voilà la seule chose que j'ai à faire si je dois rajouter une monnaire, dupliquer la ligne d'appel à calculateAll, et hop ! Regardez :
    CalculateAll(_euroPrice,_reduction,87.64,17,"Metical")
    CalculateAll(_euroPrice,_reduction,1.48,15,"Dollar Canadien")
    CalculateAll(_euroPrice,_reduction,129.56,14,"Shilling")
    
ShowResult(float(input("Entrez le prix de votre article sans taxes :\n")),float(input("Entrez la réduction appliquée à votre article en euros :\n")))
