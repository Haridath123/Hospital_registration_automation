import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])

import random
import time
from tabulate import tabulate
from tqdm import tqdm
from time import sleep
import os

def loading_screen():
    print("Processing transaction...")
    for i in tqdm(range(0, 100), total=100, desc="Loading..."):
        sleep(0.1)

def beep_sound():
    print("\a")  # Produces a beep sound
    sleep(3)

def welcome():                                                                                                                                                                     
    print("                                &&&&                                                                                                                                   ")
    print("                               &&&&&&                                                                                                                                  ")
    print("             &&&              &&&&&&&&&             &&&                                                                                                                ")
    print("            &&&&&&&&        &&&&&&&&&&&         &&&&&&&&                                                                                                               ")
    print("            &&&&&&&&&&&&    &&&&&&&&&&&&     &&&&&&&&&&&                                                                                                               ")
    print("            &&&&&&&&&&&&&& &&&&&&&&&&&&&& &&&&&&&&&&&&&&                                    &&&&                                                                       ")
    print("           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                   &&&&&&&&&&      &&&&      &&&&&&&&&   &&&&&&&&&&     &&&&       &&&&  &&&&&&&&&&&&         ")
    print("           &&&&&&&&&&&&&&&& &&&&&&&&&&&& &&&&&&&&&&&&&&&&                  &&&&&&&&&&&&&    &&&&    &&&&&&&&&&&&  &&&&&&&&&&&    &&&&       &&&&  &&&&&&&&&&&&         ")
    print("           &&&&&&&&&&&&&&&&   &&&&&&&&&   &&&&&&&&&&&&&&&                  &&&&      &&&&    &&&   &&&&       &&  &&&     &&&&   &&&&       &&&&          &&&&         ")
    print("           &&&&&&&&&&&&&&&     &&&&&&     &&&&&&&&&&&&&&&                  &&&&       &&&&   &&&   &&&&           &&&&     &&&   &&&&       &&&&         &&&&          ")
    print("           &&&&&&&&&&&&&&&      &&&&      &&&&&&&&&&&&&&&                  &&&&        &&&        &&&&            &&&     &&&&   &&&&       &&&&        &&&&           ")
    print("            &&&&&&&&&&&&&&       &&       &&&&&&&&&&&&&&                   &&&&        &&&        &&&&            &&&&&&&&&&&    &&&&       &&&&       &&&&            ")
    print("          &&&&&&&&&&&&&&&&                &&&&&&&&&&&&&&&&&                &&&&        &&&        &&&&            &&&&&&&&&      &&&&       &&&&      &&&&             ")
    print("    &&&&&&&&&&    &&&&&&&&                &&&&&&&&    &&&&&&&&&&&          &&&&        &&&        &&&&            &&&   &&&&&    &&&&       &&&&     &&&&              ")
    print("   &&&&&&&&&&&        &&&&                &&&&        &&&&&&&&&&           &&&&       &&&&        &&&&            &&&    &&&&    &&&&       &&&&    &&&&               ")
    print("    &&&&&&&&&&&                                      &&&&&&&&&&&           &&&&      &&&&          &&&&           &&&     &&&&    &&&       &&&&   &&&&                ")
    print("    &&&&&&&&&&&&                                     &&&&&&&&&&&           &&&&  &&&&&&&&           &&&&&   &&&&  &&&      &&&    &&&&&   &&&&&   &&&&                 ")
    print("     &&&&&&&&&&&                                    &&&&&&&&&&&            &&&&&&&&&&&&              &&&&&&&&&&   &&&&     &&&&    &&&&&&&&&&&    &&&&&&&&&&&&&        ")
    print("      &&&&&&&&&&&                                  &&&&&&&&&&&              &&&&&&&                     &&&&&      &&       &&&       &&&&&        &&&&&&&&&&&         ")
    print("       &&&&&&&&&&&                                &&&&&&&&&&&                                                                                                          ")
    print("        &&&&&&&&&&&&                            &&&&&&&&&&&&                                                                                                           ")
    print("          &&&&&&&&&&&                          &&&&&&&&&&&                 &&  &&        &&&&         &&&       &&&&&       &       &&&&&&       &&         &&         ")
    print("           &&&&&&&&&&&&                      &&&&&&&&&&&&                  &&  &&      &&&  &&       &&         && &&       &&        &&         &&&        &&         ")
    print("             &&&&&&&&&&&&                  &&&&&&&&&&&&                    &&  &&      &&&  &&         &&&      &&&&        &&        &&        &&&&        &&         ")
    print("                &&&&&&&&&&&              &&&&&&&&&&&                       &&  &&       &&&&&&       &&&&&      &&          &&        &&       &&  &&       &&&&       ")
    print("                   &&&&&&&&&&&        &&&&&&&&&&&                                                                                                                      ")
    print("                        &&&&&&&&&  &&&&&&&&&                                                                                                                           ")
                                                                                                                                                                       
                                                                                                                                                                       
                                                                                                                                                                       
    print("\n")
    print("Hi, welcome to the Hospital Booking System!")

