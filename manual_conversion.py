from converter_gui import ConverterGuiApp
import tkinter as tk

def to_decimal():
    num = app.entry_num.get()
    sis_entrada = app.combobox_base1.get()
    base_value = 0
    definitive_value = 0
    position = 0

    if (sis_entrada == "Binary"):
        base_value = 2
    elif (sis_entrada == "Octal"):
        base_value = 8
    elif (sis_entrada == "Hexadecimal"):
        base_value = 16
    
    if base_value == 0:
        definitive_value = int(num)
    else:
        for sequence in range(len(num), 0, -1):
            prov = num[position]
            value_prov = 0
            if prov in "ABCDEF":
                if (prov == "A"):
                    value_prov = 10
                elif (prov == "B"):
                    value_prov = 11
                elif (prov == "C"):
                    value_prov = 12
                elif (prov == "D"):
                    value_prov = 13
                elif (prov == "E"):
                    value_prov = 14
                elif (prov == "F"):
                    value_prov = 15
            else:
                value_prov = int(prov)

            definitive_value = definitive_value + (value_prov * (base_value ** (sequence - 1)))
            position += 1

    return definitive_value                

def to_binary():
    num = to_decimal()
    list_1 = []

    while (num != 0):
        prov = int(num % 2)
        list_1.append(str(prov))
        if (num % 2 == 0):
            num = num / 2
        elif (num % 2 != 0):
            num = (num / 2) - 0.5

    content = str("".join(list_1))
    return int(content[::-1])     

def to_octal():
    num = to_decimal()
    list_1 = []

    while (num >= 8):
        prov = num % 8
        list_1.append(str(prov))
        num = num // 8
        
    list_1.append(str(num))
    content = str("".join(list_1))
    return content[::-1]

def to_hexa():
    num = to_decimal()
    list_1 = []

    while (num >= 16):
        prov = num % 16
        if (prov == 10):
            list_1.append("A")
        elif (prov == 11):
            list_1.append("B")
        elif (prov == 12):
            list_1.append("C")
        elif (prov == 13):
            list_1.append("D")
        elif (prov == 14):
            list_1.append("E")
        elif (prov == 15):
            list_1.append("F")
        else:
            list_1.append(str(prov))

        num = num // 16

    list_1.append(str(num))
    content = str("".join(list_1))
    return content[::-1]

def definitive_function():
    tipo_saida = app.combobox_base2.get()
    if (tipo_saida == "Decimal"):
        result = to_decimal()
    elif (tipo_saida == "Binary"):
        result = to_binary()
    elif (tipo_saida == "Octal"):
        result = to_octal()
    elif (tipo_saida == "Hexadecimal"):
        result = to_hexa()

    app.message_result = tk.Message(app.toplevel)

    app.message_result.configure(text=result)

    app.message_result.grid(column=0, row=9)

if __name__ == "__main__":
    app = ConverterGuiApp()
    app.button_convert.configure(command=definitive_function)
    app.run()