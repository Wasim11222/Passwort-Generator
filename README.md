🔐 Passwort Generator Projekt
Dieses Projekt ist ein Passwort-Generator mit einer grafischen Benutzeroberfläche (GUI), die mit Python's tkinter-Modul erstellt wurde. Es ermöglicht den Benutzern, sichere, zufällige Passwörter zu generieren, und enthält Funktionen wie das Wechseln zwischen Dark- und Light-Modus, das Kopieren des Passworts in die Zwischenablage und die Wahl der Passwortlänge.

🚀 Funktionen:
Passwort Generierung: Erzeuge ein zufälliges Passwort mit Kleinbuchstaben, Großbuchstaben, Zahlen und Sonderzeichen. 🔑

Zwischenablage Kopieren: Das generierte Passwort kann mit einem Klick in die Zwischenablage kopiert werden. 📋

Dark/Light Mode Toggle: Wechsle zwischen Dark und Light Modus für die App-Darstellung. 🌙☀️

Passwortlänge Anpassen: Wähle die gewünschte Länge des generierten Passworts. 🧮

🛠️ Anforderungen:
Python 3.x

tkinter (meistens in Python-Installationen enthalten)

pyperclip (für Zwischenablage-Funktionalität)

📖 Wie man es benutzt:
Passwortlänge Einstellen: Gib die gewünschte Passwortlänge in das Eingabefeld ein. 🧮

Passwort Generieren: Klicke auf den Button "Passwort generieren" und erhalte dein sicheres Passwort. 🔑

Passwort Kopieren: Klicke auf "Passwort kopieren", um das Passwort in die Zwischenablage zu speichern. 📋

Thema Wechseln: Klicke auf "Thema wechseln", um zwischen Dark und Light Mode zu wechseln. 🌙➡️🌞

📜 Beispiel für die Nutzung:
python
Kopieren
Bearbeiten
# Tkinter GUI-Instanz erstellen
root = tk.Tk()

# Fenster-Eigenschaften konfigurieren
root.title("Passwort Generator")
root.geometry("400x400")

# Tkinter Hauptloop starten
root.mainloop()
Dieser Code setzt das Hauptfenster der Anwendung auf und lässt es laufen, bis der Benutzer es schließt.

📦 Installation:
Stelle sicher, dass Python 3.x auf deinem System installiert ist.

Installiere pyperclip über pip, falls es noch nicht installiert ist:

bash
Kopieren
Bearbeiten
pip install pyperclip
Führe das Skript aus und benutze den Passwort-Generator.

📄 Lizenz:
Dieses Projekt ist Open-Source und steht unter der MIT-Lizenz. Du kannst es gerne nach Belieben verwenden und anpassen.