def proceed():
    while True:
        choice = input("Do you wish to proceed? (1 for Yes / 2 for Exit): ")
        if choice == "2":
            print("Thank you for visiting!")
            return False
        elif choice == "1":
            return True
        else:
            print("Invalid input. Try again.")

def patient_type():
    while True:
        choice = input("Are you a new patient, an emergency case, or an admitted patient? (1 for New Patient / 2 for Emergency / 3 for Admitted Patient): ")
        if choice == "1":
            return "new_patient"
        elif choice == "2":
            beep_sound()
            print("Forwarding your call to the emergency department. Thank you for choosing our hospital.")
            return None
        elif choice == "3":
            food_request()
            return None
        else:
            print("Invalid input. Try again.")

def food_request():
    print("Admitted Patient - Food Request Section")
    food_options = [
        ["1", "Breakfast"],
        ["2", "Lunch"],
        ["3", "Dinner"]
    ]
    print(tabulate(food_options, headers=["Number", "Meal"], tablefmt="grid"))
    while True:
        choice = input("Select a meal option (Numbers only): ")
        if choice in ["1", "2", "3"]:
            print("Your request has been noted. Our staff will deliver your meal shortly.")
            return
        else:
            print("Invalid selection. Try again.")

def display_specializations():
    data = [[num, spec[0]] for num, spec in specializations.items()]
    print(tabulate(data, headers=["Number", "Specialization"], tablefmt="grid", showindex=False))

def select_specialization():
    while True:
        print("Select a medical specialization (Numbers only):")
        display_specializations()
        print("15. Emergency")
        
        try:
            spec_choice = int(input("Enter your choice (Numbers only): "))
            if spec_choice == 15:
                beep_sound()
                print("Forwarding your call to the emergency department. Thank you for choosing our hospital.")
                return None
            elif spec_choice in specializations:
                return specializations[spec_choice]
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_doctors(spec_name, doctors):
    print(f"Available doctors in {spec_name}:")
    table_data = []
    for num, (doc, qual, _) in doctors.items():
        waiting_patients = random.randint(1, 20)
        min_wait_time = 5 if waiting_patients < 5 else 40
        wait_time = random.randint(min_wait_time, 100)
        table_data.append([num, doc, qual, waiting_patients, wait_time])
    
    print(tabulate(table_data, headers=["Number", "Doctor", "Qualification", "Waiting Patients", "Estimated Wait Time (min)"], tablefmt="grid", showindex=False))
    return table_data

def select_doctor(spec_name, doctors):
    while True:
        doctor_list = display_doctors(spec_name, doctors)
        try:
            doc_choice = int(input("Select a doctor (Numbers only, or 0 to go back): "))
            if doc_choice == 0:
                return None
            elif 1 <= doc_choice <= len(doctor_list):
                doc_name, qual, wait_count, wait_time = doctor_list[doc_choice - 1][1:]
                print(f"Estimated waiting time: {wait_time} minutes")
                change_doctor = input("Do you want to select another doctor? (Y/N): ")
                if change_doctor.lower() == "y":
                    continue
                return doc_name, qual, wait_time
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def process_payment(total_price):
    print("Payment Options:")
    print("1. Google Pay")
    print("2. Cash Payment at Reception")
    payment_choice = input("Select a payment method: ")
    
    if payment_choice == "1":
        print(f"Please send ₹{total_price} to Google Pay number: {random.randint(6000000000, 9999999999)}")
    elif payment_choice == "2":
        print(f"Please pay ₹{total_price} at the reception desk.")
    else:
        print("Invalid payment option. Try again.")
        return process_payment(total_price)
    
    loading_screen()
    print("Payment received. Appointment confirmed.")

