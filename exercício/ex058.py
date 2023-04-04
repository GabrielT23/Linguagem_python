from random import randint
from tkinter import *
c = randint(1, 10)
tentativas = 1
def adivinhacao():
    s = int(palpite.get())
    if s == c:
        msg2["text"] = "acertou"
    else:
        msg2["text"] = "errou"

print("C=", c)
janela = Tk()
janela.title("Adivinhação")
janela.geometry("490x560+610+153")
janela.resizable(width=1, height=1)
msg = Label(janela, text="Sou seu computador...\n"
                         "Acabei de pensar em um numero entre 0 e 10."
                         " Será que você consegue advinhar qual foi?")
msg.grid(column=0, row=0)
palpite = Entry(janela, bd=2, font=("Calibri", 15), justify= CENTER)
palpite.place(width= 392, height=45, x=49, y=138)
botao = Button(janela, text="Adivinhar", command=adivinhacao)
botao.grid(column=0, row=2)
msg2 = Label(janela, text="")
msg2.grid(column=0, row=3)



janela.mainloop()