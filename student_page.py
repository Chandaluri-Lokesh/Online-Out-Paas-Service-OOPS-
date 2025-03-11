from tkinter import *
import tkinter as tk
from tkinter import messagebox
import datetime
import sys
import openpyxl
import pandas as pd


#stored_username = sys.argv[1]
stored_username = 'sys.argv[1]'


# Create an Excel workbook object
workbook = openpyxl.load_workbook('user_details.xlsx')

# Get the active sheet
sheet = workbook.active


homepage = Tk()
homepage.geometry("1450x700+0+0")


def DAYOUT():
    homepage.withdraw()
    dayout = Toplevel()
    dayout.geometry("1450x700+0+0")

    def home():
        dayout.destroy()
        homepage.deiconify()

    Label(dayout, text="DAY OUT", fg="green", font=("times new roman", 50, "bold")).pack()
    Button(dayout, text="Back", font=("times new roman", 15), width=10, height=1, bg="light gray",
           command=home).place(x=0, y=0)

    global out_time_entry, in_time_entry, reason_entry

    Label(dayout, text="Out Time", font=("times new roman", 20)).place(x=550, y=140)
    out_time_entry = Entry(dayout, font=("times new roman", 20))
    out_time_entry.place(x=800, y=140)

    Label(dayout, text="In Time", font=("times new roman", 20)).place(x=550, y=210)
    in_time_entry = Entry(dayout, font=("times new roman", 20))
    in_time_entry.place(x=800, y=210)

    Label(dayout, text="Reason", font=("times new roman", 20)).place(x=550, y=280)
    reason_entry = Entry(dayout, font=("times new roman", 20))
    reason_entry.place(x=800, y=280)

    Button(dayout, text="SUBMIT", font=("times new roman", 20), width=18, command=submit_dayout).place(x=550, y=400)
    Button(dayout, text="HOME", font=("times new roman", 20), width=18, command=home).place(x=850, y=400)


def LONGLEAVE():
    homepage.withdraw()
    longleave = Toplevel()
    longleave.geometry("1450x700+0+0")

    def home():
        longleave.destroy()
        homepage.deiconify()

    Label(longleave, text="LONG LEAVE", fg="green", font=("times new roman", 50, "bold")).pack()
    Button(longleave, text="Back", font=("times new roman", 15), width=10, height=1, bg="light gray",
           command=home).place(x=0, y=0)

    global from_date_entry, to_date_entry, state_entry, city_entry, reason_entry

    Label(longleave, text="From Date", font=("times new roman", 20)).place(x=550, y=140)
    from_date_entry = Entry(longleave, font=("times new roman", 20))
    from_date_entry.place(x=800, y=140)

    Label(longleave, text="To Date", font=("times new roman", 20)).place(x=550, y=210)
    to_date_entry = Entry(longleave, font=("times new roman", 20))
    to_date_entry.place(x=800, y=210)

    Label(longleave, text="State", font=("times new roman", 20)).place(x=550, y=280)
    state_entry = Entry(longleave, font=("times new roman", 20))
    state_entry.place(x=800, y=280)

    Label(longleave, text="City", font=("times new roman", 20)).place(x=550, y=350)
    city_entry = Entry(longleave, font=("times new roman", 20))
    city_entry.place(x=800, y=350)

    Label(longleave, text="Reason", font=("times new roman", 20)).place(x=550, y=420)
    reason_entry = Entry(longleave, font=("times new roman", 20))
    reason_entry.place(x=800, y=420)

    Button(longleave, text="SUBMIT", font=("times new roman", 20), width=18, command=submit_longleave).place(x=550, y=540)
    Button(longleave, text="HOME", font=("times new roman", 20), width=18, command=home).place(x=850, y=540)


def show_history():
    history_window = Toplevel()
    history_window.geometry("600x400")
    history_window.title("History")

    history_text = Text(history_window, width=60, height=20, font=("Arial", 12))
    history_text.pack()

    # Read the DayOut sheet from the Excel file
    dayout_data = pd.read_excel("user_details.xlsx", sheet_name="DayOut")
    history_text.insert(END, "Day Out Requests:\n")
    if not dayout_data.empty:
        history_text.insert(END, dayout_data.to_string(index=False))
    else:
        history_text.insert(END, "No Day Out requests found.")

    # Read the LongLeave sheet from the Excel file
    longleave_data = pd.read_excel("user_details.xlsx", sheet_name="LongLeave")
    history_text.insert(END, "\nLong Leave Requests:\n")
    if not longleave_data.empty:
        history_text.insert(END, longleave_data.to_string(index=False))
    else:
        history_text.insert(END, "No Long Leave requests found.")

    history_text.config(state=DISABLED)


def submit_dayout():
    out_time = out_time_entry.get()
    in_time = in_time_entry.get()
    reason = reason_entry.get()

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [stored_username, current_date, out_time, in_time, reason]

    # Append the row to the Excel sheet
    sheet = workbook["DayOut"]
    sheet.append(row)

    # Save the workbook
    workbook.save("user_details.xlsx")

    messagebox.showinfo("Success", "Day Out request submitted successfully.")
    out_time_entry.delete(0, END)
    in_time_entry.delete(0, END)
    reason_entry.delete(0, END)


def submit_longleave():
    from_date = from_date_entry.get()
    to_date = to_date_entry.get()
    state = state_entry.get()
    city = city_entry.get()
    reason = reason_entry.get()

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [stored_username, current_date, from_date, to_date, state, city, reason]

    # Append the row to the Excel sheet
    sheet = workbook["LongLeave"]
    sheet.append(row)

    # Save the workbook
    workbook.save("user_details.xlsx")

    messagebox.showinfo("Success", "Long Leave request submitted successfully.")
    from_date_entry.delete(0, END)
    to_date_entry.delete(0, END)
    state_entry.delete(0, END)
    city_entry.delete(0, END)
    reason_entry.delete(0, END)


def home():
    homepage.deiconify()


def exit_program():
    workbook.close()
    homepage.destroy()


homepage.protocol("WM_DELETE_WINDOW", exit_program)

Label(homepage, text="HOME", fg="green", font=("times new roman", 50, "bold")).pack()

Button(homepage, text="Day Out", font=("times new roman", 15), width=10, height=1, bg="light gray",
       command=DAYOUT).place(x=550, y=140)

Button(homepage, text="Long Leave", font=("times new roman", 15), width=10, height=1, bg="light gray",
       command=LONGLEAVE).place(x=550, y=240)

Button(homepage, text="Show History", font=("times new roman", 15), width=13, height=1, bg="light gray",
       command=show_history).place(x=540, y=340)

Button(homepage, text="Exit", font=("times new roman", 15), width=10, height=1, bg="light gray",
       command=exit_program).place(x=550, y=440)

homepage.mainloop()
