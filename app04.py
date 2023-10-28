from guizero import App, Text, PushButton
#App es un widget
#Progrmacion orientada a eventos

def say_hello():
    message_2.value="Ici Rocks!"


app = App("ICI App")

message=Text(app, text="Welcome to the ICI App!")
message_2 = Text(app)
button=PushButton(app, text="Click me!",command=say_hello)

app.display()
