from tkinter import messagebox
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

    def cadastrar_usuario(self):
        self.username_register = self.username_register_entry.get()
        self.email_register = self.username_email_entry.get()
        self.password_register = self.password_register_entry.get()
        self.confirm_pwd_register = self.password_confirm_entry.get()

    # Verificações de validação
        if self.username_register == '' or self.email_register == '' or self.password_register == '' or self.confirm_pwd_register == '':
            messagebox.showwarning('Sistema de Login', 'Por favor, preencha todos os campos')
            return

        elif len(self.username_register.strip()) < 4:
            messagebox.showwarning('Sistema de Login', 'O nome de usuário deve ter pelo menos 4 caracteres')
            return

        elif len(self.password_register.strip()) < 4:
            messagebox.showwarning('Sistema de Login', 'A senha deve ter pelo menos 4 caracteres')
            return

        elif self.password_register != self.confirm_pwd_register:
            messagebox.showwarning('Sistema de Login', 'As senhas não coincidem')
            return

        try:
            self.connect_db()
            self.curr.execute('''INSERT INTO users(username, email, password, password_confirm) VALUES (?, ?, ?, ?)''',
                            (self.username_register, self.email_register, self.password_register, self.confirm_pwd_register))
            self.conn.commit()
            messagebox.showinfo('Sistema de Login', f'*** Cadastro de {self.username_register} efetuado com sucesso! ***')
            self.clean_entry_register()

        except Exception as e:
            messagebox.showerror('Sistema de Login', f'--| Erro ao cadastrar: {e} |--')
        finally:
            self.desconnect_db()

    def verifica_login(self):        
        self.username_login = self.username_login_entry.get()
        self.pw_login = self.pw_login_entry.get()

        self.connect_db()

        # --> verifica se usuario existe
        self.curr.execute('''SELECT * FROM Users WHERE (username=? AND password=?)''', (self.username_login, self.pw_login))

        self.verifica_dados = self.curr.fetchone()

        try:
            if self.username_login == '' or self.pw_login == '':
                messagebox.showerror('Sistema de Login', 'Ambos campos precisam estar preenchidos!\nPor favor, tente novamente.')
            
            elif self.username_login in self.verifica_dados and self.pw_login in self.verifica_dados:
                messagebox.showinfo('Sistema de Login', f'Parabéns, {self.username_login}!\nLogin efetuado com sucesso! ')
                self.desconnect_db()
                self.clean_entry_login()
        except:
            messagebox.showerror('Sistema de Login', 'Dados não encontrados em nosso sistema\nPor favor, verifique seus dados ou cadastre-se no sistema')
            self.desconnect_db()


class App(ctk.CTk, Backend):
    def __init__(self):
        super().__init__()
        self.janela_principal_config()
        self.tela_login()
        self.create_table()

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
 
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Digite seu usuário', font=('Roboto',16), corner_radius=15, border_color='#1867A9')
        self.username_login_entry.grid(row=1,column=0, padx=10,pady=10)

        # --> criando entry de senha user no frame login

        self.pw_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Digite sua senha', font=('Roboto',16), corner_radius=15, border_color='#1867A9', show='*')
        self.pw_login_entry.grid(row=2,column=0, padx=10,pady=10)

        # --> criando checkbox pra ver senha
        
        self.show_password = ctk.CTkCheckBox(
            self.frame_login, 
            text='Ver senha', 
            font=('Roboto',12), 
            corner_radius=20,
            command=self.toggle_password_login  # <-- comando chamado ao clicar
            )
        self.show_password.grid(row=3, column=0, padx=10, pady=10)


        # --> criando button de login

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text='Fazer Login'.upper(), command=self.verifica_login, font=('Roboto bold',12), corner_radius=15, fg_color='#1E90FF', hover_color='#1C86EE')
        self.btn_login.grid(row=4,column=0, padx=10,pady=10)

        # --> 
        self.spam = ctk.CTkLabel(self.frame_login, text='Não possui registro? Clique no botão abaixo e registre-se ', font=("Roboto bold", 10))
        self.spam.grid(row=5,column=0, padx=10,pady=10)

        # --> criando button cadastro

        self.btn_register = ctk.CTkButton(self.frame_login, width=300, text='Cadastrar'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#28A745', hover_color='#218838', command=self.tela_cadastro)
        self.btn_register.grid(row=6,column=0, padx=10,pady=10)

    def toggle_password_login(self):
        if self.show_password.get() == 1:
            self.pw_login_entry.configure(show='')  # mostra senha
        else:
            self.pw_login_entry.configure(show='*')  # oculta senha

    def toggle_password_register(self):
        if self.show_password_checkbox.get() == 1:
            self.password_register_entry.configure(show='')
            self.password_confirm_entry.configure(show='')
        else:
            self.password_register_entry.configure(show='*')
            self.password_confirm_entry.configure(show='*')


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

        self.show_password_checkbox = ctk.CTkCheckBox(
        self.frame_register, 
        text='Ver senha', 
        font=('Roboto',12), 
        corner_radius=20,
        command=self.toggle_password_register  # <-- chama comando
        )
        self.show_password_checkbox.grid(row=5,column=0,pady=5)

        self.btn_register_user = ctk.CTkButton(self.frame_register, width=300, text='Cadastrar'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#28A745', hover_color='#218838', command=self.cadastrar_usuario)
        self.btn_register_user.grid(row=6,column=0, padx=10,pady=5)

        self.btn_login_back = ctk.CTkButton(self.frame_register, width=300, text='Voltar ao Login'.upper(), font=('Roboto bold',12), corner_radius=15, fg_color='#1f6666', hover_color='#0f3a3a', command=self.tela_login)
        self.btn_login_back.grid(row=7,column=0, padx=10,pady=5)

    def clean_entry_register(self):
        self.username_register_entry.delete(0, END)
        self.username_email_entry.delete(0, END)
        self.password_register_entry.delete(0, END)
        self.password_confirm_entry.delete(0, END)

    def clean_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.pw_login_entry.delete(0, END)

if __name__ == '__main__':
    app = App()
    app.mainloop()
