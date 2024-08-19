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
        if not all([initial_entry.get(), rate_entry.get(), years_entry.get(), per_month_entry.get()]):
            raise ValueError("All fields must be filled")

        # Declare variables:
        initial = float(initial_entry.get())
        rate = float(rate_entry.get()) / 100
        years = int(years_entry.get())
        per_month = float(per_month_entry.get())

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

    # Inital amount input:
    ttk.Label(frame, text="Initial amount (£):").grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)
    initial_entry = ttk.Entry(frame)
    initial_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=10, pady=10)

    # Annual interest rate input:
    ttk.Label(frame, text="Annual interest rate (%):").grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)
    rate_entry = ttk.Entry(frame)
    rate_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=10, pady=10)

    # Number of years input:
    ttk.Label(frame, text="Number of whole years:").grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)
    years_entry = ttk.Entry(frame)
    years_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=10, pady=10)

    # Monthly contribution input:
    ttk.Label(frame, text="Monthly contribution (£):").grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)
    per_month_entry = ttk.Entry(frame)
    per_month_entry.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=10, pady=10)

    # Calculate button:
    calc_button = ttk.Button(frame, text="Calculate", command=calc)
    calc_button.grid(column=1, row=4, sticky=tk.E, pady=10)

    # Result label:
    result_label = ttk.Label(frame, text="", justify="center", anchor="center", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", padding=(5, 5))
    result_label.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E), pady=10)


    # Binds for hitting enter:
    initial_entry.bind("<Return>", calc)
    rate_entry.bind("<Return>", calc)
    years_entry.bind("<Return>", calc)

    # Event loop:
    root.geometry("400x400")
    root.mainloop()