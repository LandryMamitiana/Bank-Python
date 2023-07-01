import os.path as o
import pickle as p
import pyodbc
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
     "SERVER=DEVSECOPS;"
     "DATABASE=bank;"
 )
if conn:
    print("conected");
else:
    print("Eureur")

def obtenir_compte():
    if o.isfile("Account.bat"):
        read_file = open("Account.bat", "rb")
        comptes = p.load(read_file)
        read_file.close()
        return comptes
    else:
        return {}


def write_compte(comptes):
    write_file = open("Account.bat", "wb")
    p.dump(comptes, write_file)
    write_file.close()


def display_compte(Act):
    comptes = obtenir_compte()
    print("Nom:", Act[0])
    print("Prenom:", Act[1])
    print("Cin:", Act[2])
    print("Numero Telephone:", Act[3])
    print("Adresse:", Act[4])
    print("Sexe:", Act[5])
    print("Mots de Passe:", Act[6])
    print("Balance:", Act[7])


def ajout_compte():
    comptes = obtenir_compte()
    print("Ajout compte")
    new_compte = input("Entrer votre numero de compte: ")
    if new_compte in comptes.keys():
        print("Votre numero de compte est déja existé")
        return
    nom = input("Saisir votre nom: ")
    prenom = input("Saisir votre prenom: ")
    cin = input("Saisir votre numero de CIN:  ")
    if len(cin) != 12:
        print("Votre numero cin doit etre 12 chiffres")
        ajout_compte()
    phone = input("Saisir votre numero telephone: ")
    if len(phone) != 10:
        print("Votre numero telephone doit etre 10 chiffres")
        ajout_compte()
    adresse = input("Saisir votre Adresse: ")
    sexe = input("Saisir votre sexe(Homme/Femme): ")
    # mdps = r.randint(1000,9000)
    mdps = input("Saisir votre mots passe(Maj+Caractere speciaux s' il vous plait): ")
    balance = 0
    comptes[new_compte] = [nom, prenom, cin, phone, adresse, sexe, mdps, balance]
    write_compte(comptes)
    print("Comptes a été créer avec avec succèes")


def sup_compte():
    comptes = obtenir_compte()
    print("Supprimé compte")
    new_compte = input("Entrer le numero de compte: ")
    if new_compte in comptes.keys():
        del comptes[new_compte]
        print("Votre compte a été supprimé avec succés")
        write_compte(comptes)
    else:
        print("Votre comptes n' existe pas")


def modif_compte():
    comptes = obtenir_compte()
    print("Modifié compte")
    new_compte = input("Entrer le numero de compte:  ")
    if new_compte in comptes.keys():
        display_compte(comptes[new_compte])
        print("Qu'est ce que vous voulez modifier?")
        print("0.Nom")
        print("1.Prenom")
        print("2.Numero CIN")
        print("3.Numero Telephone")
        print("4.Adresse")
        print("5.Sexe")
        print("6.Mots de Passe")
        choice = int(input("Choisir votre selection >> "))
        if choice >= 0 and choice < 7:
            v = input("Saisir un nouveau valeur: ")
            if v != " ":
                comptes[new_compte][choice] = v
                print("Votre compte a été bien modifier avec succées")
                write_compte(comptes)
            else:
                print("Veuillez-réessayez")
        else:
            print("Choix Invalide")
    else:
        print("Votre comptes n' existe pas")


def list_compte():
    comptes = obtenir_compte()
    print("Listes des comptes")
    for compte in comptes:
        print(compte, comptes[compte])
    pass


def rech_compte():
    comptes = obtenir_compte()
    new_compte = input("Entrer le numero de Compte: ")
    if new_compte in comptes.keys():
        display_compte(comptes[new_compte])
    else:
        print("compte n' existe pas")


def admin_menu():
    print("1.Ajouter compte")
    print("2.Supprimer compte")
    print("3.Modifier compte")
    print("4.Voir tous les compte")
    print("5.Recherche compte")
    print("0.Quiter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        ajout_compte()
    elif choice == 2:
        sup_compte()
    elif choice == 3:
        modif_compte()
    elif choice == 4:
        list_compte()
    elif choice == 5:
        rech_compte()
    elif choice == 0:
        avis = 'o'
        print("Voulez-vous vraiment qutter cette application(o/n)?")
        if avis=='o':
          main_menu()
        else:
          admin_menu()

        exit()

    input("Continue..")
    main_menu()


def depots_argent(new_compte):
    comptes = obtenir_compte()
    montant = int(input("Saisir le montant à déposer: "))
    comptes[new_compte][7] = int(comptes[new_compte][7]) + montant
    write_compte(comptes)
    print(" Montants déposer avec succées")


def retrait_argent(new_compte):
    comptes = obtenir_compte()
    montan = int(input("Saisir le montant à rétirer: "))
    if comptes[new_compte][7] > montan:
        comptes[new_compte][7] = int(comptes[new_compte][7]) - montan
        write_compte(comptes)
        print(" Montants rétirer avec succées")
    else:
        print("On ne peut pas effectué cet rétrait car votre solde actuel est ", comptes[new_compte][7],"ariary")


def mouv_bancaire(new_compte):
    comptes = obtenir_compte()
    print("Cher client,\n"
          "Votre solde actuel est: ", comptes[new_compte][7], "ariary")


def client_menu(new_compte):
    print("1.Depots d' argent")
    print("2.Retraits d' argent")
    print("3.Mouvements Bancaire")
    print("0.Quiter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        depots_argent(new_compte)
    elif choice == 2:
        retrait_argent(new_compte)
    elif choice == 3:
        mouv_bancaire(new_compte)
    elif choice == 0:
       avis = 'o'
       print("Voulez-vous vraiment qutter cette application(o/n)?")
       if avis =='o':
           main_menu()
       else:
            client_menu()
    print("-----------------------------------------------------")
    input("Continue..")
    client_menu(new_compte)


def main_menu():
    print("                  Banque Management                     ")
    print("1.Admin Authentinfication\n2.Client Authentification")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input("Choisir votre selection: >>")
    choice = int(choice)
    if choice == 1:
        nom_user = input("Saisir le nom d' utilisateur: ")
        mdp = input("Saisir votre mots de passe: ")
        if nom_user == "Admin" and mdp == "Admin":
            admin_menu()
        else:
            print("Nom d'utilisateur ou mots de passe incorrect")
    elif choice == 2:
        comptes = obtenir_compte()
        new_compte = input("Entrer votre numero de comptes: ")
        if new_compte in comptes.keys():
            mdp = input("Saisir mots de passe: ")
            if comptes[new_compte][6] == mdp:
                print("Bonjour ", new_compte[0])
                client_menu(new_compte)
            else:
                print("Mots de passe invalide")
        else:
            print("Comptes invalide")


main_menu()
