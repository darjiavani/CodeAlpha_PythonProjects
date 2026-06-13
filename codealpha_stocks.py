import tkinter as tk
from tkinter import ttk, messagebox
import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 170
}

portfolio = []
total_investment = 0

def add_stock():
    global total_investment

    stock = stock_var.get().upper()

    if stock not in stock_prices:
        messagebox.showerror("Error", "Invalid Stock Symbol!")
        return

    try:
        qty = int(quantity_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid quantity!")
        return

    value = stock_prices[stock] * qty
    total_investment += value

    portfolio.append([stock, qty, stock_prices[stock], value])

    tree.insert("", tk.END,
                values=(stock, qty,
                        stock_prices[stock], value))

    total_label.config(
        text=f"Total Investment: ${total_investment}"
    )

    quantity_entry.delete(0, tk.END)

def save_csv():
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Investment"]
        )

        writer.writerows(portfolio)

    messagebox.showinfo(
        "Success",
        "Portfolio saved as portfolio.csv"
    )

root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("750x500")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="📈 STOCK PORTFOLIO TRACKER",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="#00ffcc"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

tk.Label(
    frame,
    text="Stock:",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10)

stock_var = tk.StringVar()
stock_box = ttk.Combobox(
    frame,
    textvariable=stock_var,
    values=list(stock_prices.keys())
)
stock_box.grid(row=0, column=1)

tk.Label(
    frame,
    text="Quantity:",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
).grid(row=0, column=2, padx=10)

quantity_entry = tk.Entry(frame)
quantity_entry.grid(row=0, column=3)

tk.Button(
    frame,
    text="Add Stock",
    command=add_stock,
    bg="#00cc99",
    fg="white",
    font=("Arial", 11, "bold")
).grid(row=0, column=4, padx=10)

columns = ("Stock", "Qty", "Price", "Investment")

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=20)

total_label = tk.Label(
    root,
    text="Total Investment: $0",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="#ffff66"
)
total_label.pack()

tk.Button(
    root,
    text="Save Portfolio",
    command=save_csv,
    bg="#3366ff",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=15)

root.mainloop()