# FocusFingerprint - Functional and Non-Functional Requirements

## 1. Functional Requirements

Functional requirements describe what the FocusFingerprint application should do.

### FR1 - Add Study Session

The system shall allow the user to enter a new study session.

The session shall contain:

* Date
* Subject
* Study duration in minutes
* Number of distractions
* Focus rating from 1 to 5
* Study period

### FR2 - Validate User Input

The system shall validate the values entered by the user.

The system shall:

* Accept only positive study duration.
* Prevent negative distraction values.
* Accept focus ratings only from 1 to 5.
* Handle invalid numeric input without terminating the application unexpectedly.

### FR3 - Store Study Session

The system shall store valid study session data in a CSV file.

The stored information shall include:

* Date
* Subject
* Duration
* Distractions
* Focus rating
* Study period

### FR4 - View Study Sessions

The system shall allow the user to view previously recorded study sessions.

Each displayed session shall show its recorded date, subject, duration, distractions, focus rating, and study period.

### FR5 - Calculate Basic Statistics

The system shall calculate:

* Total study duration.
* Average focus rating.
* Average number of distractions.

### FR6 - Identify Study Patterns

The system shall analyze recorded sessions to identify:

* Best subject for focus.
* Best study period.
* Most distracting subject.
* Best session length.
* Study consistency.

### FR7 - Generate FocusFingerprint

The system shall generate a personalized FocusFingerprint based on the analyzed study data.

The fingerprint shall summarize:

* Strongest subject.
* Best study period.
* Best session length.
* Main distraction area.
* Average focus.

### FR8 - Generate Study Report

The system shall generate a text-based study report containing the calculated statistics and identified study patterns.

The generated report shall be stored in the `reports` folder.

### FR9 - Handle Empty Data

The system shall provide an appropriate message when no study sessions are available instead of attempting to analyze empty data.

### FR10 - Run Automated Tests

The project shall provide automated tests for the main analysis functions using Python's built-in `unittest` framework.

---

## 2. Non-Functional Requirements

Non-functional requirements describe how the application should perform and the qualities it should maintain.

### NFR1 - Usability

The application should provide a simple command-line interface with clear menu options and understandable messages so that students can use it without complex instructions.

### NFR2 - Performance

The application should process stored study sessions efficiently and produce analysis results without unnecessary processing.

### NFR3 - Reliability

The application should handle invalid user input and empty data safely without unexpectedly terminating during normal use.

### NFR4 - Maintainability

The project should be divided into separate Python modules based on their responsibilities.

For example:

* `main.py` handles the main application flow.
* `session_manager.py` handles session input.
* `data_handler.py` handles CSV storage.
* `analyzer.py` handles data analysis.
* `fingerprint.py` generates the FocusFingerprint.
* `report_generator.py` generates the report.

### NFR5 - Data Integrity

The application should store valid study session information consistently in the CSV file and should not intentionally modify previously stored session values during normal operations.

### NFR6 - Portability

The application should run on systems that support a compatible Python 3 environment without requiring platform-specific software.

### NFR7 - Testability

The main data analysis functions should be independently testable using Python's `unittest` framework.

### NFR8 - Simplicity

The application should use Python's standard library for its current implementation and avoid unnecessary external dependencies.

---

## 3. Input Requirements

The application accepts the following information from the user:

| Input        | Description                           | Validation              |
| ------------ | ------------------------------------- | ----------------------- |
| Date         | Date of the study session             | User-provided date      |
| Subject      | Subject studied                       | Text input              |
| Duration     | Study duration in minutes             | Must be greater than 0  |
| Distractions | Number of distractions                | Cannot be negative      |
| Focus Rating | Focus level during the session        | Must be between 1 and 5 |
| Study Period | Morning, Afternoon, Evening, or Night | Text input              |

---

## 4. Output Requirements

The application provides the following outputs:

* Confirmation after successfully adding a study session.
* List of stored study sessions.
* Basic study statistics.
* Identified study patterns.
* Personal FocusFingerprint.
* Generated study report.
* Appropriate messages for invalid input and unavailable data.

---

## 5. Requirement Summary

FocusFingerprint is designed to provide a simple and modular way to record study sessions, store the collected information, analyze study patterns, and generate a personalized summary.

The requirements focus on functionality, usability, reliability, maintainability, performance, data integrity, portability, and testability.
