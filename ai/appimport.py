import pandas as pd
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

# tema pro system
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

def process_pptx():
    csv_file = csv_path.get()
    
    if not csv_file:
        messagebox.showerror("Erro", "selecione um arquivo")
        return

    try:
        # Carregar os dados do CSV
        data = pd.read_csv(csv_file, dtype=str)
        data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")
        data = data.map(lambda x: str(x).strip() if pd.notna(x) else "")

        messagebox.showinfo("Sucesso", f"os arquivos estão em: {output_folder}")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")

def select_csv():
    file = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
    if file:
        csv_path.set(file)

# parte do custom tkinter
root = ctk.CTk()
root.title("Analisador de Dados abcde")
root.geometry("600x250")

csv_path = ctk.StringVar()

title_label = ctk.CTkLabel(root, text="Analisador de Dados abcde", font=("Arial", 20))
title_label.pack(pady=15)

csv_frame = ctk.CTkFrame(root)
csv_frame.pack(pady=10, padx=20, fill="x")

csv_label = ctk.CTkLabel(csv_frame, text="CSV:")
csv_label.pack(side="left", padx=10)

csv_entry = ctk.CTkEntry(csv_frame, textvariable=csv_path, width=350, state="readonly")
csv_entry.pack(side="left", padx=10)

csv_button = ctk.CTkButton(csv_frame, text="Selecionar", command=select_csv)
csv_button.pack(side="right", padx=10)

pptx_frame = ctk.CTkFrame(root)
pptx_frame.pack(pady=10, padx=20, fill="x")

process_button = ctk.CTkButton(root, text="Gerar analise", command=process_pptx, fg_color="green")
process_button.pack(pady=20)

#loop padrão do tkinter
root.mainloop()