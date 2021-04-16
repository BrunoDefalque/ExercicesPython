def ShowResult(_prixHT, _reduc):
    _euros= 1.0 
    _dollars= 1.19
    _mn= 3395 
    _eurostax= 1.21
    _dollartax= 1.075
    _mntax= 1.10


    def Conversion(_prixHT, _devise):
        return _prixHT * _devise
        

    def Tax(_prixConverti, _taxe):
        return _prixConverti * _taxe 

    print (f"Vous avez choisi une somme de {_prixHT } et une réduction de {_reduc}")
    
    _prixConv= Conversion(_prixHT,_euros)
    _prixTTC= Tax(_prixConv,_eurostax)
    _prixReduc= _prixTTC - _reduc

    _prixConv= round(_prixConv, 2)
    _prixTTC= round(_prixTTC, 2)
    _prixReduc= round(_prixReduc, 2)
    print("Prix en Euros:")
    print (f"Prix en euros HT : {_prixConv}")
    print (f"Prix en euros TC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixReduc}")
   
    _prixConv= Conversion(_prixHT,_dollars)
    _prixTTC= Tax(_prixConv, _dollartax)
    _prixReduc=_prixTTC - Conversion(_reduc, _dollars)
    _prixConv= round(_prixConv, 2)
    _prixTTC= round(_prixTTC, 2)
    _prixReduc= round(_prixReduc, 2)
   
    print ("Prix en Dollars :")
    print (f"Prix en dollars HT : {_prixConv}")
    print (f"Prix en dollar TC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixReduc}")

    _prixConv= Conversion(_prixHT,_mn)
    _prixTTC= Tax( _prixConv,_mntax)
    _prixReduc= _prixTTC - (Conversion(_reduc,_mn))
    _prixConv= round(_prixConv, 2)
    _prixTTC= round(_prixTTC, 2)
    _prixReduc= round(_prixReduc, 2)    
    print ("Prix en Tugrik") 
    print (f"Prix en tugrik HT : {_prixConv}")
    print (f"Prix en tugrik TTC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixConv}")
        




    

ShowResult(float(input("Entrez le prix de votre article sans taxes :\n")),float(input("Entrez la réduction appliquée à votre article en euros :\n")))