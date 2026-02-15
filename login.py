import ui
import console

class LoginView(ui.View):
	def __init__(self):
		self.background_color = '#ffffff'
		self.name = 'Accesso Registro'
		label = ui.Label(frame=(0, 100, 400, 40))
		label.text = "Inserire PIN Studente"
		label.alignment = ui.ALIGN_CENTER
		self.add_subview(label)
		self.entry = ui.TextField(frame=(100, 150, 200, 32))
		self.entry.placeholder = "PIN"
		self.add_subview(self.entry)
		btn = ui.Button(title="Verifica")
		btn.frame = (150, 200, 100, 40)
		btn.action = self.check
		self.add_subview(btn)

	def check(self, sender):
		# Usiamo console.alert per evitare l'errore rosso che avevi visto
		if self.entry.text == "1234":
			console.alert("Successo", "PIN Corretto!", "OK", hide_cancel_button=True)
		else:
			console.alert("Errore", "PIN Sbagliato!", "Riprova", hide_cancel_button=True)
