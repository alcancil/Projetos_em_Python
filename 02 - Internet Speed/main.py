# importar biblioteca de interface grafica
from tkinter import *

# importando o pillow
from PIL import Image, ImageTk

# importando o speedtest
import speedtest

# cores

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue

# criando a janela

janela = Tk ()
janela.title("")
janela.geometry('320x200')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=False)

# dividindo a janela em 2 frames

frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando o frame_logo
imagem = Image.open("speed.png")
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor="nw", font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=20, y=0)
l_logo_nome = Label(frame_logo, text="INTERNET SPEED", padx=10, anchor=NE, font=('Ivy 18 bold'), bg=co1, fg=co4)
l_logo_nome.place(x=75, y=10)

# configurando a linha divide frames
l_logo_linha = Label(frame_logo, width=350, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_logo_linha.place(x=0, y=57)

# Funçao calcular Upload e Download
def main():
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"

    l_download['text'] = download
    l_upload['text'] = upload

    botao_testar['text'] = 'NOVO TESTE'
    botao_testar.place(x=115, y=100)

# configurando o frame_corpo
l_download = Label(frame_corpo, text="", anchor=NW, font=('arial 26 bold'), bg=co1, fg=co4)
l_download.place(x=10, y=25)
l_download_mb = Label(frame_corpo, text="Mbps Download", anchor=NW, font=('ivy 10 bold'), bg=co1, fg=co4)
l_download_mb.place(x=15, y=70)

# configurando imagem down 
imagem_down = Image.open("down.png")
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)
l_logo_imagem = Label(frame_corpo, height=60, image=imagem_down, compound=LEFT, padx=10, anchor="nw", font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=120, y=25)

# configurando o frame_corpo
l_upload = Label(frame_corpo, text="", anchor=NW, font=('arial 26 bold'), bg=co1, fg=co4)
l_upload.place(x=220, y=25)
l_upload_mb = Label(frame_corpo, text="Mbps Upload", anchor=NW, font=('ivy 10 bold'), bg=co1, fg=co4)
l_upload_mb.place(x=220, y=70)

# configurando imagem up
imagem_up = Image.open("up.png")
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)
l_logo_imagem = Label(frame_corpo, height=60, image=imagem_up, compound=LEFT, padx=10, anchor="nw", font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=165, y=25)

# configurando o botão testar
botao_testar = Button(frame_corpo, command=main, text="INICIAR TESTE" , font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1)
botao_testar.place(x=115, y=95)

janela.mainloop ()