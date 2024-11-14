import tkinter as tk
from tkinter import ttk

# Função para calcular e atualizar as estatísticas
def calcular_estatisticas():
    try:
        # Obtém os valores das entradas (ou define como 0 se vazio)
        c = int(entry_c.get() or 0)
        cpp = int(entry_cpp.get() or 0)
        csharp = int(entry_csharp.get() or 0)
        java = int(entry_java.get() or 0)
        javascript = int(entry_javascript.get() or 0)
        php = int(entry_php.get() or 0)
        ruby = int(entry_ruby.get() or 0)
        r = int(entry_r.get() or 0)
        python = int(entry_python.get() or 0)

        total = c + cpp + csharp + java + javascript + php + ruby + r + python

        if total > 0:
            # Calcula as porcentagens e atualiza as barras
            porcentagens = [
                (c / total) * 100,
                (cpp / total) * 100,
                (csharp / total) * 100,
                (java / total) * 100,
                (javascript / total) * 100,
                (php / total) * 100,
                (ruby / total) * 100,
                (r / total) * 100,
                (python / total) * 100,
            ]

            for i, barra in enumerate(barras):
                barra["value"] = porcentagens[i]

            # Atualiza o texto com o total e porcentagens
            label_resultado["text"] = f"Total de pessoas pesquisadas: {total}"
            for i, porcentagem in enumerate(porcentagens):
                labels_porcentagem[i]["text"] = f"{linguagens[i]}: {porcentagem:.2f}%"
        else:
            label_resultado["text"] = "Total de pessoas pesquisadas: 0"
            for barra in barras:
                barra["value"] = 0
            for label in labels_porcentagem:
                label["text"] = "0%"
    except ValueError:
        label_resultado["text"] = "Insira valores numéricos válidos."

# Configuração da janela principal
root = tk.Tk()
root.title("Estatísticas de Linguagens de Programação")
root.geometry("520x600")
root.config(bg="#f0f8ff")

# Configuração do Canvas e Scrollbar
canvas = tk.Canvas(root, bg="#f0f8ff")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")

# Função para configurar a região de rolagem
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Vincula a scrollbar ao Canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Layout do Canvas e Scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Lista das linguagens e criação de componentes gráficos
linguagens = ["C", "C++", "C#", "Java", "Javascript", "PHP", "Ruby", "R", "Python"]
entries = []
barras = []
labels_porcentagem = []

# Título
titulo = tk.Label(scrollable_frame, text="Estatísticas de Linguagens de Programação", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#2c3e50")
titulo.pack(pady=10)

# Cria entrada e barra de progresso para cada linguagem
for linguagem in linguagens:
    # Grupo de entrada
    frame = tk.Frame(scrollable_frame, bg="#f0f8ff")
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=f"Pessoas que gostam da linguagem {linguagem}:", bg="#f0f8ff", fg="#34495e")
    label.grid(row=0, column=0, sticky="w")
    
    entry = tk.Entry(frame, width=10)
    entry.grid(row=0, column=1, padx=5)
    entry.bind("<KeyRelease>", lambda e: calcular_estatisticas())
    entries.append(entry)
    
    # Barra de progresso
    barra = ttk.Progressbar(scrollable_frame, length=400, mode="determinate")
    barra.pack(pady=5)
    barras.append(barra)
    
    # Label da porcentagem
    label_porcentagem = tk.Label(scrollable_frame, text="0%", bg="#f0f8ff", fg="#2c3e50")
    label_porcentagem.pack()
    labels_porcentagem.append(label_porcentagem)

# Mapeia as entradas para uso na função
entry_c, entry_cpp, entry_csharp, entry_java, entry_javascript, entry_php, entry_ruby, entry_r, entry_python = entries

# Exibe o total
label_resultado = tk.Label(scrollable_frame, text="Total de pessoas pesquisadas: 0", bg="#f0f8ff", fg="#2c3e50", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

# Inicia o loop da interface
root.mainloop()
