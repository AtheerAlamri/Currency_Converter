from tkinter import *


# Create class
class CurrencyConverter:

    # Self is a variable that represents an instance of the object itself
    def __init__(self):
        window = Tk()  # Create application window
        window.title("Currency Converter")  # Add title to application window
        window.configure(bg="#cdd4d3")  # Add background color to application window

        # Adding Label widgets to application window
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", text="Amount to convert").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", text="Conversion rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", fg="#800080", text="Converted Amount").grid(row=3, column=1, sticky=W)

        # Create objects and add entry functions
        self.amountToConvertVar = StringVar()
        Entry(window, textvariable=self.amountToConvertVar, justify=RIGHT).grid(row=1, column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable=self.conversionRateVar, justify=RIGHT).grid(row=2, column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window, font="Helvetica 12 bold", bg="#cdd4d3", textvariable=self.convertedAmountVar)
        lblConvertedAmount.grid(row=3, column=2, sticky=E)

        # Create convert and clear buttons, when clicked they will call their respective functions.
        Convert = Button(window, text="Convert", font="Helvetica 12 bold", bg="#58554a", fg="white", command=self.convert)
        Convert.grid(row=4, column=2, sticky=E)
        Delete_all = Button(window, text="Clear", font="Helvetica 12 bold", bg="#a52a2a", fg="white", command=self.delete)
        Delete_all.grid(row=4, column=6, padx=25, pady=25, sticky=E)

        window.mainloop()  # Runs the application program

    # Function to do the conversion. Stares inputs and performs conversion
    def convert(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amountToConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

    # Function to clear inputs
    def delete(self):
        self.amountToConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")


CurrencyConverter()
