import marchandise
import Client
class AppClient: 

    APP_NAME = "Gestion Client" 
    APP_VERSION = 4.2

    def __init__ (self): 
          
          #self.ajouterClient()
        # instances de clients
    
          self.clients=[]
          self.marchandises=[]

          #creer des donnees
          def creerClient():
             self.client1 = Client.Client("client1", "0645626784", "paris")
             self.client2 =  Client.Client("client2", "034567899","paris")
          #ajouter client
          def ajouterClient():
            nom=input("Entrer le nom du client\n")
            numTel=input("Le numero telephone du client\n")
            adresse=input("l'adresse du client\n")
            age=int(input("l'age du client"))
            client=Client.Client(nom, age, numTel, adresse)
            
            self.clients.append(client)
            
          #chercher Client
          def chercherClient(self, client) : 
             if (client in self.clients): 
               return client
             else: 
                return "Student doesn't exist"
          #afficher Client
          def afficherClient():
            #print("listes :"+ str(self.clients))
            for client in self.clients:
              print("Nom du client "+str(client.get_nom())+"\n Numero de telephone "+str(client.get_numTel())+
                     "\nadresse "+ str(client.get_adresse()))
              print("liste"+ str(client))

        
          #supprimer un client
          def supprimerClient(position):
             position=int(input("le client à supprimer se trouve a quel position\n"))
             self.clients.remove(position)
             return self.clients
          
        
          def nombreClient():
             nombre=len(self.clients)
             return nombre
         #lancer l'application
  
          ajouterClient()
          afficherClient()
          exit() 


if __name__=="__main__":
    client_app=AppClient()
     
  