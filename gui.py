# -*- coding: utf-8 -*-

try: 
    from tkinter import *

except ImportError:
    try:
        os.system("pip install Tkinter")
    except:
        print("No s'ha detectat Tkinter en el sistema, s'ha intentat instal·lar i no ha sigut possible. Instala'l manualment")
        exit()
        
import math

window = Tk()

"""
f = Frame(window, bg="green", width="100", height="100")
f.grid(column=0, row= 0)
text = Label(f, text="TEST FRAME", font=("Agency FB", 40), bg="green")
"""

h = 700
w = 250
window.geometry('{}x{}'.format(h, w))
window.title("Cosinus, sinus i tangents")
window.iconbitmap("icono.ico")

txt = Label(window, text="Operacions trigonomètriques", font=("Agency FB", 40))
# txt.grid(column=0, row=0)
txt.pack()
window.columnconfigure(0, weight=1) # Centrar altura
# window.rowconfigure(0, weight=1)  # Centrar d'esquerra a dreta

txt2 = Label(window, text="\nGrau", font=("Arial", 15))
# txt2.grid(column=0, row=1)
txt2.pack()
grau = Entry(window, width="10")
# grau.place(x=440, y=100)
# grau.grid(column=0, row=2)
grau.pack()

def clicked():
	try:
		num = int(grau.get())
	except ValueError:
		try:
			num = grau.get()
			num = num.replace(",",".")
			num = float(num)

		except ValueError:
			error = Label(window, text="Recorda que els graus tenen que estar en format sexagesimal!", font=("Arial", 15), bg="red")
			# error.place(x=225, y= 175)
			# error.grid(column=0, row=4)
			error.pack()

	# num = float(grau.get())
	rad = math.radians(num)
	sin = math.sin(rad)
	cos = math.cos(rad)
	tan = math.tan(rad)

	rad = round(rad, 10)
	sin = round(sin, 10)
	cos = round(cos, 10)
	tan = round(tan, 10)

	result = Tk()
	height2 = 400
	weight2 = 120
	result.geometry("{}x{}".format(height2, weight2))
	result.title("Operacions trigonomètrics de "+ str(num) +"°")
	# radians = "Aixo es igual a: "+ str(rad)
	# txt2.configure(text=radians)

	radians = Label(result, text=("Radians: %s" % rad), font=("Arial", 15))
	sinus = Label(result, text=("Sinus: %s" % sin), font=("Arial", 15))
	cosinus = Label(result, text=("Cosinus: %s" % cos), font=("Arial", 15))
	tangent = Label(result, text=("Tangent: %s" % tan), font=("Arial", 15))

	radians.pack()
	sinus.pack()
	cosinus.pack()
	tangent.pack()


bot_calc = Button(window, text="Calcular", command=clicked, height="1")
# bot_calc.place(x=510, y=100)
# bot_calc.grid(column=0, row=3)
bot_calc.pack()

# rad = math.radians(num_int)
# sin = math.sin(rad)
# print(sin)
window.mainloop()
