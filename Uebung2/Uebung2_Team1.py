# TNSS
# NOVE

"""
===============================================================================
AUFGABE 1: Funktionsübersicht & schwer verständliche Stellen im Code
===============================================================================

Funktion des Codes:
Der Code stellt ein einfaches Aufgabenverwaltungssystem (To-Do-Liste) bereit:
- add_task: Erstellt neue Aufgaben mit Name, Fälligkeitsdatum, Priorität, Status,
  Ersteller ("user1") und Zeitstempel.
- remove_task: Löscht eine Aufgabe anhand ihrer ID.
- mark_done: Sucht Aufgaben nach Namen und markiert diese als erledigt.
- show_tasks: Gibt alle derzeit gespeicherten Aufgaben auf der Konsole aus.
- process_tasks: Wählt zufällig eine Aufgabe aus und schaltet deren Status um.
- calculate_task_average: Berechnet statistische Werte (z. B. durchschnittliche
  Priorität oder ID-Mittelwert) der Aufgaben.
- upcoming_tasks: Filtert und sortiert ausstehende Aufgaben nach Fälligkeit.
- cleanup: Entfernt alle erledigten Aufgaben aus der Liste.
- get_task_count: Gibt die Anzahl der aktuell verwalteten Aufgaben zurück.

Stellen, die das Verständnis des Codes erschweren:
1. Verwendung magischer Listen-Indizes:
   Tasks werden als anonyme Listen [name, due_date, priority, is_done, user, created_at]
   gespeichert. Der Zugriff über task[0], task[1], task[2], task[3] ist fehleranfällig
   und schwer nachvollziehbar.
2. Unvorhersehbare ID-Generierung:
   task_id = len(tasks) + random.randint(2, 7) erzeugt zufällige und nicht-fortlaufende
   Schlüssel, was zu Inkonsistenzen führen kann.
3. Globale Variablen & Seiteneffekte:
   Funktionen nutzen 'global tasks' und 'global backup_tasks' anstelle einer sauberen
   Kapselung (z.B. in einer Klasse) oder Übergabe als Funktionsparameter.
4. Fehlerhafte Datumsvergleiche:
   In upcoming_tasks() werden Datumsangaben im Format "DD-MM-YYYY" als normale Strings
   verglichen (z.B. "25-05-2025" >= "27-09-2026"), was logisch falsch ist.
5. Toter Code & unklare Rückgabewerte:
   mark_done() gibt immer den String "Erledigt" zurück, selbst wenn kein Task gefunden wurde.
   process_tasks() enthält ein unbehandeltes '# TODO' und gibt starr 'False' zurück.

===============================================================================
AUFGABE 2: Bewertung der Softwarequalität (Positiv / Negativ) & Verbesserungen
===============================================================================

Positiv zu bewerten:
+ Ansätze zur Modularisierung (Aufteilung in einzelne Funktionen).
+ Sprechende Funktionsnamen (z.B. add_task, remove_task, show_tasks).
+ Verwendung von Standardbibliotheken (datetime, random).

Negativ zu bewerten:
- Mangelhafte Datenstruktur: Verwendung von Listen statt Objekten/Dataclasses.
- Fehlende Robustheit & Fehlerbehandlung: Keine Typ-/Eingabeprüfung.
- Fehlende Dokumentation: Keine Kommentare vorhanden.
- Unvollständige Logik & Redundanz: backup_tasks wird befüllt, aber an keiner Stelle im Skript ausgelesen oder wiederhergestellt.
- Verletzung von Clean Code Principles: Globale Zustände, magische Werte.

===============================================================================
IDENTIFIZIERTE SCHWACHSTELLEN UND MÖGLICHE VERBESSERUNGEN:
===============================================================================
1. Initialisierung 'tasks = None': Auf 'tasks = {}' korrigieren.
2. Singleton-Vergleich 'task_id == None': Durch PEP8 'task_id is None' ersetzen.
3. Unnötige 'global'-Anweisungen: In remove_task, mark_done, show_tasks entfernen.
4. Desynchronisierte 'backup_tasks': In remove_task() den Eintrag löschen.
5. Ungenutzte 'task_id' in mark_done(): Iteration über tasks.values() umgestellen.
6. Falscher Rückgabewert in mark_done(): Gibt "Erledigt" oder "Nicht gefunden" zurück.
7. Zu lange Codezeile in show_tasks(): Formatierung auf < 100 Zeichen anpassen.
8. Toter Code in process_tasks(): '# TODO' entfernen und dynamischen Rückgabewert nutzen.
9. TypeError in calculate_task_average(): Prioritätsmittelwert berechnen.
10. Fehlerhafter String-Datumsvergleich: Konvertierung in datetime.date-Objekte.
11. Falsche Sortierung in upcoming_tasks(): Nach Fälligkeitsdatum sortieren.
12. Ineffizientes Zählen in get_task_count(): sum() durch len(tasks) ersetzen.
13. Fehlende Dokumentation: Kommentare pflegen.
===============================================================================
"""