def hospital_booking():
    if patient_type() is None:
        return
    
    while True:
        specialization = select_specialization()
        if not specialization:
            return
        spec_name, doctors = specialization
        
        while True:
            doctor_selection = select_doctor(spec_name, doctors)
            if doctor_selection is None:
                break
            
            doc_name, qual, wait_time = doctor_selection
            
            special_services = input("Do you require special services (wheelchair/manual assistance)? (Y/N): ")
            consultation_fee = 300
            
            print(f"Total consultation fee: ₹{consultation_fee}")
            process_payment(consultation_fee)
            phone_number = input("Enter your phone number to receive a receipt: ")
            print(f"Receipt sent to {phone_number}. Thank you for choosing our hospital!")
            return

specializations = {
    1: ("Dentistry", {1: ("Dr. Arya Menon", "BDS, MDS Oral Surgery", random.randint(20, 30)), 2: ("Dr. Ravi Kumar", "BDS, MDS Prosthodontics", random.randint(20, 30)), 3: ("Dr. Sameer Rao", "BDS, MDS Endodontics", random.randint(20, 30))}),
    2: ("Optometry", {1: ("Dr. Sunil Raj", "MBBS, MS Ophthalmology", random.randint(5, 10)), 2: ("Dr. Meera Das", "MBBS, DO", random.randint(5, 10)), 3: ("Dr. Ankit Sharma", "MBBS, MS Optometry", random.randint(5, 10))}),
    3: ("ENT", {1: ("Dr. Kiran V", "MBBS, MS ENT", random.randint(25, 35)), 2: ("Dr. Anjali Bose", "MBBS, DNB ENT", random.randint(25, 35)), 3: ("Dr. Rajeev Menon", "MBBS, MS ENT", random.randint(25, 35))}),
    4: ("Cardiology", {1: ("Dr. Rajesh Iyer", "MBBS, DM Cardiology", random.randint(5, 10)), 2: ("Dr. Neha Verma", "MBBS, MD Internal Medicine", random.randint(5, 10)), 3: ("Dr. Vikram Reddy", "MBBS, DM Cardiology", random.randint(5, 10))}),
    5: ("Neurology", {1: ("Dr. Vishal Nair", "MBBS, DM Neurology", random.randint(5, 10)), 2: ("Dr. Sneha Pillai", "MBBS, MD Neurology", random.randint(5, 10)), 3: ("Dr. Arjun Khanna", "MBBS, DM Neurology", random.randint(5, 10))}),
    6: ("Orthopedics", {1: ("Dr. Arun Joseph", "MBBS, MS Orthopedics", random.randint(5, 10)), 2: ("Dr. Kavita Rao", "MBBS, DNB Spine Surgery", random.randint(5, 10)), 3: ("Dr. Sandeep Bhatt", "MBBS, MS Orthopedics", random.randint(5, 10))}),
    7: ("Gynecology", {1: ("Dr. Anu Menon", "MBBS, MD Gynecology", random.randint(5, 10)), 2: ("Dr. Priya Das", "MBBS, MS Obstetrics & Gynecology", random.randint(5, 10)), 3: ("Dr. Shweta Aggarwal", "MBBS, MD Gynecology", random.randint(5, 10))}),
    8: ("Dermatology", {1: ("Dr. Ramesh Krishnan", "MBBS, MD Dermatology", random.randint(25, 35)), 2: ("Dr. Nisha Balan", "MBBS, DDVL Dermatology", random.randint(25, 35)), 3: ("Dr. Veena Kapoor", "MBBS, MD Dermatology", random.randint(25, 35))}),
    9: ("General Medicine", {1: ("Dr. Arvind Nair", "MBBS, MD General Medicine", random.randint(10, 15)), 2: ("Dr. Swetha Mohan", "MBBS, MD Internal Medicine", random.randint(10, 15)), 3: ("Dr. Rohit Shetty", "MBBS, MD General Medicine", random.randint(10, 15))})
}

welcome()
if proceed():
    hospital_booking()
