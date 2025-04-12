# Hospital Booking System

A feature-rich, console-based hospital appointment and food request simulation written in Python. This project mimics a real-world hospital booking experience with interactive flows, dynamic doctor selection, emergency handling, payment simulation, and more.

---

## Features

- Handles New, Emergency, and Admitted patients with different flows.
- Automatically assigns a doctor based on department and availability.
- Uses the `datetime` module and random delays for realism.
- Admitted patients can order meals with detailed menus.
- Simulates GPay or cash payments with fake UPI IDs.
- Uses `tabulate` for clean data display.
- Adds life to the CLI using `tqdm`.
- Handles edge cases, user errors, and flow control.

---

## Tech Stack

- Python 3
- `tqdm` for animations
- `tabulate` for table formatting
- `random`, `datetime`, `time`, and `os` from Python standard library

---

## How to Run

1. Clone the repo or download the `.py` file.
2. Make sure you have Python 3 installed.
3. Install dependencies (if not already):
   ```bash
   pip install tqdm tabulate
>WELCOME TO TRIVANDRUM MEDICARE CENTER
Please enter your name: Hari
Select patient type:
1. New Patient
2. Emergency
3. Admitted

--> Booking appointment with Orthopedic department...
--> Your doctor is Dr. Sameer Kumar
--> Estimated wait time: 20 minutes
