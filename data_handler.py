import csv
import os

FILE_PATH = "data/study_sessions.csv"


def save_session(session):
    file_exists = os.path.exists(FILE_PATH)

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "date",
                "subject",
                "duration",
                "distractions",
                "focus_rating",
                "period"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(session)
        
def load_sessions():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)
        sessions = list(reader)

    return sessions