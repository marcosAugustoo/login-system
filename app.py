import customtkinter as ctk
import sqlite3 as sql

from tkinter import *
from openpyxl import workbook
from PIL import Image  # <-- IMPORTANTE para lidar com imagens

# setando aparencia padrão do sistema

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

class Backend():
    def connect_db(self):
        self.conn = sql.connect("sistema_cadastro_usuario.db")
        self.curr = self.conn.cursor()
        print('---||--- Banco de dados conectado com sucesso! ---||---')

    def desconnect_db(self):
        self.conn.close()
        print('---||--- Banco de dados desconectado! ---||---')

    def create_table(self):
        self.connect_db()
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NN,
                        email TEXT NN,
                        password TEXT NN,
                        password_confirm TEXT NN
                                            );
                        """)
        self.conn.commit()
        print('---||--- Tabela criada com sucesso! ---||---')
        self.desconnect_db()

    def user_register(self):
        self.username_register = self.username_register_entry.get()
        self.email_register = self.username_email_entry.get()
        self.password_register = self.password_register_entry.get()
        self.confirm_pwd_register = self.password_confirm_entry.get()

        self.connect_db()

        self.curr.execute('''
            INSERT INTO users(username, email, password, password_confirm)
            VALUES (?,?,?,?)''',
        (self.username_register, self.email_register, self.password_register, self.confirm_pwd_register))
        
        self.conn.commit()
        print('---||--- Dados cadastrados com sucesso! ---||---')
        self.desconnect_db()

class App(ctk.CTk, Backend):
    def __init__(self):
        super().__init__()
        self.janela_principal_config()
        self.create_table()
        self.tela_login()

    # configurando a janela principal

    def janela_principal_config(self):
        self.title('Sistema de Login')
        self.geometry('700x400')
        self.resizable(False, False)

    def tela_login(self):

    
        # trabalhando com imgs
        imagem_pil = Image.open('rocket.png')
        self.img = ctk.CTkImage(dark_image=imagem_pil, size=(300, 300))  # Ajuste o tamanho como quiser
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)

        # --> titulo da tela

        self.title = ctk.CTkLabel(self, text = 'Faça Login ou Cadastre-se\nem nossa plataforma para acessar\nnossos serviços', font=("Roboto bold",18))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        # --> frame do formulario de login

        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350,y=10)

        # --> colocando widgets dentro do frame formulario login

        self.lb_title = ctk.CTkLabel(self.frame_login, text = 'Faça Login', font = ('Roboto', 22))
        self.lb_title.grid(row=0, column=0,padx=10,pady=10)

        # --> criando entry de usuario no frame login
 
        self.username_login = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Digite seu usuário', font=('Roboto',16), corner_radius=15, border_color='#1867A9')
        self.username_login.grid(row=1,column=0, padx=10,pady=10)

        # --> criando entry de senha user no frame login

        self.username_password = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Digite sua senha', font=('Roboto',16), corner_radius=15, border_color='#1867A9', show='*')
        self.username_password.grid(row=2,column=0, padx=10,pady=10)

        # --> criando checkbox pra ver senha
 
        self.show_password = ctk.CTkCheckBox(self.frame_login, text='Ver senha', font=('Roboto',12), corner_radius=20)
        self.show_password.grid(row=3,column=0, padx=10,pady=10)

        # --> criando button de login

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text='Fazer Login'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#1E90FF', hover_color='#1C86EE')
        self.btn_login.grid(row=4,column=0, padx=10,pady=10)

        # --> 
        self.spam = ctk.CTkLabel(self.frame_login, text='Não possui registro? Clique no botão abaixo e registre-se ', font=("Roboto bold", 10))
        self.spam.grid(row=5,column=0, padx=10,pady=10)

        # --> criando button cadastro

        self.btn_register = ctk.CTkButton(self.frame_login, width=300, text='Cadastrar'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#28A745', hover_color='#218838', command=self.tela_cadastro)
        self.btn_register.grid(row=6,column=0, padx=10,pady=10)
        
    def tela_cadastro(self):
        # --> remove formulario de login

        self.frame_login.place_forget()

        # --> CRIANDO frame de cadastro
        self.frame_register = ctk.CTkFrame(self, width=350, height=380)
        self.frame_register.place(x=350,y=10)

        self.lb_title = ctk.CTkLabel(self.frame_register, text = 'Cadastre-se', font = ('Roboto', 22))
        self.lb_title.grid(row=0, column=0,padx=10,pady=10)

        # --> CRIANDO titulo

        self.title = ctk.CTkLabel(self, text = 'Faça Login ou Cadastre-se\nem nossa plataforma para acessar\nnossos serviços', font=("Roboto bold",18))
        self.title.grid(row=0, column=0, pady=10, padx=5)    

        self.username_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Digite seu usuário', font=('Roboto',16), corner_radius=15, border_color='#1867A9')
        self.username_register_entry.grid(row=1,column=0, padx=10,pady=5)

        self.username_email_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Email de usuário', font=('Roboto',16), corner_radius=15, border_color='#1867A9')
        self.username_email_entry.grid(row=2,column=0, padx=10,pady=5)

        self.password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Senha de usuário', show='*', font=('Roboto',16), corner_radius=15, border_color='#1867A9')
        self.password_register_entry.grid(row=3,column=0, padx=10,pady=5)

        self.password_confirm_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Confirma senha', font=('Roboto',16), corner_radius=15, border_color='#1867A9', show='*')
        self.password_confirm_entry.grid(row=4,column=0, padx=10,pady=5)

        self.show_password_checkbox = ctk.CTkCheckBox(self.frame_register, text='Ver senha', font=('Roboto',12), corner_radius=20)
        self.show_password_checkbox.grid(row=5,column=0,pady=5)

        self.btn_register_user = ctk.CTkButton(self.frame_register, width=300, text='Cadastrar'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#28A745', hover_color='#218838', command=self.user_register)
        self.btn_register_user.grid(row=6,column=0, padx=10,pady=5)

        self.btn_login_back = ctk.CTkButton(self.frame_register, width=300, text='Voltar ao Login'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#1f6666', hover_color='#0f3a3a', command=self.tela_login)
        self.btn_login_back.grid(row=7,column=0, padx=10,pady=5)

        def clean_entry_register(self):
            self.username_password.delete(0, END)
            self.username_email.delete(0, END)
            self.password_register.delete(0, END)
            self.password_confirm.delete(0, END)

        def clean_entry_login(self):
            self.username_login.delete(0, END)
            self.username_password.delete(0, END)

if __name__ == '__main__':
    app = App()
    app.mainloop()
