
import functions
import pickle

print("Que souhaitez-vous faire ?")
print("\t\t(1) Crypter un message")
print("\t\t(2) Décrypter un message")
reponse = int(input())
if reponse == 1:
    s = input("Quel est le message à coder ?\n")
    n = len(s.split())
    key = functions.keygen(s)
    message = functions.strtocode(s,key)
    with open("results", 'wb') as fichier:
        data = { "message" : message,
                      "key" : key,
                      "length" : n
        }
        pickler = pickle.Pickler(fichier)
        pickler.dump(data)
    print("Le message codé à été généré dans results")

elif reponse == 2:
    s = input("Quel est le fichier à décoder ?\n")
    with open("{}".format(s),"rb") as fichier:
        depickler = pickle.Unpickler(fichier)
        data = depickler.load()
    message = data["message"]
    key = data["key"]
    length = data["length"]
    print("Le message décodé est : \n{}".format(functions.codetostr(message, key, length)))

else:
    print("Code erroné, veuillez réessayer")
