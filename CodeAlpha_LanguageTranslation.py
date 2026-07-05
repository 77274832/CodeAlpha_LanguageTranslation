from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.config(bg="#f0f8ff")

# Language Dictionary
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# Title
Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="#f0f8ff",
    fg="blue"
).pack(pady=10)

# Input Text
Label(root, text="Enter Text:", font=("Arial", 12), bg="#f0f8ff").pack()

input_text = Text(root, height=6, width=60, font=("Arial", 12))
input_text.pack(pady=5)

# Source Language
Label(root, text="From Language:", bg="#f0f8ff").pack()

source_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
source_lang.pack()
source_lang.set("English")

# Target Language
Label(root, text="To Language:", bg="#f0f8ff").pack()

target_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
target_lang.pack()
target_lang.set("Tamil")

# Translate Function
def translate_text():
    text = input_text.get("1.0", END).strip()

    if text == "":
        messagebox.showerror("Error", "Please enter text.")
        return

    try:
        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

        # Output Label
Label(root, text="Translated Text:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)

# Output Text Box
output_text = Text(root, height=6, width=60, font=("Arial", 12))
output_text.pack(pady=5)

# Copy Function
def copy_text():
    text = output_text.get("1.0", END).strip()

    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Translated text copied!")

def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

# Translate Button
Button(
    root,
    text="Translate",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=translate_text
).pack(pady=10)

# Copy Button
Button(
    root,
    text="Copy",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=copy_text
).pack()
Button(
    root,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=clear_text
).pack(pady=5)
# Start the Application
Label(
    root,
    text="Developed by Shree Mathi",
    font=("Arial", 10, "italic"),
    bg="#f0f8ff",
    fg="gray"
).pack(side="bottom", pady=10)
root.mainloop()

