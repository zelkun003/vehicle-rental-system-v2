
import tkinter as tk
from tkinter import messagebox


class VehicleRental:
    def __init__(self, customer_name, vehicle_type, rental_days, daily_rate):
        self.customer_name = customer_name
        self.vehicle_type = vehicle_type
        self.rental_days = rental_days
        self.daily_rate = daily_rate

    def calculate_total(self):
        return self.rental_days * self.daily_rate

    def get_summary(self):
        total_cost = self.calculate_total()

        return (
            "=== RENTAL SUMMARY ===\n\n"
            f"Customer: {self.customer_name}\n"
            f"Vehicle Type: {self.vehicle_type}\n"
            f"Rental Days: {self.rental_days}\n"
            f"Daily Rate: ₱{self.daily_rate:.2f}\n"
            f"Total Cost: ₱{total_cost:.2f}"
        )


def calculate_rental():
    try:
        customer = customer_entry.get().strip()
        vehicle = vehicle_entry.get().strip()
        days = int(days_entry.get())
        rate = float(rate_entry.get())

        if not customer or not vehicle:
            messagebox.showerror(
                "Input Error", "Enter customer and vehicle names."
            )
            return

        if days <= 0 or rate < 0:
            messagebox.showerror(
                "Input Error",
                "Days must be positive and rate cannot be negative."
            )
            return

        rental = VehicleRental(customer, vehicle, days, rate)

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, rental.get_summary())

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter a whole number for days and a valid rate."
        )


root = tk.Tk()
root.title("Vehicle Rental System - Python OOP")
root.geometry("430x520")
root.resizable(False, False)

tk.Label(
    root, text="VEHICLE RENTAL SYSTEM",
    font=("Arial", 16, "bold")
).pack(pady=15)


def create_field(label_text):
    tk.Label(root, text=label_text, font=("Arial", 10)).pack()
    entry = tk.Entry(root, width=35)
    entry.pack(pady=5)
    return entry


customer_entry = create_field("Customer Name")
vehicle_entry = create_field("Vehicle Type")
days_entry = create_field("Rental Days")
rate_entry = create_field("Daily Rate (₱)")

tk.Button(
    root,
    text="Calculate Rental",
    command=calculate_rental,
    bg="lightblue",
    width=22
).pack(pady=12)

result_text = tk.Text(root, height=9, width=42)
result_text.pack(pady=8)

root.mainloop()
