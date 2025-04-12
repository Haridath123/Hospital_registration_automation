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

## Imports and Libraries:
### Standard Libraries:
- `subprocess`, `sys`: Used for installing external libraries (tabulate and tqdm) through the pip package manager.
- `random`: Used for generating random numbers, e.g., to simulate waiting times and doctor availability.
- `time`, `sleep`: Used for timing functions such as delays in the loading screen or sounds.
- `os`: Provides functionality to interact with the operating system.

### External Libraries:
- `tabulate`: Used for creating neat, formatted tables to display data like meal options, doctor lists, etc.
- `tqdm`: Used for the progress bar in the `loading_screen` function.

## Main Functions:
### `loading_screen()`
- Displays a loading animation using `tqdm` to simulate processing of a transaction.

### `beep_sound()`
- Simulates a beep sound using the ASCII Bell character and pauses for 3 seconds.

### `welcome()`
- Prints an ASCII art welcome message and introduces the hospital booking system.

### `proceed()`
- Prompts the user to either proceed with the hospital booking system or exit.

### `patient_type()`
- Asks the user whether they are a new patient, an emergency case, or an admitted patient.
  - If the user selects "Emergency", it redirects them to the emergency department and exits further patient booking.
  - If the user selects "Admitted Patient", the food request section is triggered.

### `food_request()`
- Displays food options and takes user input for meal preferences for admitted patients.

### `display_specializations()`
- Displays available specializations (such as Dentistry, Optometry, etc.) in a formatted table.

### `select_specialization()`
- Prompts the user to choose a specialization and displays the corresponding doctor list.

### `display_doctors()`
- Displays the list of available doctors in the chosen specialization along with their qualifications and estimated waiting times.

### `select_doctor()`
- Prompts the user to select a doctor from the available list, shows waiting times, and allows them to change the doctor if they wish.

### `process_payment()`
- Handles the payment process, allowing the user to choose between online (Google Pay) or cash payment, and simulates the payment transaction.

### `hospital_booking()`
- The main function that orchestrates the hospital booking system flow:
  - Starts by selecting the patient type.
  - Guides the user through specialization selection, doctor selection, food request (for admitted patients), and payment processing.
  - Ends with confirming the appointment after successful payment.

## Data:
- `specializations`: A dictionary holding different medical specialties (e.g., Dentistry, Optometry, ENT) and their corresponding available doctors. Each doctor has a random number of patients and a random waiting time associated with them.

## Flow of Execution:
1. The program begins by calling the `welcome()` function to display the hospital's greeting message.
2. Next, the `proceed()` function is called to ask the user if they wish to continue. If they choose to exit, the program ends.
3. If they proceed, the `hospital_booking()` function is executed, which guides the user through selecting a patient type, specialization, doctor, and payment options.
4. The entire process is modularized into functions, making it easy to maintain, test, and modify specific sections of the program.

## Key Concepts:
- **Modularization**: The program is divided into separate functions that handle specific tasks, making the code cleaner and easier to understand.
- **User Interaction**: The program relies on user inputs at various points (e.g., for selecting patient types, specializations, doctors, and payment methods).
- **Randomization**: The `random` module is used to simulate waiting times and the number of patients for each doctor, making the booking process more dynamic and realistic.
- **Formatted Output**: The `tabulate` library is used to present data in neatly organized tables for better readability.

## Modules and Interconnections:
- `loading_screen()` and `beep_sound()` are utility functions used to simulate user feedback during the booking process.
- `patient_type()`, `food_request()`, and `hospital_booking()` are the key control flow functions, each triggering different parts of the booking system.
- The `specializations` dictionary connects the user's input with relevant doctor lists, which are then displayed by `select_specialization()` and `select_doctor()`.


---

## How to Run

1. Clone the repo or download the `.py` file.
2. Make sure you have Python 3 installed.
3. Install dependencies (if not already):
   ```bash
   pip install tqdm tabulate
>WELCOME TO TRIVANDRUM MEDICARE CENTER
>Please enter your name: Hari
>Select patient type:
>1. New Patient
>2. Emergency
>3. Admitted

>--> Booking appointment with Orthopedic department...
>--> Your doctor is Dr. Sameer Kumar
>--> Estimated wait time: 20 minutes
