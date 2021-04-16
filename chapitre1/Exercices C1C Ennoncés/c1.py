heure= int (input ("Entrez les heures SVP "))

minute= int(input ("Entrez les minutes SVP"))

if (heure < 0):
    print("Vous ne pouvez pas indiquer une heure négative!!")
if (heure >23):
    print("Vous ne pouvez pas indiquer une heure supérieure à 23!!")
if (minute < 0):
    print("Vous ne pouvez pas indiquer une minute négative!!")
if (minute > 59):
    print("Vous ne pouvez pas indiquer une minute supérieure à 59!!")
if (heure >= 6 and heure <= 22):
    print("C'est la journée")
if ((heure <= 5 and heure >=0) or heure == 23):
    print("C'est la nuit, faites de beaux rêves")


print("voici les heures encodée " + str(heure) + "h" + str(minute))