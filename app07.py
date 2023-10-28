"""Aplicacion de escirtorio que pregunta el nombre de una persona y lo muestre en pantalla"""

from guizero import App, Text, PushButton, TextBox
#App es un widget
#Progrmacion orientada a eventos

def nombre():
    app.info("Suma", text=f"La suma es {int(num_1.value) + int(num_2.value)}")



app = App(title="ICI App")

message_1=Text(app, text="Ingresa uno numeros", color="pink")
num_1 = TextBox(app, width=20)
message_2=Text(app, text="Ingresa otro numeros", color="pink")
num_2 = TextBox(app, width=20)

button=PushButton(app, text="Sumar",command=nombre)

app.display()