import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

# Passwortgenerierung basierend auf zufälligen Entscheidungen
def generate_password(length):
    # Entscheidungslogik für die Passwortmerkmale
    use_numbers = random.choice([True, False])
    use_special_chars = random.choice([True, False])
    use_uppercase = random.choice([True, False])

    # Basiszeichen: Kleinbuchstaben
    characters = string.ascii_lowercase

    if use_numbers:
        characters += string.digits  # Zahlen hinzufügen
    if use_special_chars:
        characters += string.punctuation  # Sonderzeichen hinzufügen
    if use_uppercase:
        characters += string.ascii_uppercase  # Großbuchstaben hinzufügen

    # Passwort generieren
    return ''.join(random.choice(characters) for i in range(length))

# Funktion zum Kopieren des Passworts in die Zwischenablage
def copy_to_clipboard(password):
    pyperclip.copy(password)

# Themen (Dark Mode und Light Mode)
dark_theme = {
    "background": "#2e2e2e",
    "foreground": "#ffffff",
    "button_bg": "#555555",
    "button_fg": "#ffffff"
}

light_theme = {
    "background": "#f0f0f0",
    "foreground": "#000000",
    "button_bg": "#d3d3d3",
    "button_fg": "#000000"
}

# Standardthema: Dark Mode
current_theme = dark_theme

# Wechsel des Themes
def toggle_theme():
    global current_theme
    if current_theme == dark_theme:
        current_theme = light_theme
    else:
        current_theme = dark_theme
    apply_theme()

# Anwendung des aktuellen Themes
def apply_theme():
    root.config(bg=current_theme["background"])
    password_entry.config(bg=current_theme["background"], fg=current_theme["foreground"])
    password_label.config(bg=current_theme["background"], fg=current_theme["foreground"])
    generate_button.config(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    copy_button.config(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    theme_button.config(bg=current_theme["button_bg"], fg=current_theme["button_fg"])

# Funktion zum Starten des Passwortgenerators
def generate_password_button():
    try:
        length = int(password_length_entry.get())  # Passwortlänge abfragen
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gib eine gültige Länge ein!")
        return

    # Passwort generieren
    password = generate_password(length)
    
    # Generiertes Passwort im Eingabefeld anzeigen
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Funktion zum Kopieren des generierten Passworts
def copy_password():
    password = password_entry.get()
    if password:
        copy_to_clipboard(password)
        messagebox.showinfo("Erfolg", "Passwort wurde in die Zwischenablage kopiert!")
    else:
        messagebox.showwarning("Warnung", "Kein Passwort zum Kopieren!")

# Erstellen der GUI
root = tk.Tk()
root.title("Passwort Generator")
root.geometry("400x400")

# Eingabefeld für die Passwortlänge
password_label = tk.Label(root, text="Länge des Passworts:", bg=current_theme["background"], fg=current_theme["foreground"])
password_label.pack(pady=10)

password_length_entry = tk.Entry(root)
password_length_entry.pack(pady=5)

# Button zum Generieren des Passworts
generate_button = tk.Button(root, text="Passwort generieren", command=generate_password_button)
generate_button.pack(pady=20)

# Feld zum Anzeigen des generierten Passworts
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

# Button zum Kopieren des Passworts
copy_button = tk.Button(root, text="Passwort kopieren", command=copy_password)
copy_button.pack(pady=10)

# Button zum Wechseln des Themes
theme_button = tk.Button(root, text="Thema wechseln", command=toggle_theme)
theme_button.pack(pady=10)

# Standardthema anwenden
apply_theme()

# Tkinter Hauptloop starten
root.mainloop()
