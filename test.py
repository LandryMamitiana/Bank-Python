import pyodbc
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
     "SERVER=DEVSECOPS;"
     "DATABASE=bank;"
    "Trusted_Connection=yes;"
 )
def affiche():
    print("1.Ajouter compte")
    print("2.Supprimer compte")
    print("3.Modifier compte")
    print("4.Voir tous les compte")
    print("0.Quiter")
    choice = input('Choisir votre selection: >>')
    while not choice.isdigit():
        choice = input('Choisir votre selection: >>')
    choice = int(choice)
    if choice == 1:
        create(conn)
    elif choice == 2:
        delete(conn)
    elif choice == 3:
        update(conn)
    elif choice == 4:
        read(conn)
    elif choice == 0:
        avis = 'o'
        print("Voulez-vous vraiment qutter cette application(o/n)?")
        if avis=='o':
          main_menu()
        else:
          admin_menu()

        exit()

if conn:
    print("Connected")
else:
    print("eurreur")

def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("select * from login")
    for row in cursor:
        print(f"row={row}")
    print()

def create(conn):
    print("create")
    cursor = conn.cursor()
    print("Saisir votre nom:")
    username = input()
    print("Saisir votre mots de passe:")
    password = input()
    cursor.execute(" insert into login(username,password) values (?,?);",(username,password))
    conn.commit()
    read(conn)


def delete(conn):
    print("delete")
    cursor = conn.cursor()
    print("Saisir votre nom à supprimer: ")
    username = input()
    cursor.execute("delete from login where username = ?",(username));
    conn.commit()
    read(conn)

def update(conn):
    print("update")
    print("Saisir votre nom à modifier:")
    username = input()
    print("Saisir votre mots de passe à modifier:")
    password = input()
    cursor = conn.cursor()
    cursor.execute("update login set password=? where username=? ;",(password,username))
    conn.commit()
    read(conn)

affiche()