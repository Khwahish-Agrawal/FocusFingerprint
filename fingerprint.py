from analyzer import (
    find_best_subject,
    find_best_period,
    find_most_distracting_subject,
    find_best_session_length
)


def generate_fingerprint(sessions):
    if not sessions:
        return "No study data available."

    best_subject = find_best_subject(sessions)
    best_period = find_best_period(sessions)
    most_distracting_subject = find_most_distracting_subject(sessions)
    best_session_length = find_best_session_length(sessions)

    total_focus = 0

    for session in sessions:
        total_focus += int(session["focus_rating"])

    average_focus = total_focus / len(sessions)

    fingerprint = f"""
========================================
        YOUR FOCUSFINGERPRINT
========================================

Strongest Subject       : {best_subject}
Best Study Period       : {best_period}
Best Session Length     : {best_session_length}
Main Distraction Area   : {most_distracting_subject}
Average Focus           : {average_focus:.2f}/5

----------------------------------------
Your study pattern shows that your
focus varies according to subject,
study period and session length.
========================================
"""

    return fingerprint