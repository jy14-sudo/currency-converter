import tkinter as tk

class Currency:
    def __init__(self, root):

        
        self.geld = {
            "Euro": 1,
            "Yen": 185,
            "Schwedische Kronen": 10.6
        }

        self.root = root
        self.root.title("Enter your currency to convert")

        self.label = tk.Label(root, text="Currency:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Convert", command=self.umrechnen)
        self.button.pack(pady=5)

        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def umrechnen(self):
        eingabe = self.entry.get()

        if eingabe in self.geld:
            kurs = self.geld[eingabe]
            self.output_label.config(text=f"1 Euro is {kurs} {eingabe}")
        else:
            self.output_label.config(text="Currency not found!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()