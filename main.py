from tkinter import RIGHT, PhotoImage
import customtkinter

customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme ("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.resizable(False, False)

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")

email =customtkinter.CTkEntry(janela,
                              placeholder_text="E-mail")

senha =customtkinter.CTkEntry(janela,
                              placeholder_text="Senha",
                              show="*")

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar senha")

botao = customtkinter.CTkButton(janela, text="Login",
                                command=clique)


texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
checkbox.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
janela.mainloop()