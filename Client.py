import marchandise

#definition d'un classe

class Client:

    def __init__(self, nom, age, numTel, adresse):
          self.nom=nom
          self.age=age
          self.numTel=numTel
          self.adresse=adresse
    
    #getter et setter
    #nom
    def get_nom (self): 
        return self.nom 
    
    def set_nom (self, value): 
        self.nom = value
    #numTel
    def get_numTel (self): 
        return self.numTel
    
    def set_numTel (self, value): 
        self.numTel = value
     #adresse
    def get_adresse (self): 
        return self.adresse
    
    def set_adresse (self, value): 
        self.adresse = value
    #age
    def get_age (self): 
        return self.adresse
    
    def set_age (self, value): 
        self.adresse = value

    #commander une marchardise

    

