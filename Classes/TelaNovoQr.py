import tkinter as tk
import Tela
import json
import os
from Classes import VerificaUrl

url = ""

def adicionar_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: remover_placeholder(entry, placeholder))
    entry.bind("<FocusOut>", lambda event: restaurar_placeholder(entry, placeholder))

def remover_placeholder(entry):
    entry.delete(0, tk.END)  
    entry.config(fg='black')  

def restaurar_placeholder(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def TelaAlterarQr():
    nova_janela = tk.Tk()
    nova_janela.title("Nova Janela")

    largura = 350 
    altura = 150

    largura_tela = nova_janela.winfo_screenwidth() # Capturando o tamanho da tela do user
    altura_tela = nova_janela.winfo_screenheight() # Capturando o tamanho da tela do user
    
    pos_x = (largura_tela // 2) - (largura // 2) #Calculando o meio da tela
    pos_y = (altura_tela // 2) - (altura // 2)  #Calculando o meio da tela 

    nova_janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y-50}")

    txtBox = tk.Entry(nova_janela, width=30, font=("Arial", 12))
    txtBox.pack(pady=20)

    placeholder_texto = "Nova url (link)"
    adicionar_placeholder(txtBox, placeholder_texto)

    def AtualizarPagina():
        texto = txtBox.get()
        if texto != placeholder_texto:
            print(f"Texto inserido: {texto}")
            url = texto

            status = VerificaUrl.VerificaUrl(url)

            if status == True:

                caminho_arquivo = '../TKINTERTESTE/Data/data.json'
                diretorio_atual = os.getcwd()
                caminho_completo = os.path.join(diretorio_atual, caminho_arquivo)
                if not os.path.exists(caminho_completo):
                    print(f"Arquivo não encontrado: {caminho_completo}")
                    return

                with open(caminho_completo, 'r') as file:
                    dados = json.load(file)

                dados['url'] = url

                with open(caminho_completo, 'w') as file:
                    json.dump(dados, file, indent=4)

                nova_janela.destroy()
                Tela.CriarTela(url)

            else:
                remover_placeholder(txtBox)
                adicionar_placeholder(txtBox, "Url inválida")

            

    botao_capturar = tk.Button(nova_janela, text="Confirmar", command=AtualizarPagina)
    botao_capturar.pack(pady=10)
