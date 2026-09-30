from session_manager import add_study_session
from data_handler import load_sessions
from fingerprint import generate_fingerprint
from report_generator import generate_report
from analyzer import (
    calculate_basic_stats,
    find_best_subject,
    find_best_period,
    find_most_distracting_subject,
    find_best_session_length,
    calculate_consistency
)


def main():
    print("========================================")
    print("          FOCUSFINGERPRINT")
    print("========================================")
    print("Personal Study Pattern Analyzer")
    print()
    print("1. Add Study Session")
    print("2. View Study Sessions")
    print("3. Analyze Focus")
    print("4. Generate FocusFingerprint")
    print("5. Generate Report")
    print("6. Exit")
    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        session = add_study_session()
        print("\nSession captured successfully!")
        print(session)

    elif choice == "2":
        sessions = load_sessions()

        if not sessions:
            print("\nNo study sessions found.")
        else:
            print("\n--- Study Sessions ---")

            for session in sessions:
                print(
                    f"Date: {session['date']} | "
                    f"Subject: {session['subject']} | "
                    f"Duration: {session['duration']} min | "
                    f"Distractions: {session['distractions']} | "
                    f"Focus: {session['focus_rating']}/5 | "
                    f"Period: {session['period']}"
                )

    elif choice == "3":
        sessions = load_sessions()

        if not sessions:
            print("\nNo study sessions available for analysis.")
        else:
            stats = calculate_basic_stats(sessions)
            best_subject = find_best_subject(sessions)
            best_period = find_best_period(sessions)
            distracting_subject = find_most_distracting_subject(sessions)
            best_session_length = find_best_session_length(sessions)
            consistency = calculate_consistency(sessions)

            print("\n--- Focus Analysis ---")
            print(f"Total study time: {stats['total_duration']} minutes")
            print(f"Average focus: {stats['average_focus']}/5")
            print(f"Average distractions: {stats['average_distractions']}")
            print(f"Best subject for focus: {best_subject}")
            print(f"Best study period: {best_period}")
            print(f"Most distracting subject: {distracting_subject}")
            print(f"Best session length: {best_session_length}")
            print(f"Study consistency: {consistency}%")

    elif choice == "4":
        sessions = load_sessions()

        if not sessions:
            print("\nNo study sessions available.")
        else:
            fingerprint = generate_fingerprint(sessions)
            print(fingerprint)

    elif choice == "5":
        sessions = load_sessions()

        if not sessions:
            print("\nNo study sessions available for report.")
        else:
            report = generate_report(sessions)

            print("\nReport generated successfully!")
            print("Report saved at: reports/focus_report.txt")
            print()
            print(report)

    elif choice == "6":
        print("Thank you for using FocusFingerprint!")

    else:
        print("\nInvalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()