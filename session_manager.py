from data_handler import save_session


def add_study_session():
    print("\n--- Add Study Session ---")

    date = input("Enter date (DD-MM-YYYY): ").strip()
    subject = input("Enter subject: ").strip()

    while True:
        try:
            duration = int(input("Enter study duration in minutes: "))

            if duration > 0:
                break
            else:
                print("Duration must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            distractions = int(input("Enter number of distractions: "))

            if distractions >= 0:
                break
            else:
                print("Distractions cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            focus_rating = int(input("Enter focus rating (1-5): "))

            if 1 <= focus_rating <= 5:
                break
            else:
                print("Focus rating must be between 1 and 5.")

        except ValueError:
            print("Please enter a number from 1 to 5.")

    period = input(
        "Enter study period (Morning/Afternoon/Evening/Night): "
    ).strip().title()

    session = {
        "date": date,
        "subject": subject,
        "duration": duration,
        "distractions": distractions,
        "focus_rating": focus_rating,
        "period": period
    }

    save_session(session)

    return session
