"""Aplicacion de escirtorio que pregunta el nombre de una persona y lo muestre en pantalla"""

from guizero import App, Text, PushButton, TextBox
#App es un widget
#Progrmacion orientada a eventos

def nombre():
    #message_2.value="Hola "+ name.value
    #app.info("Mensaje", "Hola " + name.value)
    app.info("Saludo", text =f"Hola {name.value}")



app = App(title="ICI App")

message=Text(app, text="¿Como te llamas?", color="pink")
name = TextBox(app, width=30, multiline=True)
message_2 = Text(app, color="purple")

button=PushButton(app, text="Click me!",command=nombre)

app.display()
