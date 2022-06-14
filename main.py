import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from googletrans import Translator

def translate_file():
    text = txt_edit.get("1.0", tk.END)
    translate_text = translator.translate(text, dest='pt')
    txt_edit.delete("1.0", tk.END)
    txt_edit.insert(tk.END, translate_text.text)

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", ".txt"), ("All Files", ".*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", ".txt"), ("All Files", ".*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


translator = Translator()
window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Abrir", command=open_file)
btn_traslate = tk.Button(frm_buttons, text="Traduzir", command=translate_file)
btn_save = tk.Button(frm_buttons, text="Salvar", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_traslate.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()