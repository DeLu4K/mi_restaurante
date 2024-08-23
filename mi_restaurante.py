from tkinter import *
import random, datetime
from tkinter import filedialog, messagebox

operador = ""
precios_comida = [1.32, 1.69, 2.31, 3.22, 1.99, 2.05, 2.65, 5.50]
precios_bebida = [0.25, 0.99, 1.23, 1.08, 1.10, 2.00, 1.58, 2.00]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            txt_comida[x].set("0")
        x += 1

    x = 0
    for b in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            txt_bebida[x].set("0")
        x += 1

    x = 0
    for p in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            txt_postres[x].set("0")
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in txt_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in txt_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in txt_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.21
    total = sub_total + impuestos

    var_coste_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_coste_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_coste_postres.set(f"$ {round(sub_total_postres, 2)}")
    var_coste_subtotal.set(f"$ {round(sub_total, 2)}")
    var_coste_impuesto.set(f"$ {round(impuestos, 2)}")
    var_coste_total.set(f"$ {round(total, 2)}")


def recibo():
    txt_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    txt_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    txt_recibo.insert(END, f"*" * 67 + "\n")
    txt_recibo.insert(END, "Items\t\tCant.\tCoste Items\n")
    txt_recibo.insert(END, f"-" * 80 + "\n")

    x = 0
    for comida in txt_comida:
        if comida.get() != "0":
            txt_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t"
                                   f"$ {int(comida.get()) * precios_comida[x]}\n")
        x += 1

    x = 0
    for bebida in txt_bebida:
        if bebida.get() != "0":
            txt_recibo.insert(END, f"{lista_bebida[x]}\t\t{bebida.get()}\t"
                                   f"$ {int(bebida.get()) * precios_bebida[x]}\n")
        x += 1
    x = 0
    for postres in txt_postres:
        if postres.get() != "0":
            txt_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t"
                                   f"$ {int(postres.get()) * precios_postre[x]}\n")
        x += 1

    txt_recibo.insert(END, f"-" * 80 + "\n")
    txt_recibo.insert(END, f"Coste de la comida: \t\t\t{var_coste_comida.get()}\n")
    txt_recibo.insert(END, f"Coste de la bebida: \t\t\t{var_coste_bebida.get()}\n")
    txt_recibo.insert(END, f"Coste de los postres: \t\t\t{var_coste_postres.get()}\n")
    txt_recibo.insert(END, f"-" * 80 + "\n")
    txt_recibo.insert(END, f"Sub-Total: \t\t\t{var_coste_subtotal.get()}\n")
    txt_recibo.insert(END, f"Impuestos: \t\t\t{var_coste_impuesto.get()}\n")
    txt_recibo.insert(END, f"Total: \t\t\t{var_coste_total.get()}\n")
    txt_recibo.insert(END, f"*" * 67 + "\n")
    txt_recibo.insert(END, "Le esperamos pronto")


def guardar():
    info_recibo = txt_recibo.get(1.0, END)
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    file.write(info_recibo)
    file.close()
    messagebox.showinfo("Información", "Su recibo ha sido guardado")


def resetear():
    txt_recibo.delete(0.1, END)
    for txt in txt_comida:
        txt.set("0")
    for txt in txt_bebida:
        txt.set("0")
    for txt in txt_postres:
        txt.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for var in variables_comida:
        var.set(0)
    for var in variables_bebida:
        var.set(0)
    for var in variables_postres:
        var.set(0)

    var_coste_comida.set("")
    var_coste_bebida.set("")
    var_coste_postres.set("")
    var_coste_subtotal.set("")
    var_coste_impuesto.set("")
    var_coste_total.set("")


# iniciar tkinter
app = Tk()

# tamaño de la ventana
app.geometry("1080x630+0+0")

# evitar maximizar
app.resizable(0, 0)

# encabezado
app.title("Mi restaurante - Sistema de facturación")

# color de fondo de la ventana
app.config(bg="burlywood")

# panel superior
panel_superior = Frame(app, border=2, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta título
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4",
                        font=("Dosis", 30), bg="burlywood", width=46)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(app, border=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT, padx=5)

# panel costos
panel_costos = Frame(panel_izquierdo, border=1, relief=FLAT, bg="azure4", padx=40, pady=10)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 15, "bold"), border=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT, padx=5)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 15, "bold"), border=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT, padx=5)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 15, "bold"), border=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT, padx=5)

# panel derecha
panel_derecha = Frame(app, border=1, relief=FLAT)
panel_derecha.pack(side=RIGHT, padx=10)

