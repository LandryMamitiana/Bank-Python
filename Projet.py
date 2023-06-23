import os.path as o
import pickle as p
import pyodbc
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
     "SERVER=DEVSECOPS;"
     "DATABASE=bank;"
 )
if conn:
    print("conected réusiite avec succèes");
else:
    print("Eureur")
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

def main_menu():
    print("                                   GESTION BANCAIRE                                      ")
    print("----------------------------------------------------")
    print("                        Bienvenue dans notre Application                        ")
    print("                         1.Admin Authentinfication\n"
          "                         2.Client Authentification")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input("Choisir votre selection: >>")
    choice = int(choice)
    if choice == 1:
        print("                            LOGIN AUTHENTIFICATION                               ")
        cursor=conn.cursor()
        cursor.execute("Select * from login where username=? AND password=?")
        row = cursor.fetchall()
        username = input("Saisir le nom d' utilisateur: ")
        password = input("Saisir votre mots de passe: ")
        if row:
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
