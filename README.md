
# Passwort-Generator

## 📜 Projektbeschreibung

Der **Passwort-Generator** ist ein einfaches und leistungsstarkes Tool, das sicherere Passwörter für Benutzer erstellt. Das Programm generiert zufällige Passwörter mit einer festgelegten Länge und enthält zufällig Großbuchstaben, Zahlen und Sonderzeichen. Diese Passwörter sind ideal für den sicheren Schutz von Accounts und Daten. Das Tool verwendet eine benutzerfreundliche GUI (Graphical User Interface) mit Tkinter, die es ermöglicht, Passwörter mit nur wenigen Klicks zu erstellen und sofort zu kopieren.

## 🔑 Warum dieses Projekt wichtig ist

In der heutigen digitalen Welt ist es entscheidend, sichere Passwörter zu verwenden, um Online-Accounts und Daten zu schützen. Schwache Passwörter (z. B. "123456" oder "password") sind anfällig für Brute-Force-Angriffe und können schnell von Angreifern geknackt werden. Ein sicheres Passwort sollte daher:

- Mindestens 12 Zeichen lang sein.
- Eine Mischung aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten.

Der Passwort-Generator automatisiert diesen Prozess und bietet eine schnelle, benutzerfreundliche Möglichkeit, starke und sichere Passwörter zu erstellen.

## 🛠️ Was du benötigst

Um das Passwort-Generator-Programm auszuführen, musst du die folgenden Voraussetzungen erfüllen:

### Anforderungen:
- **Python 3.x**: Du benötigst eine funktionierende Installation von Python 3, um das Programm auszuführen.
- **pyperclip**: Eine Python-Bibliothek, die verwendet wird, um das generierte Passwort in die Zwischenablage zu kopieren.
  
  Um `pyperclip` zu installieren, öffne dein Terminal oder deine Kommandozeile und führe den folgenden Befehl aus:
  
  ```bash
  pip install pyperclip
  ```

## 🖥️ Wie funktioniert es?

### 1. **Passwortlänge angeben:**
   Der Benutzer gibt die gewünschte Länge des Passworts in das Textfeld ein. Es wird empfohlen, Passwörter mit einer Länge von mindestens 12 Zeichen zu verwenden.

### 2. **Automatische Passwortgenerierung:**
   Sobald der Benutzer auf die Schaltfläche "Passwort generieren" klickt, trifft das Programm automatisch Entscheidungen darüber, ob Zahlen, Sonderzeichen oder Großbuchstaben in das Passwort aufgenommen werden. Die Auswahl erfolgt zufällig.

### 3. **Passwort anzeigen:**
   Das generierte Passwort wird in einem Eingabefeld angezeigt, sodass der Benutzer es direkt sehen kann.

### 4. **Passwort kopieren:**
   Der Benutzer kann das generierte Passwort per Klick auf die Schaltfläche "Passwort kopieren" direkt in die Zwischenablage kopieren. So kann es sofort an anderer Stelle eingefügt werden, z. B. in ein Passwortfeld bei der Anmeldung.

### 5. **Thema wechseln:**
   Der Benutzer kann zwischen einem "Dark Mode" und einem "Light Mode" wechseln, um das Aussehen der Benutzeroberfläche zu ändern und die Verwendung komfortabler zu gestalten.

## ⚙️ Installation und Ausführung

1. **Installiere Python:**
   Wenn du Python noch nicht installiert hast, kannst du es von der offiziellen Website [python.org](https://www.python.org/downloads/) herunterladen und installieren.

2. **Installiere pyperclip:**
   Stelle sicher, dass `pyperclip` installiert ist, indem du folgenden Befehl in deinem Terminal oder der Kommandozeile ausführst:

   ```bash
   pip install pyperclip
   ```

3. **Führe das Programm aus:**
   Lade den Code herunter und speichere ihn als Python-Datei (z. B. `password_generator.py`). Um das Programm zu starten, öffne dein Terminal oder die Kommandozeile, navigiere zum Ordner, in dem sich die Datei befindet, und führe folgenden Befehl aus:

   ```bash
   python password_generator.py
   ```

4. **Benutze das Programm:**
   - Gib die gewünschte Passwortlänge ein.
   - Klicke auf "Passwort generieren".
   - Das generierte Passwort wird angezeigt.
   - Klicke auf "Passwort kopieren", um es in die Zwischenablage zu kopieren.

## 💡 Wie kann es helfen?

- **Sicherere Passwörter:** Das Programm hilft Benutzern, starke und zufällige Passwörter zu erstellen, die schwer zu erraten oder zu knacken sind.
- **Zeitsparend:** Es spart Zeit, da das Programm Passwörter automatisch generiert, ohne dass der Benutzer sich selbst komplexe Kombinationen ausdenken muss.
- **Benutzerfreundlich:** Mit einer einfachen Benutzeroberfläche und der Möglichkeit, das Passwort sofort zu kopieren, ist das Tool sehr benutzerfreundlich.

## 🔧 Beitrag leisten

Wenn du zum Projekt beitragen möchtest, kannst du Forks erstellen, Bugs melden oder Verbesserungen vorschlagen. Erstelle ein Issue oder einen Pull Request auf GitHub, und wir schauen uns deinen Beitrag an!

## 📝 Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).
