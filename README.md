# 🔐 Passwort-Generator

![Passwort-Generator Screenshot](screenshot.png) *(Optional: Bild einfügen)*  

## 📜 Projektbeschreibung  
Der Passwort-Generator ist ein einfaches und leistungsstarkes Tool, das sichere Passwörter für Benutzer erstellt. Das Programm generiert zufällige Passwörter mit einer festgelegten Länge und enthält eine Kombination aus Groß-/Kleinbuchstaben, Zahlen und Sonderzeichen. Diese Passwörter bieten optimalen Schutz für Accounts und sensible Daten.  

Das Tool bietet:  
✅ **Benutzerfreundliche GUI** (mit Tkinter)  
✅ **Sofortiges Kopieren** (via pyperclip)  
✅ **Anpassbare Passwortlänge**  
✅ **Dark/Light Mode**  

---

## 🔑 Warum dieses Projekt wichtig ist  
In der digitalen Welt sind schwache Passwörter (wie "123456" oder "password") ein großes Sicherheitsrisiko. Der Passwort-Generator löst dieses Problem durch:  

🔒 **Sichere Passwörter** nach aktuellen Standards:  
- Mindestens **12 Zeichen** (empfohlen)  
- Mix aus **Groß-/Kleinbuchstaben**, **Zahlen** und **Sonderzeichen**  
- **Zufällige Generierung** – keine vorhersehbaren Muster  

🛡️ **Schützt vor:**  
- Brute-Force-Angriffen  
- Datenlecks durch schwache Passwörter  

---

## 🛠️ Technische Voraussetzungen  

### 📋 Anforderungen:
| Komponente      | Version    | Beschreibung                     |
|----------------|-----------|----------------------------------|
| **Python**     | 3.6+      | Laufzeitumgebung                 |
| **pyperclip**  | 1.8+      | Zum Kopieren der Passwörter      |
| **Tkinter**    | (included)| Für die GUI (standardmäßig in Python enthalten) |

### 📦 Installation:
1. Python installieren: [python.org/downloads](https://www.python.org/downloads/)  
2. pyperclip installieren (Terminal/CMD):  
   ```bash
   pip install pyperclip
🖥️ Bedienungsanleitung
🔄 Schritt-für-Schritt:
Passwortlänge festlegen

Gib im Eingabefeld die gewünschte Länge ein (z. B. 12).

Passwort generieren

Klicke auf „Passwort generieren“ – das System erstellt automatisch ein sicheres Passwort.

Passwort kopieren

Klicke auf „Passwort kopieren“ – es wird direkt in deine Zwischenablage übernommen.

Design anpassen (optional)

Wechsle zwischen Dark Mode 🌙 und Light Mode ☀️ über den Theme-Button.

⚙️ Installation & Ausführung
🚀 Schnellstart:
bash
# 1. Repository klonen
git clone https://github.com/dein-username/passwort-generator.git

# 2. Ins Verzeichnis wechseln
cd passwort-generator

# 3. Programm starten
python password_generator.py
📁 Alternative (manuell):
Lade die password_generator.py-Datei herunter.

Führe sie mit Python aus:

bash
python3 password_generator.py
💡 Nutzen des Tools
Funktion	Vorteil
Sichere Passwörter	Reduziert Hacking-Risiko
Zeitersparnis	Kein manuelles Erstellen nötig
Einfache Bedienung	Intuitive Oberfläche – keine Vorkenntnisse erforderlich
🛠️ Erweiterungsmöglichkeiten
Du kannst das Projekt erweitern um:

📊 Passwort-Stärke-Analyse

🔄 Passwort-History (letzte Generierungen)

🌐 Browser-Integration (als Plug-in)

