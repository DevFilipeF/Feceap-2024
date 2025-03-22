
# NÃO MEXER POIS ESTA FUNCIONANDO SEM CONFLITOS!!!

# TKINTER
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

from loginbd import Database  

import subprocess
import sys

app = QApplication([])

pixmap = QPixmap(r"c:\Users\Israel\Downloads\RECICLAFACIL COM BD\ReciclaFacilPY\images\logoee.png")
janela = ctk.CTk()

class Application():
    
    def __init__(self):
        self.janela = janela
        self.db = Database()
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Login")
        janela.resizable(False, False)
        janela.iconbitmap(r"c:\Users\Israel\Downloads\RECICLAFACIL COM BD\ReciclaFacilPY\images\logo.ico")


    def tela_login(self):
        img = PhotoImage(file=r"c:\Users\Israel\Downloads\RECICLAFACIL COM BD\ReciclaFacilPY\images\logoee.png")
        label_img = ctk.CTkLabel(master=janela, image=img, text="")
        label_img.place(x=5, y=65)

        title_label = ctk.CTkLabel(master=janela, text="  Entre na sua conta e acesse \n a plataforma ", font=("Roboto", 20), text_color="green").place(x=15, y=10)

    # Frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

    # Widgets do Frame
        label = ctk.CTkLabel(master=login_frame, text="Login", font=("Roboto", 20))
        label.place(x=25, y=5)

        self.username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuario", width=300, font=("Roboto", 14))
        self.username_entry.place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo nome de usuario é obrigatório.", text_color="green", font=("Roboto", 10)).place(x=25, y=135)

        self.password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*")
        self.password_entry.place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo senha é obrigatório.", text_color="green", font=("Roboto", 10)).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar de mim")
        checkbox.place(x=25, y=235)

        # Mantemos o login e adicionamos a abertura de outro arquivo
        login_button = ctk.CTkButton(master=login_frame, text="ENTRAR", width=300, command=self.login_e_abrir)
        login_button.place(x=25, y=285)

        register_span = ctk.CTkLabel(master=login_frame, text="Se não possui uma conta").place(x=25, y=325)

        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2D9334", command=self.tela_register)
        register_button.place(x=175, y=325)
        
    def login_e_abrir(self):
    # Chama a função original de login
        login_sucesso = self.login()
    
        if login_sucesso:
        # Se o login for bem-sucedido, abre o outro arquivo Python
            subprocess.Popen(["python", r"c:\Users\Israel\Downloads\RECICLAFACIL COM BD\ReciclaFacilPY\main.py"])


    def verify_login(self, username, password):
        self.db.cursor.execute("SELECT * FROM users WHERE Username=? AND Password=?", (username, password))
        return self.db.cursor.fetchone() is not None

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos obrigatórios.")
            return

        if self.verify_login(username, password):
            messagebox.showinfo(message="Login feito com sucesso!", title="Estado do Login")
          
            
             # Fecha a janela atual
            self.janela.destroy()
        
            # Abre o próximo arquivo Python
            subprocess.Popen([sys.executable, r"c:\Users\Israel\Downloads\RECICLAFACIL COM BD\ReciclaFacilPY\main.py"])
            
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

 
    def tela_register(self):
        # Removendo Frame de login
        for widget in self.janela.winfo_children():
            widget.pack_forget()

        # Tela Cadastro
        rg_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        rg_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(master=rg_frame, text="Faça o seu cadastro", font=("Roboto", 20)).place(x=24, y=5)
        span = ctk.CTkLabel(master=rg_frame, text="Por Favor preencha todos os campos corretamente!", font=("Roboto", 10), text_color="gray").place(x=25, y=65)

       
        self.reg_email_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Email", width=300, font=("Roboto", 14))
        self.reg_email_entry.place(x=25, y=105)

        self.reg_username_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome de usuario", width=300, font=("Roboto", 14))
        self.reg_username_entry.place(x=25, y=145)


        self.reg_password_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*")
        self.reg_password_entry.place(x=25, y=185)

        self.reg_cPassword_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirme a Senha", width=300, font=("Roboto", 14), show="*")
        self.reg_cPassword_entry.place(x=25, y=225)

        self.reg_pix_entry = ctk.CTkEntry(master=rg_frame, placeholder_text="Pix", width=300, font=("Roboto", 14))
        self.reg_pix_entry.place(x=25, y=265)


        self.checkbox_terms = ctk.CTkCheckBox(master=rg_frame, text="Aceito todos os Termos e Políticas")
        self.checkbox_terms.place(x=25, y=305)

        back_button = ctk.CTkButton(master=rg_frame, text="VOLTAR", width=145, fg_color="gray", hover_color="#202020", command=self.back)
        back_button.place(x=25, y=345)

        save_button = ctk.CTkButton(master=rg_frame, text="CADASTRAR", width=145, fg_color="green", hover_color="#014B05", command=self.save_user)
        save_button.place(x=180, y=345)

    def back(self):
        # Removendo frame de cadastro
        for widget in self.janela.winfo_children():
            widget.pack_forget()

        # Voltando com frame de login
        self.tela_login()

    def save_user(self):
        username = self.reg_username_entry.get()
        email = self.reg_email_entry.get()
        password = self.reg_password_entry.get()
        confirm_password = self.reg_cPassword_entry.get()
        pix = self.reg_pix_entry.get()
        terms_accepted = self.checkbox_terms.get()

        if not username or not email or not password or not confirm_password or not pix:
            messagebox.showwarning("Aviso", "Por favor preencha todos os campos obrigatórios.")
            return

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        if not terms_accepted:
            messagebox.showerror("Erro", "Você deve aceitar os termos e políticas.")
            return

        # Salvar no banco de dados
        try:
            self.db.insert_user(username, email, password, confirm_password,pix)
            messagebox.showinfo(title="Cadastro", message="Cadastro bem-sucedido!")
            # Volta para a tela de login após cadastro
            self.back()  
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

# SPLASH SCREEN
splash = QSplashScreen()
splash.setPixmap(pixmap)

QTimer.singleShot(5000, splash.close)
QTimer.singleShot(5000, Application)

splash.show()
app.exec_()
