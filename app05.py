"""Aplicacion de escirtorio que pregunta el nombre de una persona y lo muestre en pantalla"""

from guizero import App, Text, PushButton, TextBox
#App es un widget
#Progrmacion orientada a eventos

app = App(title="ICI App")

message=Text(app, text="¿Como te llamas?")
message_2 = TextBox(app)
#button=PushButton(app, text="Click me!",command=say_hello)

app.display()
