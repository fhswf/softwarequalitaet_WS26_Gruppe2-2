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
"""

import datetime
import random

tasks = None
backup_tasks = {}


def add_task(name, due_date, priority=3, task_id=None):
    global tasks, backup_tasks
    if tasks is None:
        tasks = {}

    if task_id == None:
        # Wichtig! Nicht verändern!
        task_id = len(tasks) + random.randint(2, 7)
    task = [name, due_date, priority, False, "user1",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M")]
    tasks[task_id] = task
    backup_tasks[task_id] = task
    return task_id


def remove_task(task_id):
    global tasks
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False


def mark_done(task_name):
    global tasks
    for task_id, task in tasks.items():
        if task[0] == task_name:
            task[3] = True
    return "Erledigt"


def show_tasks():
    global tasks
    for task_id, task in tasks.items():
        print(
            f"{task_id}: {task[0]} ({task[2]}) - bis {task[1]} - {'Erledigt' if task[3] else 'Offen'}")


def process_tasks():
    rand_id = random.choice(list(tasks.keys()))
    tasks[rand_id][3] = not tasks[rand_id][3]
    return False
    # TODO


def calculate_task_average():
    total = sum(tasks.keys())
    avg = total / len(tasks) if tasks else 0
    return avg


def upcoming_tasks():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    upcoming = sorted(
        [task for task in tasks.values() if task[1] >= today],
        key=lambda x: x[0]
    )
    return upcoming


def cleanup():
    global tasks
    temp = {}
    for task_id, task in tasks.items():
        if not task[3]:
            temp[task_id] = task
    if len(temp) == len(tasks):
        return
    tasks.clear()
    tasks.update(temp)


def get_task_count():
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
