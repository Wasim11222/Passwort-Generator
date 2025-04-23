# 🔐 Passwort-Generator (Tkinter GUI)

![Screenshot der Anwendung](screenshot.png) *(Beispielbild einfügen)*

## 📜 Projektbeschreibung
Ein Python-basierter Passwort-Generator mit grafischer Oberfläche (GUI), der sichere, zufällige Passwörter erstellt. Die Anwendung bietet:

✅ Zufällige Passwortgenerierung mit anpassbarer Länge  
✅ Optionale Integration von Zahlen, Sonderzeichen und Großbuchstaben  
✅ Ein-Klick-Kopierfunktion in die Zwischenablage  
✅ Dark/Light Mode Umschaltung  
✅ Benutzerfreundliche Fehlerbehandlung  

---

## 🛠️ Technische Implementierung

### 📂 Code-Struktur
```python
import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox
🔧 Kernfunktionen
Passwortgenerierung (generate_password())

Nutzt random.choice für zufällige Merkmale:

python
use_numbers = random.choice([True, False])
use_special_chars = random.choice([True, False])
Kombiniert Zeichensätze dynamisch:

python
characters = string.ascii_lowercase
if use_numbers:
    characters += string.digits
GUI-Komponenten (Tkinter)

Eingabefeld für Passwortlänge

Anzeigefeld für generiertes Passwort

Aktionbuttons:

python
generate_button = tk.Button(root, text="Passwort generieren", command=generate_password_button)
Theme-System

Dark/Light Mode Umschaltung:

python
dark_theme = {
    "background": "#2e2e2e",
    "foreground": "#ffffff"
}
🖥️ Bedienungsanleitung
🚀 Start der Anwendung
bash
python password_generator.py
🔄 Nutzungsablauf
Passwortlänge eingeben

Zahl im Eingabefeld eintragen (z.B. 12)

Passwort generieren

Klick auf "Passwort generieren"

Passwort kopieren

Klick auf "Passwort kopieren" → Passwort landet in Zwischenablage

Design anpassen

"Thema wechseln" Button toggelt zwischen Dark/Light Mode

📦 Abhängigkeiten
Paket	Version	Beschreibung
Python	3.6+	Laufzeitumgebung
Tkinter	-	GUI-Bibliothek (Python-Standard)
pyperclip	1.8+	Zwischenablagen-Zugriff
Installation:

bash
pip install pyperclip
🛡️ Sicherheitsmerkmale
🔒 Passwortstärke
Dynamische Zeichenauswahl:

python
# 50% Chance für jede Erweiterung
use_special_chars = random.choice([True, False])
Mindestanforderungen:

Kleinbuchstaben (immer enthalten)

Optionale Komplexität durch:

Großbuchstaben (string.ascii_uppercase)

Zahlen (string.digits)

Sonderzeichen (string.punctuation)

🚫 Fehlerbehandlung
Prüfung auf gültige Längeneingabe:

python
try:
    length = int(password_length_entry.get())
except ValueError:
    messagebox.showerror("Fehler", "Bitte gib eine gültige Länge ein!")
🎨 UI-Design
🖌️ Theme-System
Element	Dark Mode	Light Mode
Hintergrund	#2e2e2e (Dunkel)	#f0f0f0 (Hell)
Text	Weiß	Schwarz
Buttons	Grau (#555555)	Hellgrau (#d3d3d3)
Umschaltlogik:

python
def toggle_theme():
    global current_theme
    current_theme = light_theme if current_theme == dark_theme else dark_theme
💡 Erweiterungsideen
Passwortstärke-Anzeige

Farbcodierung (Rot/Gelb/Grün) basierend auf Komplexität

Profil-System

Voreinstellungen für verschiedene Dienste (z.B. "Bank", "Email")

Passwort-History

Letzte generierte Passwörter speichern (lokal verschlüsselt)

⚠️ Hinweise
Nutzt systemeigene Zwischenablage (pyperclip)

Für maximale Sicherheit Passwörter nicht unverschlüsselt speichern

Empfohlene Mindestlänge: 12 Zeichen
