# PDF Keyword Search and Extract

Dieses Programm durchsucht alle PDFs im Verzeichnis "input" nach einem bestimmten Stichwort und erstellt für jedes PDF, in dem das Stichwort gefunden wird, eine neue PDF-Datei im Verzeichnis "output", die nur die Seiten enthält, auf denen das Stichwort vorkommt.

## Installation

### Python 3.12 installieren

1. Gehe zur [offiziellen Python-Website](https://www.python.org/downloads/).
2. Lade den Installer für Python 3.12 für Windows herunter.
3. Führe den Installer aus und stelle sicher, dass die Option "Add Python to PATH" aktiviert ist.
4. Klicke auf "Install Now" und folge den Anweisungen zur Installation.

### Virtuelle Umgebung erstellen

1. Öffne eine Eingabeaufforderung (cmd) oder PowerShell.
2. Navigiere zu dem Verzeichnis, in dem du das Projekt speichern möchtest:
    ```sh
    cd \Pfad\zum\Projektverzeichnis
    ```
3. Erstelle eine virtuelle Umgebung:
    ```sh
    python -m venv venv
    ```
4. Aktiviere die virtuelle Umgebung:
    - Für cmd:
        ```sh
        venv\Scripts\activate
        ```
    - Für PowerShell:
        ```sh
        .\venv\Scripts\Activate.ps1
        ```

### Abhängigkeiten installieren

1. Installiere die Abhängigkeiten:
    ```sh
    pip install -r requirements.txt
    ```

## Verwendung

1. Stelle sicher, dass sich die PDF-Dateien, die durchsucht werden sollen, im Verzeichnis `input` befinden. Erstelle dieses Verzeichnis, falls es noch nicht existiert.
2. Erstelle ein Verzeichnis `output`, falls es noch nicht existiert.
3. Führe das Python-Skript aus:
    ```sh
    python search_and_extract_pdf.py
    ```
4. Gib das Stichwort ein, nach dem gesucht werden soll. Das Programm durchsucht alle PDFs im Verzeichnis `input` nach dem Stichwort.
5. Das Programm listet alle Dokumente auf, in denen das Stichwort gefunden wurde, sowie die Seiten, auf denen es vorkommt.
6. Für jedes gefundene Dokument wird eine neue PDF-Datei im Verzeichnis `output` erstellt, die nur die relevanten Seiten enthält.
