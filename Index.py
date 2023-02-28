#Importar as Bliblio
from sqlite3.dbapi2 import TimeFromTicks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar Nossa Janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
#jan.attributes("-alpha", 0,9)
#jan.iconbitmap(default="icons/LogoIcon.ico")
#====== Carregando Image =====
#logo = PhotoImage(file= "icons/logo.png")



#====== Widgests =======

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
#type: ignoreLeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=390, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#logoLabel = Label(LeftFrame,image = logo, bg="MIDNIGHTBLUE" )
#logoLabel.place(x= 50, y = 100)

userLabel = Label(RightFrame, text="Username: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg = "White")
userLabel.place(x= 5, y = 100)

userEntry = ttk.Entry(RightFrame, width=30)
userEntry.place(x= 150, y = 110)
#
PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg = "White")
PassLabel.place(x= 5, y = 150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x= 150, y = 160)

def Login():
    User = userEntry.get()
    Pass = PassEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """,(User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if  (User in VerifyLogin and Pass in VerifyLogin ):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo!")
    except:
        messagebox.showerror(title="Login Info", message="Acesso Negado. Verifique se esta Cadastrado No Sistema!")

#botoes
loginButton = ttk.Button(RightFrame, text=" Login ", width=30, command=Login)
loginButton.place(x = 100, y = 225)

def Register():
    #Removendo Widgest de Login
    loginButton.place(x = 5000)
    RegisterButton.place(x= 5000)
    
    #inserindo Widgets de cadastro
    nomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic",20), bg= "MIDNIGHTBLUE", fg= "White")
    nomeLabel.place(x= 5, y= 5)
    
    nomeEntry = Entry(RightFrame, width=39)

    nomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:",font=("Century Gothic",20) , bg="MIDNIGHTBLUE", fg="white" )
    EmailLabel.place(x=5, y= 55)

    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = nomeEntry.get()
        Email = EmailEntry.get()
        User = userEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email == "" and User=="" and Pass==""):
            messagebox.showerror(title="Register Error", message="Nao Deixe Nenhum Campo Em Branco")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")

    
    
    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x= 100, y=225)

    def BackToLogin():
        #removendo Widgets de cadastro
        nomeLabel.place(x=5000)
        nomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os Widgets de Login
        loginButton.place(x = 100)
        RegisterButton.place(x= 125)
    
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)




RegisterButton = ttk.Button(RightFrame, text=" Register ", width=20, command=Register)
RegisterButton.place(x= 125, y=260)




jan.mainloop()

