import pyodbc
import os.path as o
import datetime

# connnection à la base de donnée
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DEVSECOPS;"
    "DATABASE=bank;"
    "Trusted_Connection=yes;"
)
server = 'DEVSECOPS'
database = 'bank'
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"

# lister tous les comptes qui existes
def voir_compte(conn):
    print("----------------------BONJOUR----------------------")
    print("                                                         LISTES DES COMPTES BANCAIRES QUI SONT INSCRITS                                                  ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    cursor.execute("select * from compte")
    for row in cursor:
        print(f"Information du compte={row}")
    print()
    print("Tapez 0 pour quitter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 0:
        admin_menu()
    else:
        voir_compte(conn)


# ajoiuter un nouveu compte
def ajout_compte(conn):
    print("----------------------BONJOUR----------------------")
    print("                        AJOUTER UN COMPTE BANCAIRE                            ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    cursor.execute("select * from compte where numero_compte=?", (numero_compte))
    exist = cursor.fetchall()
    if exist:
        print("Numero de compte existe déjà")
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            admin_menu()
        else:
            ajout_compte(conn)
    else:
        cursor = conn.cursor()
        nom = input("Saisir votre Nom : ")
        prenom = input("Saisir votre Prenom : ")
        numero_cin = input("Saisir votre Numero de Cin(12 chiffres en minimun) : ")
        while len(numero_cin) != 12:
            numero_cin = input("Saisir votre Numero de Cin(12 chiffres au minimum) : ")
        numero_phone = input("Saisir votre Numero Telephone(10 chiffres en minimum) : ")
        while len(numero_phone) != 10:
            numero_phone = input("Saisir votre Numero Telephone(10 chiffres en minimum) : ")
        adresse = input("Saisr votre Adresse Exacte : ")
        sexe = input("Saisir votre Sexe(Homme/Femme) :  ")
        mdp = input("Veuillez saisir un mots de passe bien securisé(10 minimum) :  ")
        while len(mdp) < 10:
            mdp = input("Veuillez saisir un mots de passe bien securisé(10 minimum) :  ")
        solde = 0
        montant = 0
        cursor.execute(
            "insert into compte(numero_compte,nom,prenom,numero_cin,numero_phone,adresse,sexe,mdp,solde,montant) values (?,?,?,?,?,?,?,?,?,?);",
            (numero_compte, nom, prenom, numero_cin, numero_phone, adresse, sexe, mdp, solde, montant))
        print("Merci,\n Votre compte a été crée avec succées")
        conn.commit()
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            admin_menu()
        else:
            ajout_compte(conn)
        print("--------------------FIN D' AJOUT ---------------------")
        admin_menu()


# supprimer un compte
def supprime_compte(conn):
    print("----------------------BONJOUR----------------------")
    print("                        SUPPRIMER UN COMPTE BANCAIRE                            ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    cursor.execute("select * from compte where numero_compte=?", (numero_compte))
    exist = cursor.fetchall()
    if exist:
        cursor = conn.cursor()
        numero_compte = input("Saisir le Numero de Compte du Client à supprimer : ")
        cursor.execute("delete from compte where numero_compte = ?", (numero_compte))
        print("Merci,\n Votre compte a été supprimée  avec succées")
        conn.commit()
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            admin_menu()
        else:
            supprime_compte(conn)
        print("----------------FIN DE SUPPRESSION -------------------------")
        admin_menu()
    else:
        print("Compte invalide")


# modifier un compte
def update_compte(conn):
    print("----------------------BONJOUR----------------------")
    print("              METTRE A JOUR UN COMPTE BANCAIRE                            ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    cursor.execute("select * from compte where numero_compte=?", (numero_compte))
    exist = cursor.fetchall()
    if exist:
        cursor = conn.cursor()
        cursor.execute("select * from compte where numero_compte=?", (numero_compte))
        for row in cursor:
            print("Numero de compte :", row[0])
            print("Nom :", row[1])
            print("Prenom :", row[2])
            print("Numero CIN :", row[3])
            print("Numero Telephone :", row[4])
            print("Adresse :", row[5])
            print("Sexe :", row[6])
            print("Mots de passe :", row[7])
            nom = input("Saisir votre Nom : ")
            prenom = input("Saisir votre Prenom : ")
            numero_cin = input("Saisir votre Numero de Cin(12 chiffres en minimun) : ")
            while len(numero_cin) != 12:
                numero_cin = input("Saisir votre Numero de Cin(12 chiffres au minimum) : ")
            numero_phone = input("Saisir votre Numero Telephone(10 chiffres en minimum) : ")
            while len(numero_phone) != 10:
                numero_phone = input("Saisir votre Numero Telephone(10 chiffres en minimum) : ")
            adresse = input("Saisr votre Adresse Exacte : ")
            sexe = input("Saisir votre Sexe(Homme/Femme) :  ")
            mdp = input("Veuillez saisir un mots de passe bien securisé(10 minimum) :  ")
            while len(mdp) < 10:
                mdp = input("Veuillez saisir un mots de passe bien securisé(10 minimum) :  ")
            solde = 0
            montant = 0
            cursor = conn.cursor()
            cursor.execute(
                "update compte set  nom=? ,prenom=?,numero_cin=?,numero_phone=?,adresse=?,sexe=?,mdp=?,solde=?,         montant=? where numero_compte=? ;",
                (nom, prenom, numero_cin, numero_phone, adresse, sexe, mdp, solde, montant, numero_compte))
            print("Merci,\n Votre compte a été modifiée avec succées")
            conn.commit()
            print("Tapez 0 pour quitter")
            choice = input('Choisir votre selection: >>')
            while not choice.isdigit():
                choice = input('Choisir votre selection: >>')
            choice = int(choice)
            if choice == 0:
                admin_menu()
            else:
                update_compte(conn)
            print("----------------FIN DE MODIFICATION -------------------------")
            admin_menu()
    else:
        print("Compte n' existe pas")

# rechercher un compte
def rech_compte(conn):
    print("----------------------BONJOUR----------------------")
    print("                                     RECHERCHE COMPTE                                      ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    cursor.execute("select * from compte where numero_compte=?", (numero_compte))
    exist = cursor.fetchall()
    if exist:
        cursor = conn.cursor()
        cursor.execute("select * from compte where numero_compte=?", (numero_compte))
        for row in cursor:
            print("Numero de compte :", row[0])
            print("Nom :",row[1])
            print("Prenom :", row[2])
            print("Numero CIN :",row[3])
            print("Numero Telephone :",row[4])
            print("Adresse :",row[5])
            print("Sexe :",row[6])
            print("Mots de passe :",row[7])
        print("Veuillez-choisir votre action")
        print(" 1.Continuer")
        print(" 0.Quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 1:
            rech_compte(conn)
        elif choice == 0:
            admin_menu()
        else:
            print("Vous devez choisir  1 ou 0")
            rech_compte(conn)
    else:
        print("Compte n' existe pas")
        admin_menu()


# administrateur menu
def admin_menu():
    print("----------------------BONJOUR----------------------")
    print("                        BIENVENUE SUR ADMIN PANEL                                  ")
    print("----------------------------------------------------")
    print("Bonjour Monsieur/Madame, Veuillez-choissir votre choix :")
    print("                1.Ajouter compte")
    print("                2.Supprimer compte")
    print("                3.Modifier compte")
    print("                4.Voir tous les compte")
    print("                5.Recherche compte")
    print("                6.Recherche pret entre 2 dates")
    print("                7.Recherche expiration entre 2 dates")

    print("                0.Quitter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        ajout_compte(conn)
    elif choice == 2:
        supprime_compte(conn)
    elif choice == 3:
        update_compte(conn)
    elif choice == 4:
        voir_compte(conn)
    elif choice == 5:
        rech_compte(conn)
    elif choice == 6:
        date_pret(conn)
    elif choice == 7:
        date_expiration(conn)
    elif choice == 0:
        main_menu()
    else:
        print("Vous devez chosir un nombre entre 0 à 7 ")
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            admin_menu()
        else:
            admin_menu()




connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"

def date_pret(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comptes WHERE date_pret BETWEEN '01/06/23' AND '30/06/23';")
    for row in cursor:
        print("Numero de compte :", row[0])
        print("Montant preté :", row[1])
        print("Date du pret :", row[2])
        print("Date d' expiration :", row[3])
        print("Durée du pret :", row[4])
        print("Montant :", row[5])
        print("--------------------------------")
    print("Veuillez-choisir votre action")
    print(" 1.Continuer")
    print(" 0.Quitter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        date_pret(conn)
    elif choice == 0:
        admin_menu()
    else:
        print("Vous devez choisir  1 ou 0")
        date_pret(conn)


def date_expiration(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comptes WHERE date_expiration BETWEEN '01/06/23' AND '30/06/23';")
    for row in cursor:
        print("Numero de compte :", row[0])
        print("Montant preté :", row[1])
        print("Date du pret :", row[2])
        print("Date d' expiration :", row[3])
        print("Durée du pret :", row[4])
        print("Montant :", row[5])
        print("--------------------------------")
    print("Veuillez-choisir votre action")
    print(" 1.Continuer")
    print(" 0.Quitter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        date_expiration(conn)
    elif choice == 0:
        admin_menu()
    else:
        print("Vous devez choisir  1 ou 0")
        date_expiration(conn)
# client menu
def client_menu():
    print("----------------------BONJOUR----------------------")
    print("                        BIENVENUE SUR CLIENT PANEL                                  ")
    print("----------------------------------------------------")
    print("Cher(e) Client(e), Veuillez-choissir votre choix :")
    print("                1.Versement d'Argent")
    print("                2.Retrait d'Argent")
    print("                3.Prets d'Argent")
    print("                4.Rembourser mon pret")
    print("                5.Voir mon Solde Principale")
    print("                6.Voir mon Pret")
    print("                7.Conversion Monetaire")
    print("                 0.Quitter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        versement(conn)
    elif choice == 2:
        retraits(conn)
    elif choice == 3:
        prets(conn)
    elif choice == 4:
        rembo(conn)
    elif choice == 5:
        voir_solde(conn)
    elif choice == 6:
        voir_pret(conn)
    elif choice == 7:
        convert()

    elif choice == 0:
        main_menu()


connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"


# verser un  argent
def versement(conn):
    print("----------------------BONJOUR----------------------")
    print("                                       VERSEMENT D' ARGENT                                      ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    mdp = input("Saisir votre mots de passe : ")
    cursor.execute("select * from compte where numero_compte=? AND mdp=?", (numero_compte,mdp))
    exist = cursor.fetchall()
    if exist:
        montant = int(input("Saisir le montant à déposer: "))
        cursor = conn.cursor()
        cursor.execute("update compte set  solde = solde + ? where numero_compte=? ;",
                       (montant, numero_compte))
        print("Versement réussit avec succèes")
        conn.commit()
        print("Veuillez-choisir votre action")
        print(" 1.Continuer")
        print(" 0.Quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 1:
            versement(conn)
        elif choice == 0:
            client_menu()
        else:
            print("Vous devez choisir  1 ou 0")
            versement(conn)
    else:
        print("Echec ou compte spécifié n' existe pas")
        client_menu()


# retirer un argent
def retraits(conn):
    print("----------------------BONJOUR----------------------")
    print("                                       RETRAITS D' ARGENT                                      ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    mdp = input("Saisir votre mots de passe : ")
    cursor.execute("select * from compte where numero_compte=? AND mdp=?", (numero_compte,mdp))
    exist = cursor.fetchall()
    if exist:
        cursor = conn.cursor()
        cursor.execute("select * from compte where numero_compte = ?", (numero_compte))
        montant = int(input("Saisir le montant à retirer: "))
        solde = cursor.fetchone()[9]
        if montant < 10000:
            print("Minimum retrait 10 000 ariary")
            retraits(conn)
        else:
            if solde >= montant:
                cursor = conn.cursor()
                cursor.execute("update compte set  solde = solde - ? where numero_compte=? ;", (montant, numero_compte))
                print("Retrait effectue avec succèes")
                conn.commit()
                print("Veuillez-choisir votre action")
                print(" 1.Continuer")
                print(" 0.Quitter")
                choice = input('Choisir votre selection: >>')
                while not choice.isdigit():
                    choice = input('Choisir votre selection: >>')
                choice = int(choice)
                if choice == 1:
                    retraits(conn)
                elif choice == 0:
                    client_menu()
                else:
                    print("Vous devez choisir  1 ou 0")
                    retraits(conn)
            else:
                print("Action Invalide")
                print("Cher(e) Client(e),\n Votre solde actuels est ", solde, " Ariary")
                print("Veuillez faire un versement d' argent pour effectuer cette action")
                conn.commit()
                print("Tapez 0 pour quitter")
                choice = input('Choisir votre selection: >>')
                while not choice.isdigit():
                    choice = input('Choisir votre selection: >>')
                choice = int(choice)
                if choice == 0:
                    client_menu()
                else:
                    retraits(conn)
    else:
        print("Numero de compte invalide ou compte n' existe pas")
        client_menu()


# preter un argent
def prets(conn):
    print("----------------------BONJOUR----------------------")
    print("                                            PRET D' ARGENT                            ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    mdp = input("Saisir votre mots de passe : ")
    cursor.execute("select * from compte where numero_compte=? AND mdp=?", (numero_compte,mdp))
    exist = cursor.fetchall()
    while exist:
        cursor = conn.cursor()
        cursor.execute("select * from comptes where numero_compte = ?", (numero_compte))
        montant_pret = cursor.fetchone()[1]
        montant_pret = int(montant_pret)
        if montant_pret > 0:
            print("Il reste encore des comptes à regler")
            print("Numero de compte: ", numero_compte)
            print("Argent preter: ", montant_pret, "Ariary")
            print("Tapez 0 pour quitter")
            choice = input('Choisir votre selection: >>')
            while not choice.isdigit():
                choice = input('Choisir votre selection: >>')
            choice = int(choice)
            if choice == 0:
                client_menu()
            else:
                cursor=conn.cursor()
                montant_pret = 0;
                cursor.execute("select * from comptes where numero_compte = ?", (numero_compte))
                cursor.execute("update comptes set  montant_pret = ? where numero_compte=? ;",(montant_pret,numero_compte))
            conn.commit()
        else:
            cursor = conn.cursor()
            montant_pret = input("Saisir le montant de l' argent à preter (100 000 Ariary au maximum) : ")
            while int(montant_pret) > 100000:
                montant_pret = input("Saisir le montant de l' argent à preter (100 000 Ariary au maximum) : ")
            date_pret = input("Saisir la date du pret : ")
            date_expiration = input("Saisir la date d' expiration : ")
            duree_pret = input("Veuillez saisir la duree du pret(2 mois maximum) :  ")
            while len(duree_pret) < 3:
                duree_pret = input("Veuillez saisir la duree du pret(2 mois maximum) :  ")
            cursor.execute(
                "update comptes set  montant_pret=? ,date_pret=?,date_expiration=?,duree_pret=? where numero_compte=? ;",
                (montant_pret, date_pret, date_expiration, duree_pret,numero_compte))
            print("Merci,\n Votre pret a effectuée avec succées")
            conn.commit()
            print("--------------------FIN DE PRET ---------------------")
            print("Continue...")
            print("Tapez 0 pour quitter")
            choice = input('Choisir votre selection: >>')
            while not choice.isdigit():
                choice = input('Choisir votre selection: >>')
            choice = int(choice)
            if choice == 0:
                client_menu()
            else:
                prets(conn)
    #print("Compte n' existe pas")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre Numero de compte : ")
    montant_pret = input("Saisir le montant de l' argent à preter (100 000 Ariary au maximum) : ")
    while int(montant_pret) > 100000:
        montant_pret = input("Saisir le montant de l' argent à preter (100 000 Ariary au maximum) : ")
    date_pret = input("Saisir la date du pret : ")
    date_expiration = input("Saisir la date d' expiration(payement) : ")
    duree_pret = input("Veuillez saisir la duree du pret(2 mois maximum) :  ")
    while len(duree_pret) < 3:
        duree_pret = input("Veuillez saisir la duree du pret(2 mois maximum) :  ")
    cursor.execute(
        "insert into comptes(numero_compte, montant_pret,date_pret,date_expiration,duree_pret ) values (?,?,?,?,?);",
        (numero_compte, montant_pret, date_pret, date_expiration, duree_pret))
    print("Merci,\n Votre compte a été crée avec succées en plus votre pret a ete efferctiée avec succes")
    conn.commit()
    print("--------------------FIN DE PRET ---------------------")
    client_menu()


# rembouser le pret
def rembo(conn):
    print("----------------------BONJOUR----------------------")
    print("                                      REMBOURSEMENT D' ARGENT                          ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    mdp = input("Saisir votre mots de passe : ")
    cursor.execute("select * from compte where numero_compte=? AND mdp=?", (numero_compte,mdp))
    exist = cursor.fetchall()
    while exist:
        montant = int(input("Saisir le montant à rembourser : "))
        print("Numero de compte : ", numero_compte)
        cursor = conn.cursor()
        cursor.execute("update comptes set  montant_pret = montant_pret - ? where numero_compte=? ;",
                       (montant, numero_compte))
        cursor.execute("select * from comptes where numero_compte = ?", (numero_compte))
        montant_pret = cursor.fetchone()[1]
        montant_pret = int(montant_pret)
        if montant_pret > 0:
            print("Cher(e) Client(e),\n Merci beaucoup d' avoir payer votre pret")
            print("Mais,Il reste encore des comptes à regler")
            print("Numero de compte : ", numero_compte)
            print("Argent preter : ", montant_pret, "Ariary")
            print("Tapez 0 pour quitter")
            choice = input('Choisir votre selection: >>')
            while not choice.isdigit():
                choice = input('Choisir votre selection: >>')
            choice = int(choice)
            if choice == 0:
                client_menu()
            else:
                print("Votre remboursement est annulé")
                rembo(conn)
            conn.commit()
        else:
                print("Vou avez de remise de ", - montant_pret , "Ariary")
                print("Tapez 0 pour quitter")
                choice = input('Choisir votre selection: >>')
                while not choice.isdigit():
                    choice = input('Choisir votre selection: >>')
                choice = int(choice)
                if choice == 0:
                    client_menu()
                else:
                    rembo(conn)
    print("Compte n' existe pas")
    conn.commit()
    print("--------------------FIN DE REMBOURSEMENT ---------------------")
    client_menu()


# voir le solde actuel
def voir_solde(conn):
    print("----------------------BONJOUR----------------------")
    print("                                       VOIR SOLDE ACTUEL                                      ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    mdp = input("Saisir votre mots de passe : ")
    cursor.execute("select * from compte where numero_compte=? AND mdp=?", (numero_compte,mdp))
    exist = cursor.fetchall()
    if exist:
        cursor.execute("select * from compte where numero_compte = ?", (numero_compte))
        solde = cursor.fetchone()[9]
        print("Numero de compte: ", numero_compte)
        print("Cher(e) Client(e),\n Votre solde actuels est ", solde, " Ariary")
        conn.commit()
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            client_menu()
        else:
            voir_solde(conn)
    else:
        print("Numero de compte invalide ou n' existe pas")
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            client_menu()
        else:
            voir_solde(conn)


connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"


# voir le pret total
def voir_pret(conn):
    print("----------------------BONJOUR----------------------")
    print("                                       VOIR PRET TOTAL                                      ")
    print("----------------------------------------------------")
    cursor = conn.cursor()
    numero_compte = input("Saisir votre numero de compte pour vérifier : ")
    mdp = input("Saisir votre mots de passe : ")
    cursor.execute("select * from compte where numero_compte=? AND mdp=?", (numero_compte,mdp))
    exist = cursor.fetchall()
    if exist:
        cursor.execute("select * from comptes where numero_compte = ?", (numero_compte))
        montant_pret = cursor.fetchone()[1]
        print("Numero de compte: ", numero_compte)
        print("Cher(e) Client(e),\n Vous avez encore une dete de  ", montant_pret, " Ariary à payer")
        conn.commit()
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            client_menu()
        else:
            voir_pret(conn)
    else:
        print("Numero de compte invalide ou n' existe pas")
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            client_menu()
        else:
            voir_pret(conn)

#convertion monetaire
def convert():
    print("----------------------BONJOUR----------------------")
    print("                                       CONVERTION MONETAIRE                                      ")
    print("----------------------------------------------------")
    print("Quelle monaie vouliez-vous convertir")
    print(" 1.Euro en Ariary")
    print(" 2.Ariary en Euro")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        euro = int(input("Conversion Ariary -> Donner la valeur en Euros : "))
        ariary = euro * 4000
        franc = ariary *5
        print("La conversion de ",euro, "Euros vaut ",ariary," Ariary(",franc, "Fmg)")
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            client_menu()
        else:
            convert()
    elif choice == 2:
        ariary = int(input("Conversion Euros -> Donner la valeur en Ariary : "))
        euro = ariary / 4000
        franc = ariary*5
        print("La conversion de ", ariary, "Ariary(",franc, "Fmg)" " vaut ", euro, " Euros")
        print("Tapez 0 pour quitter")
        choice = input('Choisir votre selection: >>')
        while not choice.isdigit():
            choice = input('Choisir votre selection: >>')
        choice = int(choice)
        if choice == 0:
            client_menu()
        else:
            convert()
    else:
        print("Vous devez choisir  1 ou 0")
        convert()
#  administrateur authentification
def authentification(username, password):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "SELECT COUNT(*) from login where username=? AND password=?"
    cursor.execute(query, (username, password))
    existe = cursor.fetchone()[0]
    if existe:
        print("Authentification reussite avec succèes")
        admin_menu()
    else:
        print("Echec d' authentification")
        main_menu()
    conn.close()


# client authentification
def authen_client(numero_compte, mdp):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "SELECT COUNT(*) from compte where numero_compte=? AND mdp=?"
    cursor.execute(query, (numero_compte, mdp))
    existe = cursor.fetchone()[0]
    if existe:
        print("Authentification reussite avec succèes")
        client_menu()
    else:
        print("Echec d' authentification")
        main_menu()
    conn.close()


# menu principal
def main_menu():
    print("                                   GESTION BANCAIRE                                      ")
    print("----------------------------------------------------")
    print("                        Bienvenue dans notre Application ('_')                      ")
    print("                         1.Admin Authentification\n"
          "                        2.Client Authentification\n"
          "                        0.Quitter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input("Choisir votre selection: >>")
    choice = int(choice)
    if choice == 1:
        print("----------------------BONJOUR----------------------")
        print("                        ADMIN AUTHENTIFICATION                                  ")
        print("----------------------------------------------------")
        username = input("Saisir votre nom : ")
        password = input("Saisir votre mots de passe : ")
        authentification(username, password)
    elif choice == 2:
        print("----------------------BONJOUR----------------------")
        print("                        CLIENT AUTHENTIFICATION                                  ")
        print("----------------------------------------------------")
        numero_compte = input("Saisir votre numero de compte : ")
        mdp = input("Saisir votre mots de passe : ")
        authen_client(numero_compte, mdp)
    elif choice == 0:
        exit()
    else:
        print("Choix  invalide")
        main_menu()

main_menu()