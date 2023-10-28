from guizero import App, Text, PushButton
#App es un widget

app = App(title="ICI App")
message=Text(app, text="Welcome to the ICI App!")

button=PushButton(app, text=("Click me!"))

app.display()
