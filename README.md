# FocusFingerprint - Personal Study Pattern Analyzer

## Overview

FocusFingerprint is a Python-based command-line application that helps students understand their personal study patterns.

The application records study sessions and analyzes factors such as study duration, focus rating, distractions, subject, and study period. Based on the collected data, it generates a personal FocusFingerprint that summarizes the user's study habits.

The project uses Python programming concepts such as functions, modules, dictionaries, lists, loops, conditions, file handling, CSV processing, exception handling, data processing, and automated testing.

---

## Problem Statement

Students often study for different amounts of time, at different times of the day, and with different levels of concentration. However, they may not have a simple way to identify which study conditions work best for them.

FocusFingerprint provides a simple command-line solution for recording study sessions and identifying useful patterns from the collected data.

---

## Objectives

* Record individual study sessions.
* Store study data using a CSV file.
* Validate user input.
* Calculate basic study statistics.
* Identify the subject with the highest focus.
* Identify the most effective study period.
* Identify the session length associated with the highest focus.
* Identify the subject with the highest average distractions.
* Measure study consistency.
* Generate a personalized FocusFingerprint.
* Generate a text-based study report.
* Test the analysis functions automatically.

---

## Features

### 1. Add Study Session

The user can enter:

* Date
* Subject
* Study duration
* Number of distractions
* Focus rating from 1 to 5
* Study period

The application validates important numeric inputs before saving the session.

### 2. View Study Sessions

Displays previously recorded study sessions from the CSV file.

### 3. Analyze Focus

The application calculates:

* Total study time
* Average focus
* Average distractions
* Best subject for focus
* Best study period
* Most distracting subject
* Best session length
* Study consistency

### 4. Generate FocusFingerprint

The application combines the analysis results into a personalized study pattern summary.

### 5. Generate Report

The application creates a text report containing the user's study statistics, study patterns, and FocusFingerprint.

The report is saved at:

```text
reports/focus_report.txt
```

### 6. Automated Testing

The project includes seven test cases covering the main analysis functions and empty-data handling.

---

## Technology Used

* Python 3.14.7
* CSV file handling
* Python `unittest`
* Visual Studio Code
* Git
* GitHub

No external Python packages are required to run the current version.

---

## Project Structure

```text
FocusFingerprint/

│
├── README.md
├── statement.md
├── main.py
├── session_manager.py
├── data_handler.py
├── analyzer.py
├── fingerprint.py
├── report_generator.py
│
├── data/
│   └── study_sessions.csv
│
├── reports/
│   └── focus_report.txt
│
├── tests/
│   └── test_analyzer.py
│
└── docs/
    ├── architecture.png
    ├── workflow.png
    ├── use_case.png
    ├── class_diagram.png
    ├── sequence_diagram.png
    └── storage_diagram.png
```

---

## How the Application Works

```text
User
  ↓
Add Study Session
  ↓
Input Validation
  ↓
CSV Storage
  ↓
Data Analysis
  ↓
FocusFingerprint
  ↓
Study Report
```

---

## Installation and Setup

### 1. Install Python

Python 3.14 or a compatible Python 3 version is required.

Check the installed Python version using:

```text
python --version
```

### 2. Open the Project Folder

Open the `FocusFingerprint` folder in Visual Studio Code.

### 3. Run the Application

Open the terminal inside the project folder and run:

```text
python main.py
```

---

## Application Menu

When the application starts, the following menu is displayed:

```text
========================================
          FOCUSFINGERPRINT
========================================
Personal Study Pattern Analyzer

1. Add Study Session
2. View Study Sessions
3. Analyze Focus
4. Generate FocusFingerprint
5. Generate Report
6. Exit
```

Enter the corresponding number to select an operation.

---

## Running Tests

The project uses Python's built-in `unittest` framework.

Run the tests using:

```text
python -m unittest tests/test_analyzer.py
```

The current test suite contains seven test cases.

Expected result:

```text
.......
----------------------------------------------------------------------
Ran 7 tests

OK
```

---

## Data Storage

Study session data is stored in:

```text
data/study_sessions.csv
```

Each record contains:

```text
date
subject
duration
distractions
focus_rating
period
```

The CSV file allows the application to save and retrieve study sessions without requiring an external database.

---

## Generated Report

The application generates a text report at:

```text
reports/focus_report.txt
```

The report contains:

* Basic study statistics
* Average focus
* Average distractions
* Best subject for focus
* Best study period
* Best session length
* Most distracting subject
* Study consistency
* FocusFingerprint summary

---

## Input Validation

The application validates user input to prevent invalid values.

The following rules are applied:

* Study duration must be greater than 0.
* Number of distractions cannot be negative.
* Focus rating must be between 1 and 5.
* Invalid numeric input is handled without crashing the program.

---

## Testing

The current test suite checks:

1. Basic statistics calculation.
2. Best subject detection.
3. Best study period detection.
4. Most distracting subject detection.
5. Best session length detection.
6. Study consistency calculation.
7. Empty session handling.

All seven current tests pass successfully.

---

## Future Enhancements

Possible future improvements include:

* Graphical visualization of study patterns.
* Weekly and monthly analysis.
* More detailed distraction analysis.
* Exporting reports to PDF.
* Additional study habit metrics.
* Interactive dashboards.
* Improved date validation.

---

## Project Purpose

FocusFingerprint was developed as a Python Essentials project to demonstrate the practical use of Python programming concepts in a meaningful student-focused application.
