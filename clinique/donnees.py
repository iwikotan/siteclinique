class info:
    contenue=[
              {'id':1,'noms':'iwikotan','prenoms':'thierry landry','age':'17ans','sexe':'M','statut':'particulier'},
              {'id':2,'noms':'Laourou','prenoms':'viviane','age':'15ans','sexe':'f','statut':'particulier'},
              {'id':3,'noms':'ADAM','prenoms':'smith','age':'1ans','sexe':'M','statut':'particulier'},
        
    ]
    #il faut souvent ajouter @classmethod pour ajouter une methode de class et qui prend cls 
    @classmethod
    def all(cls):
        return cls.contenue

    @classmethod
    def find(cls,id):
         return cls.contenue[int(id)-1]