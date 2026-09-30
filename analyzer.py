
def calculate_basic_stats(sessions):
    if not sessions:
        return {
            "total_duration": 0,
            "average_focus": 0,
            "average_distractions": 0
        }

    total_duration = 0
    total_focus = 0
    total_distractions = 0

    for session in sessions:
        total_duration += int(session["duration"])
        total_focus += int(session["focus_rating"])
        total_distractions += int(session["distractions"])

    average_focus = total_focus / len(sessions)
    average_distractions = total_distractions / len(sessions)

    return {
        "total_duration": total_duration,
        "average_focus": round(average_focus, 2),
        "average_distractions": round(average_distractions, 2)
    }


def find_best_subject(sessions):
    if not sessions:
        return "No data"

    subject_data = {}

    for session in sessions:
        subject = session["subject"]
        focus = int(session["focus_rating"])

        if subject not in subject_data:
            subject_data[subject] = []

        subject_data[subject].append(focus)

    best_subject = ""
    best_average = -1

    for subject, focus_values in subject_data.items():
        average = sum(focus_values) / len(focus_values)

        if average > best_average:
            best_average = average
            best_subject = subject

    return best_subject


def find_best_period(sessions):
    if not sessions:
        return "No data"

    period_data = {}

    for session in sessions:
        period = session["period"]
        focus = int(session["focus_rating"])

        if period not in period_data:
            period_data[period] = []

        period_data[period].append(focus)

    best_period = ""
    best_average = -1

    for period, focus_values in period_data.items():
        average = sum(focus_values) / len(focus_values)

        if average > best_average:
            best_average = average
            best_period = period

    return best_period


def find_most_distracting_subject(sessions):
    if not sessions:
        return "No data"

    subject_data = {}

    for session in sessions:
        subject = session["subject"]
        distractions = int(session["distractions"])

        if subject not in subject_data:
            subject_data[subject] = []

        subject_data[subject].append(distractions)

    most_distracting = ""
    highest_average = -1

    for subject, distraction_values in subject_data.items():
        average = sum(distraction_values) / len(distraction_values)

        if average > highest_average:
            highest_average = average
            most_distracting = subject

    return most_distracting


def find_best_session_length(sessions):
    if not sessions:
        return "No data"

    best_session = sessions[0]

    for session in sessions:
        current_focus = int(session["focus_rating"])
        best_focus = int(best_session["focus_rating"])

        if current_focus > best_focus:
            best_session = session

    return f"{best_session['duration']} minutes"


def calculate_consistency(sessions):
    if not sessions:
        return 0

    unique_dates = set()

    for session in sessions:
        unique_dates.add(session["date"])

    consistency = (len(unique_dates) / len(sessions)) * 100

    return round(consistency, 2)
