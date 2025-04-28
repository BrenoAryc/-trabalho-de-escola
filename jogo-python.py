from tkinter import *
import random

def verificar():
    palpite = int(caixatexto.get())
    if palpite == numero:
        resultado["text"] = "Parabéns! Você acertou!"
    else:
        resultado["text"] = "Tente novamente!"

numero = random.randint(0, 10)

janela = Tk()
janela.title("Jogo")
janela.geometry("800x600")
janela.resizable(False, False)

instrucoes = Label(janela, text="Digite um número entre 0 a 10:")
instrucoes.pack(pady=20)

caixatexto = Entry(janela)
caixatexto.pack(padx=10, pady=10)

botao = Button(janela, text="Enviar", pady=14, padx=14, bd=4, command=verificar, background="lightgreen")
botao.place(x=360, y=200)

resultado = Label(janela, text="")
resultado.place(x=348, y=280)

janela.bind("<Return>", lambda event: botao.invoke())

janela.mainloop()
