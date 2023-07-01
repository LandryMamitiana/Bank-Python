from hashlib import sha256
entree = input("Entrer le nom du fichier à chiffrée: ")
sortie = input("Entrer le nom du fichier final: ")
cle = input("Entrer le clé de securité: ")
cles = sha256(cle.encode('utf-8')).digest()
with open(entree,'rb') as f_entree:
    with open(sortie,'rb') as f_sortie:
        i=0
        while f_entree.peek():
            c=ord(f_entree.read(1))
            j = i % len(cles)
            b = bytes[c^cles[j]]
            f_sortie.write(b)
            i = i+1

