from tkinter import *
from tkinter import massagebox #importa o modulo de caixas de mensagem do tkinter
from tkinter import ttk#importa o modulo de widgets tematicos do tkinter
from dataclasses import database#importa a classe Database do modulo DataBase

#cria a janela
jan = Tk()
jan.title("SL Sytens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False)

#deixar a tela transparente
jan.attributes("-alpha, 0.9")
jan.iconbitmap(default="C:/Users/caio_battisti/Documents/GitHub/foto/logo.png")#carrega a imagem da logo

#cria a Frame
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE",relief="raise")#cria a frame a esquerda
LeftFrame.pack(side=LEFT)
RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE",relief="raise")#cria a frame a direita
RightFrame.pack(side=RIGHT)

#adicionar o logo
Logolabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")#cria im label para a imgem ao lado
Logolabel.place(x=50, y=100)#posiciona o label no frame esquerdo

#aicionar campos de usuario e senha