import datetime
import random


tasks = {}
backup_tasks = {}


TASK_NAME_IDX = 0
TASK_DUE_DATE_IDX = 1
TASK_PRIORITY_IDX = 2
TASK_IS_DONE_IDX = 3
TASK_USER_IDX = 4
TASK_CREATED_AT_IDX = 5


def add_task(name, due_date, priority=3, task_id=None):

    global tasks
    if tasks is None:
        tasks = {}

    if task_id is None:
        # Wichtig! Nicht verändern!
        task_id = len(tasks) + random.randint(2, 7)

    now_str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    task = [name, due_date, priority, False, "user1", now_str]

    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id


def remove_task(task_id):

    if task_id in tasks:
        del tasks[task_id]
        if task_id in backup_tasks:
            del backup_tasks[task_id]
        return True
    return False


def mark_done(task_name):

    found = False
    for task in tasks.values():
        if task[TASK_NAME_IDX] == task_name:
            task[TASK_IS_DONE_IDX] = True
            found = True
    return "Erledigt" if found else "Nicht gefunden"


def show_tasks():

    for task_id, task in tasks.items():
        status = "Erledigt" if task[TASK_IS_DONE_IDX] else "Offen"
        print(
            f"{task_id}: {task[TASK_NAME_IDX]} ({task[TASK_PRIORITY_IDX]}) "
            f"- bis {task[TASK_DUE_DATE_IDX]} - {status}"
        )


def process_tasks():

    if not tasks:
        return False
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][TASK_IS_DONE_IDX] = not tasks[rand_id][TASK_IS_DONE_IDX]
    return True


def calculate_task_average():

    if not tasks:
        return 0.0
    total_priority = sum(task[TASK_PRIORITY_IDX] for task in tasks.values())
    return total_priority / len(tasks)


def upcoming_tasks():

    today = datetime.datetime.now().date()
    upcoming = []

    for task in tasks.values():

        if task[TASK_IS_DONE_IDX]:
            continue
        try:
            task_date = datetime.datetime.strptime(
                task[TASK_DUE_DATE_IDX], "%d-%m-%Y"
            ).date()
            if task_date >= today:
                upcoming.append((task_date, task))
        except ValueError:

            upcoming.append((today, task))

    upcoming.sort(key=lambda item: item[0])
    return [task for _, task in upcoming]


def cleanup():

    temp = {
        task_id: task
        for task_id, task in tasks.items()
        if not task[TASK_IS_DONE_IDX]
    }
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():

    return len(tasks) if tasks else 0


if __name__ == "__main__":
    add_task("Projekt abschließen", "25-05-2025", 1, task_id="hello")
    add_task("Projekt abschließen", "25-05-2025", 1)
    add_task("Einkaufen gehen", "21-05-2025", 3)
    add_task("Dokumentation schreiben", "30-05-2025", 2)

    mark_done("Einkaufen gehen")
    process_tasks()
    show_tasks()

    print("Offene Aufgaben nach Datum sortiert:", upcoming_tasks())
    cleanup()
    print("Gesamtzahl der Aufgaben:", get_task_count())
