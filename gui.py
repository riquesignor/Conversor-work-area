import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from conversor import converter_imagem, FORMATOS_SAIDA


def escolher_arquivo():
    caminho = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.webp")]
    )
    if caminho:
        entrada_var.set(caminho)


def converter():
    try:
        novo = converter_imagem(entrada_var.get(), formato_var.get())
        messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{novo}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


janela = tk.Tk()
janela.title("Conversor de Imagens")
janela.geometry("420x160")
janela.resizable(False, False)

entrada_var = tk.StringVar()
formato_var = tk.StringVar(value="png")

tk.Button(janela, text="Escolher imagem", command=escolher_arquivo).pack(pady=8)
tk.Label(janela, textvariable=entrada_var, wraplength=400).pack()

ttk.Combobox(
    janela, textvariable=formato_var, values=sorted(FORMATOS_SAIDA), state="readonly"
).pack(pady=8)

tk.Button(janela, text="Converter", command=converter).pack(pady=8)

janela.mainloop()