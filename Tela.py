import tkinter as tk
import GeraQr as qr
import TelaNovoQr 



def CriarTela(url):

    def BotaoClick():
        tela.destroy()
        TelaNovoQr.TelaAlterarQr()
        

    tela = tk.Tk() # Instancia o objeto
    tela.title("QR Code") # Título da Aba

    largura = 400   # Tamanho da tela
    altura = 500    # Tamanho da tela

    largura_tela = tela.winfo_screenwidth() # Capturando o tamanho da tela do user
    altura_tela = tela.winfo_screenheight() # Capturando o tamanho da tela do user
    
    pos_x = (largura_tela // 2) - (largura // 2) #Calculando o meio da tela
    pos_y = (altura_tela // 2) - (altura // 2)  #Calculando o meio da tela 

    tela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y-50}")

    titulo = tk.Label(tela, text="Scan me!", font= ("Arial", 20)) # Criando o título
    titulo.pack(pady=20) # Ajustando a posição

    if (url == ""):
        url_que_vai = "https://github.com/txKaue"
    else:
        url_que_vai = url
        
    qr.GerarImagem(tela, url_que_vai)

    btnNovoQr = tk.Button(
        tela, 
        text="Gerar novo QR", 
        command=BotaoClick,
        bg="#98FB98",
        width=20, 
        height=2,
        font=("Arial", 12),
        relief=tk.GROOVE,
        ) 
    
    btnNovoQr.pack(pady=0) # Ajustando a posição do botão

    tela.mainloop() # Isso aqui mantém a tela aberta


if __name__ == "__main__":
    CriarTela("")
