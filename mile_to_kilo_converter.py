from tkinter import *

window = Tk()
window.title("Miles To Kilometer Converter")

mile_input = Entry()
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")

kilometer_result_label = Label(text="0")

kilometer_label = Label(text="Km")

calculate_button = Button(text="Calculate")


window.mainloop()