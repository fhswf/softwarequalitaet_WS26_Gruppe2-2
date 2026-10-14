#RTRE
#JYBS

"""
=======================
Aufgabe 1:
=======================
Welche Funktionen erfüllt der Code?

- Verwaltung einer Aufgabenliste (To-Do-Liste)
- Aufgaben hinzufügen (add_task)
- Aufgaben löschen (remove_task)
- Aufgaben als erledigt markieren (mark_done)
- Aufgaben anzeigen (show_tasks)
- Durchschnitt der Aufgabenlänge berechnen (calculate_task_average)
- Kommende Aufgaben ermitteln (upcoming_tasks)
- Erledigte Aufgaben entfernen (cleanup)
- Anzahl der vorhandenen Aufgaben zählen (get_task_count)
- Argumente der Aufgabe: Name, Fälligkeitsdatum, Priorität, ID

Auffälligkeiten, die das Verständnis des Codes erschweren:

- Aufgaben werden als Liste gespeichert, sodass die Bedeutung der einzelnen
  Indizes (z.B. task[0], task[1], task[2]) nicht direkt erkennbar ist.
- Es fehlen Kommentare.
- Vorhanden Kommentare (TODO, Wichtig) sind nicht weiter erläutert.
- Der Aufbau eines Tasks ist nicht dokumentiert.
- Die Vergabe der task_id ist nicht eindeutig (länge String+ Zufallszahl)-->kann zwei mal gleich sein. 
- backup_tasks wird befüllt, später jedoch nicht mehr verwendet.
- Mehrere Funktionen prüfen nicht, ob tasks den Wert None besitzt.
- Die Datumswerte werden als Strings gespeichert, wodurch Vergleiche nicht sauber funktionieren.
- Zuordnung der Tasks nicht einheitlich. mark_done arbeitet mit dem task namen. Dieser kann mehrfach auftauchen. 

=======================
Aufgabe 2:
=======================

Softwarequalität positiv:
-Funktionen einzeln ausgelagert
-Nachvollziehbare Funktionsnamen

Softwarequalität negativ:
-Datenstruktur Liste (Zugriff per Indizes)
-Keine Dokumentation der Funktionen
-Abfangen unsinniger Eingaben (Fehleranfällig)
-Fehler in Datenvergleich (Weil falscher Datentyp)


======================
Aufgabe 4 (optional)
======================

************* Module Uebung2_Team2
Uebung2/Uebung2_Team2.py:28:0: C0301: Line too long (102/100) (line-too-long)
Uebung2/Uebung2_Team2.py:32:0: C0301: Line too long (112/100) (line-too-long)
Uebung2/Uebung2_Team2.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
Uebung2/Uebung2_Team2.py:99:0: C0301: Line too long (103/100) (line-too-long)
Uebung2/Uebung2_Team2.py:1:0: C0103: Module name "Uebung2_Team2" doesn't conform to snake_case naming style (invalid-name)
Uebung2/Uebung2_Team2.py:54:0: C0103: Constant name "tasks" doesn't conform to UPPER_CASE naming style (invalid-name)
Uebung2/Uebung2_Team2.py:61:4: W0602: Using global for 'backup_tasks' but no assignment is done (global-variable-not-assigned)
Uebung2/Uebung2_Team2.py:87:8: W0612: Unused variable 'task_id' (unused-variable)

-----------------------------------
Your code has been rated at 8.75/10

"""

import datetime
import random

#Speichert alle Aufgaben
tasks = None
#Speichert eine Kopie der Aufgaben
backup_tasks = {}


def add_task(name, due_date, priority=3, task_id=None):
    """Erstellt eine neue Aufgabe und fügt sie der Aufgabenliste hinzu"""
    global tasks, backup_tasks
    
    if tasks is None:
        tasks = {}

    if task_id is None:
        # Wichtig! Nicht verändern!
        task_id = len(tasks) + random.randint(2, 7)
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task.copy()
    return task_id


def remove_task(task_id):
    """Entfernt eine Aufgabe aus der Liste"""
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name):
    """Aufgabe als erledigt markieren"""

    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
            return True

    return False


def show_tasks():
    """Alle Aufgaben anzeigen"""
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


def process_tasks():
    """Ändert den Status einer zufällig ausgewählten Aufgabe"""

    if not tasks:
        return False

    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]

    return True


def calculate_task_average():
    """Berechnet die durchschnittliche Priorität aller Aufgaben"""

    if not tasks:
        return 0

    priorities = [task[2] for task in tasks.values()]
    return sum(priorities) / len(priorities)


def upcoming_tasks():
    """Liefert alle zukünftigen Aufgaben sortiert zurück"""
    today = datetime.datetime.now()
    upcoming = sorted(
        [
            task for task in tasks.values()
            if datetime.datetime.strptime(task[1], "%d-%m-%Y") >= today
        ],
        key=lambda x: datetime.datetime.strptime(x[1], "%d-%m-%Y")
    )

    return upcoming


def cleanup():
    """Entfernt erledigte Aufgaben aus der Aufgabenliste"""

    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():
    """Gibt die Anzahl der vorhanden Aufgaben aus"""
    return sum(1 for _ in tasks) if tasks else 0


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
