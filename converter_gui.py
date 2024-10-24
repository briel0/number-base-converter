import tkinter as tk
import tkinter.ttk as ttk

class ConverterGuiApp:
    def __init__(self, master=None):
        """
        BUILD GUI
        """
        # SETTING TOPLEVEL
        self.toplevel = tk.Tk() if master is None else tk.Toplevel(master)

        # CONFIGURING THE WINDOW
        self.toplevel.geometry("200x250")

        self.toplevel.configure(padx=5, pady=5)

        self.toplevel.resizable(False, False)

        # SETTING A TITLE
        self.title = tk.Label(self.toplevel)

        self.title.configure(justify="center", text='System Converter')

        self.title.grid(column=0, row=0)

        # NUMBER ENTRY
        self.label_enternum = ttk.Label(self.toplevel)

        self.label_enternum.configure(text='Enter number')

        self.label_enternum.grid(column=0, row=1, sticky="w")

        self.entry_num = ttk.Entry(self.toplevel)

        self.entry_num.configure(width=22)

        self.entry_num.grid(column=0, pady=5, row=2)

        # BASE ENTRY 1
        self.label_frombase = ttk.Label(self.toplevel)

        self.label_frombase.configure(text='From base:')

        self.label_frombase.grid(column=0, row=3, sticky="w")

        self.combobox_base1 = ttk.Combobox(
            self.toplevel, values=["Binary", "Octal", "Decimal", "Hexadecimal"])

        self.combobox_base1.set("Decimal")

        self.combobox_base1.grid(column=0, pady=5, row=4)

        # BASE ENTRY 2
        self.label_tobase = ttk.Label(self.toplevel)

        self.label_tobase.configure(text='To base:')

        self.label_tobase.grid(column=0, row=5, sticky="w")

        self.combobox_base2 = ttk.Combobox(
            self.toplevel, values=["Binary", "Octal", "Decimal", "Hexadecimal"])

        self.combobox_base2.set("Binary")

        self.combobox_base2.grid(column=0, row=6)

        # BUTTON
        self.button_convert = ttk.Button(self.toplevel)

        self.button_convert.configure(text='Convert!')

        self.button_convert.grid(column=0, pady=5, row=7)

        # RESULT LABEL
        self.label_result = ttk.Label(self.toplevel)

        self.label_result.configure(text='Result:')

        self.label_result.grid(column=0, row=8)

        self.toplevel.grid_anchor("center")

        self.message_result = tk.Message(self.toplevel, width = 1000)

        # MAIN WIDGET
        self.mainwindow = self.toplevel

    def run(self):
        """
        RUN GUI
        """
        self.mainwindow.mainloop()
