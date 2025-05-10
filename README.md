# 🛡️ Sistema de Login com Interface Moderna (CustomTkinter)

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)](https://www.sqlite.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey?logo=python)](https://docs.python.org/3/library/tkinter.html)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-blueviolet)](https://github.com/TomSchimansky/CustomTkinter)
[![PIL](https://img.shields.io/badge/Pillow-Imagens-yellow)](https://pillow.readthedocs.io/en/stable/)

---

## 📸 Demonstrações

### Funcionalidade:
![Login](prints/login_tela.png)

### Tela de Cadastro:
![Cadastro](prints/cadastro_tela.png)

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **CustomTkinter** → interface moderna com visual clean e responsivo.
- **SQLite3** → banco de dados local para persistência dos usuários.
- **Tkinter / CTk Widgets** → entradas, botões, checkboxs, frames.
- **Pillow (PIL)** → renderização de imagens (como logos ou ícones).

---

## 🔐 Funcionalidades

- Cadastro de novos usuários com validação de campos.
- Validação de senha e confirmação.
- Login de usuários com verificação no banco de dados.
- Visualização ou ocultação de senha.
- Interface moderna e intuitiva.
- Banco de dados SQLite local.
- Feedback via `messagebox` para ações do usuário.

---

## ⚙️ Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/sistema-login-customtkinter.git

# 2. Entre na pasta do projeto
cd sistema-login-customtkinter

# 3. Instale os pacotes necessários
pip install customtkinter pillow openpyxl

# 4. Execute a aplicação
python main.py
