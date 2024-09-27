import tkinter as tk
from tkinter import ttk, Canvas
from tkinter import font as tkfont
import ttkbootstrap as tkb
from ttkbootstrap.tooltip import ToolTip
import PySide6.QtCore



####################################
### COMPOUND INTEREST CALCULATOR ### 
####################################



### FUNCTIONS ###

# Compound interest function
def compound(initial, rate, years, per_month):
    month = years * 12
    month_rate = rate / 12
    amount = initial
    for _ in range(month):
        amount = amount * (1 + month_rate) + per_month
    return amount


# Decimal check
def decimal(value, max=2):
    try:
        pounds, pence = value.split(".")
        return len(pence) <= max
    except ValueError:
        return True

# Calculation
def calc(event=None):
    try:
        # Retrieve and clean inputs
        initial = frame.initial_entry.get().replace(",", "")
        rate = frame.rate_entry.get().replace(",", "")
        years = frame.years_entry.get().replace(",", "")
        per_month = frame.per_month_entry.get().replace(",", "")
        
        # Check for all fields having info
        if not all([frame.initial_entry.get(), frame.rate_entry.get(), frame.years_entry.get(), frame.per_month_entry.get()]):
            raise ValueError("All fields must be filled.")
        if not(initial.replace(".","", 1).isdigit() and rate.replace(".", "", 1).isdigit() and years.isdigit() and per_month.replace(".", "", 1).isdigit()):
            raise ValueError("All fields must be numeric.")
        
        # Decimal check
        if not decimal(initial):
            raise ValueError("Pence amount should not have more than two decimal places.")
        if not decimal(per_month):
            raise ValueError ("Pence amount should not have more than two decimal places.")

        # Converts inputs to appropriate types
        initial = float(initial)
        rate = float(rate) / 100
        years = int(years)
        per_month = float(per_month)

        # Check for non-negative
        if initial < 0 or rate < 0 or years < 0 or per_month < 0:
            raise ValueError("All values must be non-negative.")
        
        # Check for years < 100
        if years > 100:
            raise ValueError("Number of years should be 100 or less.")
        
        # Check for interest < 100%
        if rate > 1:
            raise ValueError(f"Interest rate should be 100% or less.")
        
        # Calculation
        amount = compound(initial, rate, years, per_month)
        result_label.config(text=f"Total amount:\n£{amount:.2f}")
    
    except ValueError as x:
        result_label.config(text=str(x))

# Tooltips
def tooltips():
    ToolTip(frame.initial_entry, text="Enter the initial amount in GBP.")
    ToolTip(frame.rate_entry, text="Enter the annual interest rate as a percentage.")
    ToolTip(frame.years_entry, text="Enter the number of whole years.")
    ToolTip(frame.per_month_entry, text="Enter the monthly contribution in GBP.")

def dpi():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass



### GUI ###

# Main
if __name__ == "__main__":
    dpi()
    root = tk.Tk()
    root.title("GrowthCalc")

    # Window styling
    root.geometry("450x550")
    root.resizable(False, False)

    # Styling
    bg_colour = "#1e1e1e"
    fg_colour = "#f4f4f4"
    accent_colour = "#005a9e"
    entry_bg_colour = "#333333"
    button_colour = "#0078d7"

    title_font = tkfont.Font(family="Segoe UI", size=22)
    main_font = tkfont.Font(family="Segoe UI", size=12)
    result_font = tkfont.Font(family="Segoe UI", size=16)

    # Configuration
    style = tkb.Style()
    style.theme_use('cosmo')
    style.configure("TFrame", background=bg_colour)
    style.configure("TLabel", background=bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TEntry", fieldbackground=entry_bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TButton", background=button_colour, foreground=fg_colour, font=main_font)
    style.map("TButton", background=[('active', accent_colour)])

    # Main frame
    frame = tkb.Frame(root, padding="30")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
    frame.configure(border=0, relief="flat")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = tkb.Label(frame, text="Compound Interest\n        Calculator", font=title_font, anchor="center")
    header_label.grid(column=0, row=0, columnspan=3, pady=(0, 30))

    # Input
    fields = [
        ("Initial amount (£):\t", "initial"),
        ("Annual interest rate (%):\t", "rate"),
        ("Number of whole years:\t", "years"),
        ("Monthly contribution (£):\t", "per_month"),
    ]

    for i, (label_text, entry_name) in enumerate(fields):
        tkb.Label(frame, text=label_text, font=main_font).grid(column=0, row=i+1, sticky=tk.W, pady=10)
        entry = tkb.Entry(frame, width=30)
        entry.grid(column=1, row=i+1, sticky=tk.E, pady=10)
        setattr(frame, f"{entry_name}_entry", entry)
        entry.bind("<Return>", calc)
        entry.configure(takefocus=1)

    # Calculate button
    calc_button = tkb.Button(frame, text="Calculate", command=calc, width=20, takefocus=False)
    calc_button.grid(column=0, columnspan=2, row=len(fields)+1, pady=30)
    calc_button.configure(takefocus=1)
    calc_button.bind("<Return>", lambda event: calc())
    calc_button.bind("<space>", lambda event: calc())

    # Result label
    result_label = tkb.Label(frame, text="", justify="center", anchor="center", font=result_font, wraplength=380)
    result_label.grid(column=0, columnspan=2, row=len(fields)+2, sticky=(tk.W, tk.E), pady=15)

    # Grid
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Bind for hitting enter
    root.bind("<Return>", calc)
    calc_button.bind("<Return>", calc)

    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()