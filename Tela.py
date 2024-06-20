import tkinter as tk
import GeraQr as qr

def CriarTela():

    tela = tk.Tk() # Instancia o objeto
    tela.title("QR Code") # Título da Aba

    largura = 400   # Tamanho da tela
    altura = 400    # Tamanho da tela

    largura_tela = tela.winfo_screenwidth() # Capturando o tamanho da tela do user
    altura_tela = tela.winfo_screenheight() # Capturando o tamanho da tela do user
    
    pos_x = (largura_tela // 2) - (largura // 2) #Calculando o meio da tela
    pos_y = (altura_tela // 2) - (altura // 2)  #Calculando o meio da tela 

    tela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y-50}")

    titulo = tk.Label(tela, text="Scan me!", font= ("Arial", 20)) # Criando o título
    titulo.pack(pady=20) # Ajustando a posição

    url = "https://github.com/txKaue"
    qr.GerarImagem(tela, url)

    tela.mainloop() # Isso aqui mantém a tela aberta


if __name__ == "__main__":
    CriarTela()
