import unittest

from analyzer import (
    calculate_basic_stats,
    find_best_subject,
    find_best_period,
    find_most_distracting_subject,
    find_best_session_length,
    calculate_consistency
)


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sessions = [
            {
                "date": "25-09-2026",
                "subject": "Python",
                "duration": "90",
                "distractions": "3",
                "focus_rating": "4",
                "period": "Morning"
            },
            {
                "date": "26-09-2026",
                "subject": "DBMS",
                "duration": "60",
                "distractions": "2",
                "focus_rating": "5",
                "period": "Evening"
            }
        ]

    def test_basic_stats(self):
        result = calculate_basic_stats(self.sessions)

        self.assertEqual(result["total_duration"], 150)
        self.assertEqual(result["average_focus"], 4.5)
        self.assertEqual(result["average_distractions"], 2.5)

    def test_best_subject(self):
        result = find_best_subject(self.sessions)

        self.assertEqual(result, "DBMS")

    def test_best_period(self):
        result = find_best_period(self.sessions)

        self.assertEqual(result, "Evening")

    def test_most_distracting_subject(self):
        result = find_most_distracting_subject(self.sessions)

        self.assertEqual(result, "Python")

    def test_best_session_length(self):
        result = find_best_session_length(self.sessions)

        self.assertEqual(result, "60 minutes")

    def test_consistency(self):
        result = calculate_consistency(self.sessions)

        self.assertEqual(result, 100.0)

    def test_empty_sessions(self):
        self.assertEqual(
            calculate_basic_stats([]),
            {
                "total_duration": 0,
                "average_focus": 0,
                "average_distractions": 0
            }
        )

        self.assertEqual(find_best_subject([]), "No data")
        self.assertEqual(find_best_period([]), "No data")
        self.assertEqual(find_most_distracting_subject([]), "No data")
        self.assertEqual(find_best_session_length([]), "No data")
        self.assertEqual(calculate_consistency([]), 0)


if __name__ == "__main__":
    unittest.main()