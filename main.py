import tkinter as tk
from tkinter import ttk



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
        initial = float(initial_entry.get())
        rate = float(rate_entry.get()) / 100
        years = int(years_entry.get())
        per_month = float(per_month_entry.get())
        amount = compound(initial, rate, years, per_month)
        result_label.config(text=f"Total amount: £{amount:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# TKinter:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Compound Interest Calculator")


    # Theme:
    style = ttk.Style()
    style.configure("Tlabel", font=("Helvetica", 12))
    style.configure("Tbutton", font=("Helvetica", 12))

    # Frame & grid:
    frame = ttk.Frame(root, padding="20")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Inital amount input:
    ttk.Label(frame, text="Initial amount (£):").grid(column=0, row=0, sticky=tk.W, pady=5)
    initial_entry = ttk.Entry(frame)
    initial_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=5)

    # Annual interest rate input:
    ttk.Label(frame, text="Annual interest rate (%):").grid(column=0, row=1, sticky=tk.W, pady=5)
    rate_entry = ttk.Entry(frame)
    rate_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=5)

    # Number of years input:
    ttk.Label(frame, text="Number of whole years:").grid(column=0, row=2, sticky=tk.W, pady=5)
    years_entry = ttk.Entry(frame)
    years_entry.grid(column=1, row=2)

    # Monthly contribution input:
    ttk.Label(frame, text="Monthly contribution (£):").grid(column=0, row=3, sticky=tk.W, pady=5)
    per_month_entry = ttk.Entry(frame)
    per_month_entry.grid(column=1, row=3, sticky=(tk.W, tk.E), pady=5)

    # Calculate button:
    calc_button = ttk.Button(frame, text="Calculate", command=calc)
    calc_button.grid(column=1, row=4, sticky=tk.E, pady=10)

    # Result label:
    result_label = ttk.Label(frame, text="", justify="center", anchor="center", font=("Helvetica", 12, "italic"), borderwidth=1, relief="solid", padding=(5, 5))
    result_label.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E), pady=10)


    # Binds for hitting enter:
    initial_entry.bind("<Return>", calc)
    rate_entry.bind("<Return>", calc)
    years_entry.bind("<Return>", calc)

    # Event loop:
    root.geometry("300x250")
    root.mainloop()