print("Bonjour et bienvenu dans notre parc fait pour vous! \n Pour nous aider à rendre votre séjour le plus agréable à trouver quelles attractions sont faites pour vous, veuillez entrez les informations suivantes: ")
_age= int(input("Age: "))
_sexe= print(input("Sexe (M/F): "))
_nationalite= print(input("Nationalité: "))
_taille= int(input("Taille (en cm): "))
_poids= float(input("Poids (en kg): "))
_signesastro= print(input("Veuillez entrer le chiffre qui correspond à votre signe astrologique:\n 1 - Belier\n2 - Taureau\n3 - Gémeaux\n4 - Cancer\n5 - Lion\n6 - Vierge\n7 - Balance\n8 - Scorpion\n9 - Sagittaire\n10 - Capricorne\n11 - Verseau\n12 - Poisson\n"))
def GrandSplash(_age, _signesastro, _sexe, _taille):
    if _age>="18":
        if _signesastro=="4":
            _signesastro=input
        elif _signesastro=="7":
            _signesastro=input
        elif _signesastro=="12":      
            _signesastro=input 
    elif _sexe=="F":
        if _taille>="160":
            _taille>=input
    elif _age>="45":
        _age>=input

def RiviereSauvage(_nationalite, _sexe, _taille, _signesastro):
    if _nationalité=="Allemand":
        _nationalité=input
    elif _sexe=="F":
        if _taille>="150":
            _taille>=input
    elif _signesastro=="10":
        _singesastro=input

def GrandHuit(_sexe, _age, _taille, _poids, _signesastro):
    if _sexe=="F":
        if _age<="10":
            if  _taille<="130":
                 if  _poids<="45":
                     _poids<=input
    elif _sexe=="M":
        _sexe=input
        if _signesastro=="3":
            _signesastro=input
    
def AutoTemponeuse(_nationalite, _age, _sexe):
    if _nationalite=="Italien":
        _nationalite=input
    elif _nationalité=="Japonais":
        _nationalité=input
    elif _nationalité=="Allemand":
        if _age>="89":
            _age>=input
        if _age<="120":
            _age<=input
    elif _nationalite=="Autrichien":
        _nationalite=input
    elif _age<="17":
        _age<=input
    elif _sexe=="F":
        if _age>="25":
            _age>=input
        if _age<="35":
            _age<=input
    
def Carousel(_taille, _age, _sexe):
    if _taille<="140":
        if _age>="18":
            _age>=input
    elif _sexe=="M":
        _sexe=input
    
def ChaiseVolante(_sexe, _age, _taille):
    if _sexe=="F":
        if _age>="45":
            _age>=input
    elif _taille<="150":
        _taille<=input
    
def Trampoline(_age, _sexe, _taille, _poids, _signesastro):
    if _age>="25":
        if _sexe=="M":
            if _taille>="180":
                if _poids>="80":
                    if _poids<="100":
                        if _signesastro=="5":
                            _signesastro=input
                        elif _signesastro=="9":
                            _signesastro=input
    elif _sexe=="F":
        _sexe=input
    
def Chenille(_nationalite, _age, _taille):
    if _nationalite=="Nigerien":
        if _age>="14":
            _age>=input
    elif _taille>="150":
        _taille>=input
        
				
        