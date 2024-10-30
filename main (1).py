import tkinter as tk
from tkinter import *
from datetime import date

main = tk.Tk()
main.title("Age Calculator")
main.geometry("500x500")

name_value = StringVar()
year_value = StringVar()
month_value = StringVar()
day_value = StringVar()

name_entry = Entry(main, textvariable=name_value)
name_entry.grid(row=1, column=2)

year_entry = Entry(main, textvariable=year_value)
year_entry.grid(row=2, column=2)

month_entry = Entry(main, textvariable=month_value)
month_entry.grid(row=3, column=2)

day_entry = Entry(main, textvariable=day_value)
day_entry.grid(row=4, column=2)

Label(text="Name").grid(row=1, column = int(2))
Label(text="Year").grid(row=2, column = int(2))
Label(text="Month").grid(row=3, column = int(2))
Label(text="Day").grid(row=4, column = int(2))

date_today = date.today()
current_year = date_today.year
current_month = date_today.month
current_day = date_today.day

# print(current_year)
# print(year_value.get())


def calculateAge():

  years_old = int(current_year) - int(year_value.get())

  if (current_month, current_day) < (int(month_entry.get()),
                                     int(day_entry.get())):
    years_old -= 1
    

  if (current_month, current_day) == (int(month_entry.get()),
                                      int(day_entry.get())):
    Label(text="Happy Birthday!").grid(row=6, column = 2)
    
  else:
    print(years_old)

  
  Label(text=f"{name_entry.get()}, you are {years_old} years old.").grid(row=7, column = int(2))


#Labels and Buttons
age_button = Button(text="Calculate Age", command=calculateAge).grid(row=5,
                                                                     column=2)

  

main.mainloop()
