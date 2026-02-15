import ui

class LoginView(ui.View):
    def __init__(self):
        self.background_color = '#ffffff'
        self.name = 'Accesso Registro'
        
        self.label = ui.Label(frame=(0, 100, 400, 40))
        self.label.text = "Inserire PIN Studente"
        self.label.alignment = ui.ALIGN_CENTER
        self.add_subview(self.label)
        
        self.entry = ui.TextField(frame=(100, 150, 200, 32))
        self.entry.placeholder = "PIN"
        self.add_subview(self.entry)
        
        self.btn = ui.Button(title="Verifica")
        self.btn.frame = (150, 200, 100, 40)
        self.btn.action = self.check
        self.add_subview(self.btn)
        
    def check(self, sender):
        # Qui metteremo la logica del PIN dopo
        if self.entry.text == "1234":
            ui.alert("PIN Corretto")
        else:
            ui.alert("PIN Errato")
