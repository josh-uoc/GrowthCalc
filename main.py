import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont



####################################
### COMPOUND INTEREST CALCULATOR ### 
####################################



# Compound interest function
def compound(initial, rate, years, per_month):
    month = years * 12
    month_rate = rate / 12
    amount = initial
    for _ in range(month):
        amount = amount * (1 + month_rate) + per_month
    return amount

# # Main test:
# if __name__ == "__main__":
#     initial = float(input("Initial amount (£): £"))
#     rate = float(input("Annual interest rate (%): "))
#     years = int(input("Number of years: "))
#     amount = compound(initial, rate, years)
#     print(f"Total amount after {years} years: £{amount:.2f}")

# Main:
def calc(event=None):
    try:
        # Check for all fields having info:
        if not all([frame.initial_entry.get(), frame.rate_entry.get(), frame.years_entry.get(), frame.per_month_entry.get()]):
            raise ValueError("All fields must be filled")

        # Declare variables:
        initial = float(frame.initial_entry.get())
        rate = float(frame.rate_entry.get()) / 100
        years = int(frame.years_entry.get())
        per_month = float(frame.per_month_entry.get())

        # Check for non-negative:
        if initial < 0 or rate < 0 or years < 0 or per_month < 0:
            raise ValueError("All values must be non-negative.")
        
        # Check for years < 100:
        if years > 100:
            raise ValueError("Number of years should be 100 or less.")
        
        # Check for interest < 100%:
        if rate > 1:
            raise ValueError(f"Interest rate should be 100% or less.")
        
        # Calculation
        amount = compound(initial, rate, years, per_month)
        result_label.config(text=f"Total amount: £{amount:.2f}")
    
    except ValueError as x:
        result_label.config(text=str(x))

# GUI:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Compound Interest Calculator")

    # Styling
    bg_colour = "#333333"
    fg_colour = "#eceff4"
    accent_colour = "#bf616a"

    font = tkfont.Font(family="Helvetica", size=10)

    # Configuration:
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TFrame", background=bg_colour)
    style.configure("Tlabel", background=bg_colour, foreground=fg_colour, font=font)
    style.configure("TEntry", fieldbackground=fg_colour, font=font)
    style.configure("Tbutton", background=accent_colour, foreground=fg_colour, font=font)
    style.map("TButton", background=[('active', accent_colour)])

    # Main frame:
    frame = ttk.Frame(root, padding="20")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=2)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = ttk.Label(frame, text="Compound Interest Calculator", font=("Helvetica", 16, "bold"))
    header_label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

    # Input
    fields = [
        ("Initial amount (£):", "initial"),
        ("Annual interest rate (%):", "rate"),
        ("Number of whole years:", "years"),
        ("Monthly contribution (£):", "per_month"),
    ]

    for i, (label_text, entry_name) in enumerate(fields):
        ttk.Label(frame, text=label_text).grid(column=0, row=i+1, sticky=tk.W, padx=(0, 10), pady=5)
        entry = ttk.Entry(frame, width=20)
        entry.grid(column=1, row=i+1, sticky=tk.E, pady=5)
        setattr(frame, f"{entry_name}_entry", entry)
        entry.bind("<Return>", calc)

    # Calculate button:
    calc_button = ttk.Button(frame, text="Calculate", command=calc)
    calc_button.grid(column=1, sticky=(tk.E), pady=5)

    # Result label:
    result_label = ttk.Label(frame, text="", justify="center", anchor="center", font=("Helvetica", 12, "bold"))
    result_label.grid(column=0, row=len(fields)+2, columnspan=2, sticky=(tk.W, tk.E), pady=10)

    # Grid
    for child in frame.winfo_children():
        child.grid_configure(padx=5)


    # Bind for hitting enter:
    entry.bind("<Return>", calc)

    # Event loop:
    root.geometry("400x400")
    root.mainloop()