import sys  # Importation d'une bibliothèque Aller voir ligne 14


def ChoiceDestination():
    print("1 - Bruxelles\n2- Mons\n3- Nivelles\n4- Charleroi")
    _destinationChoice = int(input("Entrez la destination d'arrivée :"))
    if (_destinationChoice == 1):
        _destination = "Bruxelles"
    elif (_destinationChoice == 2):
        _destination = "Mons"
    elif (_destinationChoice == 3):
        _destination = "Nivelles"
    elif (_destinationChoice == 4):
        _destination = "Charleroi"
    else:
        # Cette bibliothèque permet de mettre fin complètement au programme
        sys.exit("ERREUR, LA DESTINATION N'EST PAS CORRECT !!!")
    print("Avez décidé d'aller à " + _destination + "\n")
    return _destination


def ChoicePeriodOfTime():
    print("1 - Matin\n2 - Après-midi\n3 - Soir")
    _timeChoice = int(input("À quel moment désirez-vous partir"))
    if (_timeChoice == 1):
        _time = "Matin"
    elif _timeChoice == 2:
        _time = "Après-midi"
    elif _timeChoice == 3:
        _time = "Soir"
    else:
        sys.exit("ERREUR, L'HEURE D'EENTREE N'EST PAS CORRECT !!!")
    print("Avez décidé de partir" + _time + "\n")
    return _time
def DisplayTime(_time, _matin, _apm, _soir):
    if (_time == "Matin"):
        print("Votre train demarre à " + _matin)
    elif (_time == "Après-midi"):
        print("Votre train démarre à " + _apm)
    elif (_time == "Soir"):
        print("Votre train démarre à " + _soir)
destination= ChoiceDestination()
time= ChoicePeriodOfTime()
if (destination == "Bruxelles"):
    DisplayTime(time, "10h33", "14h42", "19h02")
elif (destination == "Mons"):
    DisplayTime(time, "10h59", "17h42", "22h02")
elif (destination == "Nivelles"):
    DisplayTime(time, "06h59", "17h12", "22h01")
elif (destination == "Charleroi"):
    DisplayTime(time, "09h59", "16h42", "23h02")