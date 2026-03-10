import tkinter as tk
from tkinter import ttk

rates = {
    "Euro": 1.0,
    "Yen": 160,
    "Schwedische Kronen": 11.2,
    "Bosnische Mark": 1.95583,
    "Türkische Lira": 35
}
def convert():
    amount = float(entry.get())
    from_currency = from_box.get()
    to_currency = to_box.get()

    euro = amount / rates[from_currency]
    result = euro * rates[to_currency]

    result_label.config(text=str(round(result,2)) + " " + to_currency)

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Betrag").pack()
entry = tk.Entry(root)
entry.pack()

from_box = ttk.Combobox(root, values=list(rates.keys()))
from_box.pack()
from_box.current(0)

to_box = ttk.Combobox(root, values=list(rates.keys()))
to_box.pack()
to_box.current(1)

tk.Button(root, text="Umrechnen", command=convert).pack()

result_label = tk.Label(root, text="Ergebnis")
result_label.pack()

root.mainloop()