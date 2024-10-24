from converter_gui import ConverterGuiApp
import tkinter as tk

bases = {
    "Binary": 2,
    "Octal": 8,
    "Decimal": 10,
    "Hexadecimal": 16
}

def getAns(original, base):
    if(base == 2):
        return bin(original)
    if(base == 8):
        return oct(original)
    if(base == 10):
        return original
    if(base == 16):
        return hex(original)

def definitive():

    baseUm = bases[app.combobox_base1.get()] 
    baseDois = bases[app.combobox_base2.get()]
    
    dec = int(app.entry_num.get(), base = baseUm)

    result = getAns(dec, baseDois)
    
    if(baseDois != 10):
        result = result[2:]

    app.message_result.configure(text=f"{result}")

    app.message_result.grid(column=0, row=9)

if __name__ == "__main__":
    #SETTING A FUNCTION TO THE GUI BUTTON AND RUNNING THE APP
    app = ConverterGuiApp()
    app.button_convert.configure(command=definitive)
    app.run()
