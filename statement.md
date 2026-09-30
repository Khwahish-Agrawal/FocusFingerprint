# FocusFingerprint - Project Statement

## Problem Statement

Students often study different subjects for different amounts of time and at different times of the day. Their focus and number of distractions can also change from one study session to another.

However, students may not have a simple way to record these study sessions and identify patterns in their study habits.

FocusFingerprint is designed to provide a simple command-line solution where students can record their study sessions and analyze their study duration, focus level, distractions, subject, and study period.

The application processes the collected data and generates a personal FocusFingerprint that summarizes the user's observed study patterns.

---

## Project Scope

The scope of FocusFingerprint includes recording, storing, processing, and analyzing personal study session data.

The project covers:

* Recording individual study sessions.
* Storing study session data in a CSV file.
* Validating user inputs.
* Viewing previously recorded study sessions.
* Calculating total study time.
* Calculating average focus and distractions.
* Identifying the subject with the highest focus.
* Identifying the study period with the highest focus.
* Identifying the most distracting subject.
* Identifying the session length associated with the highest focus.
* Measuring study consistency.
* Generating a personal FocusFingerprint.
* Generating a text-based study report.
* Testing the analysis functions using Python's `unittest` framework.

The current version is a command-line application and does not include a graphical user interface or an external database.

---

## Target Users

The primary target users of FocusFingerprint are:

* School students.
* College and university students.
* Students preparing for examinations.
* Learners who want to track and understand their study habits.

The application is intended for users who want a simple way to maintain study records and observe patterns in their study sessions.

---

## High-Level Features

### 1. Study Session Recording

Users can enter information about their study session, including:

* Date
* Subject
* Duration
* Number of distractions
* Focus rating
* Study period

### 2. Study Data Storage

The recorded sessions are stored in a CSV file so that the information can be retrieved and analyzed later.

### 3. Study Session Viewing

Users can view their previously recorded study sessions from the application.

### 4. Focus Analysis

The application processes the stored data to calculate important study statistics and identify patterns.

### 5. FocusFingerprint Generation

The application creates a personal summary based on the user's strongest subject, preferred study period, best session length, main distraction area, and average focus.

### 6. Report Generation

The application generates a text-based report containing the user's study statistics and identified patterns.

### 7. Automated Testing

The project includes automated tests for the major analysis functions and empty-data handling.

---

## Expected Outcome

The expected outcome of FocusFingerprint is a simple Python application that allows students to record their study sessions and understand their observed study patterns through calculated statistics and a personalized FocusFingerprint.

The project also demonstrates the practical application of Python programming concepts such as functions, modules, data structures, loops, conditions, file handling, CSV processing, exception handling, data processing, and automated testing.
