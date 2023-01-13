import tkinter as tk
import tkinter.ttk as ttk

class ConverterGuiApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel = tk.Tk() if master is None else tk.Toplevel(master)

        self.toplevel.configure(padx=5, pady=5)

        self.toplevel.resizable(False, False)

        self.title = tk.Label(self.toplevel)

        self.title.configure(justify="center", text='System Converter')

        self.title.grid(column=0, row=0)

        self.label_enternum = ttk.Label(self.toplevel)

        self.label_enternum.configure(text='Enter number')

        self.label_enternum.grid(column=0, row=1, sticky="w")

        self.entry_num = ttk.Entry(self.toplevel)

        self.entry_num.configure(width=22)

        self.entry_num.grid(column=0, pady=5, row=2)

        self.label_frombase = ttk.Label(self.toplevel)

        self.label_frombase.configure(text='From base:')

        self.label_frombase.grid(column=0, row=3, sticky="w")

        self.combobox_base1 = ttk.Combobox(
            self.toplevel, values=["Binary", "Octal", "Decimal", "Hexadecimal"])

        self.combobox_base1.set("Decimal")

        self.combobox_base1.grid(column=0, pady=5, row=4)

        self.label_tobase = ttk.Label(self.toplevel)

        self.label_tobase.configure(text='To base:')

        self.label_tobase.grid(column=0, row=5, sticky="w")

        self.combobox_base2 = ttk.Combobox(
            self.toplevel, values=["Binary", "Octal", "Decimal", "Hexadecimal"])

        self.combobox_base2.set("Binary")

        self.combobox_base2.grid(column=0, row=6)

        self.button_convert = ttk.Button(self.toplevel)

        self.button_convert.configure(text='Convert!')

        self.button_convert.grid(column=0, pady=5, row=7)

        self.label_result = ttk.Label(self.toplevel)

        self.label_result.configure(text='Result:')

        self.label_result.grid(column=0, row=8)

        # Main widget
        self.mainwindow = self.toplevel

    def run(self):
        self.mainwindow.mainloop()