# panel calculadora
panel_calculadora = Frame(panel_derecha, border=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack(pady=10)

# panel recibo
panel_recibo = Frame(panel_derecha, border=1, relief=FLAT, bg="burlywood")
panel_recibo.pack(pady=10)

# panel botones
panel_button = Frame(panel_derecha, border=1, relief=FLAT)
panel_button.pack(pady=10)

# lista de productos
lista_comidas = ["pollo", "cerdo", "cordero", "kebab", "salmon", "pizza", "atun", "pasta"]
lista_bebida = ["agua", "soda", "zumo", "cola", "vino", "cerveza", "cerveza2", "limonada"]
lista_postres = ["helado", "fruta", "brownie", "flan", "mousse", "pastel", "pastel2", "puding"]

# generar items comida
variables_comida = []
cuadros_comida = []
txt_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbuttons
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 15, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append("")
    txt_comida.append("")
    txt_comida[contador] = StringVar()
    txt_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=("Dosis", 14, "bold"),
                                     border=1,
                                     width=4,
                                     state=DISABLED,
                                     textvariable=txt_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
txt_bebida = []
contador = 0
for bebida in lista_bebida:
    # crear checkbuttons
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=("Dosis", 15, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append("")
    txt_bebida.append("")
    txt_bebida[contador] = StringVar()
    txt_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 14, "bold"),
                                     border=1,
                                     width=4,
                                     state=DISABLED,
                                     textvariable=txt_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
txt_postres = []
contador = 0
for postres in lista_postres:
    # checkbuttons
    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=("Dosis", 15, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear los cuadros de entrada
    cuadros_postres.append("")
    txt_postres.append("")
    txt_postres[contador] = StringVar()
    txt_postres[contador].set("0")
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=("Dosis", 14, "bold"),
                                      border=1,
                                      width=4,
                                      state=DISABLED,
                                      textvariable=txt_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1

# variables
var_coste_comida = StringVar()
var_coste_bebida = StringVar()
var_coste_postres = StringVar()
var_coste_subtotal = StringVar()
var_coste_impuesto = StringVar()
var_coste_total = StringVar()

# etiquetas de costes y campos de entrada
etiqueta_coste_comida = Label(panel_costos,
                              text="Coste Comida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_coste_comida.grid(row=0,
                           column=0)

txt_coste_comida = Entry(panel_costos,
                         font=("Dosis", 12, "bold"),
                         border=1,
                         width=10,
                         state="readonly",
                         textvariable=var_coste_comida)
txt_coste_comida.grid(row=0,
                      column=1,
                      padx=20)


# etiquetas de costes y campos de entrada
etiqueta_coste_bebida = Label(panel_costos,
                              text="Coste Bebida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_coste_bebida.grid(row=1,
                           column=0)

txt_coste_bebida = Entry(panel_costos,
                         font=("Dosis", 12, "bold"),
                         border=1,
                         width=10,
                         state="readonly",
                         textvariable=var_coste_bebida)
txt_coste_bebida.grid(row=1,
                      column=1,
                      padx=20)


# etiquetas de costes y campos de entrada
etiqueta_coste_postres = Label(panel_costos,
                               text="Coste Postres",
                               font=("Dosis", 12, "bold"),
                               bg="azure4",
                               fg="white")
etiqueta_coste_postres.grid(row=2,
                            column=0)

txt_coste_postres = Entry(panel_costos,
                          font=("Dosis", 12, "bold"),
                          border=1,
                          width=10,
                          state="readonly",
                          textvariable=var_coste_postres)
txt_coste_postres.grid(row=2,
                       column=1,
                       padx=20)


# etiquetas de costes y campos de entrada
etiqueta_coste_subtotal = Label(panel_costos,
                                text="Subtotal",
                                font=("Dosis", 12, "bold"),
                                bg="azure4",
                                fg="white")
etiqueta_coste_subtotal.grid(row=0,
                             column=2)

txt_coste_subtotal = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           border=1,
                           width=10,
                           state="readonly",
                           textvariable=var_coste_subtotal)
txt_coste_subtotal.grid(row=0,
                        column=3,
                        padx=20)


# etiquetas de costes y campos de entrada
etiqueta_coste_impuesto = Label(panel_costos,
                                text="Impuestos",
                                font=("Dosis", 12, "bold"),
                                bg="azure4",
                                fg="white")
etiqueta_coste_impuesto.grid(row=1,
                             column=2)

txt_coste_impuesto = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           border=1,
                           width=10,
                           state="readonly",
                           textvariable=var_coste_impuesto)
txt_coste_impuesto.grid(row=1,
                        column=3,
                        padx=20)


# etiquetas de costes y campos de entrada
etiqueta_coste_total = Label(panel_costos,
                             text="Total",
                             font=("Dosis", 12, "bold"),
                             bg="azure4",
                             fg="white")
etiqueta_coste_total.grid(row=2,
                          column=2)

txt_coste_total = Entry(panel_costos,
                        font=("Dosis", 12, "bold"),
                        border=1,
                        width=10,
                        state="readonly",
                        textvariable=var_coste_total)
txt_coste_total.grid(row=2,
                     column=3,
                     padx=20)


# botones
botones = ["Total", "Recibo", "Guardar", "Resetear"]
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_button,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=8)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas,
               padx=1)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area del recibo
txt_recibo = Text(panel_recibo,
                  font=("Dosis", 12, "bold"),
                  bd=1,
                  width=45,
                  height=10)
txt_recibo.grid(row=0,
                column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("Dosis", 16, "bold"),
                          width=34,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ["7", "8", "9", "+",
                       "4", "5", "6", "-",
                       "1", "2", "3", "x",
                       "=", "Borrar", "0", "/"]

botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=("Dosis", 16, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=8)
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna,
               padx=2, pady=2)

    columna += 1
    if columna == 4:
        fila += 1
        columna = 0

botones_guardados[0].config(command=lambda: click_boton("7"))
botones_guardados[1].config(command=lambda: click_boton("8"))
botones_guardados[2].config(command=lambda: click_boton("9"))
botones_guardados[3].config(command=lambda: click_boton("+"))
botones_guardados[4].config(command=lambda: click_boton("4"))
botones_guardados[5].config(command=lambda: click_boton("5"))
botones_guardados[6].config(command=lambda: click_boton("6"))
botones_guardados[7].config(command=lambda: click_boton("-"))
botones_guardados[8].config(command=lambda: click_boton("1"))
botones_guardados[9].config(command=lambda: click_boton("2"))
botones_guardados[10].config(command=lambda: click_boton("3"))
botones_guardados[11].config(command=lambda: click_boton("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton("0"))
botones_guardados[15].config(command=lambda: click_boton("/"))

# evitar que la pantalla se cierre
app.mainloop()
