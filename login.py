import ui
import console

class LoginView(ui.View):
	def __init__(self):
		# Sfondo scuro per stile Onion
		self.background_color = '#1a1a1a' 
		self.name = 'Onion System Login'
		
		# Calcoliamo il centro dello schermo
		w, h = ui.get_screen_size()
		
		# Etichetta centrata
		self.label = ui.Label()
		self.label.frame = (0, h/2 - 100, w, 40)
		self.label.text = "SISTEMA CRIPTATO - INSERIRE PIN"
		self.label.text_color = '#00ff00'
		self.label.alignment = ui.ALIGN_CENTER
		self.label.font = ('<system-bold>', 18)
		self.add_subview(self.label)
		
		# Campo PIN centrato con gli asterischi *
		self.entry = ui.TextField()
		self.entry.frame = (w/2 - 100, h/2 - 40, 200, 40)
		self.entry.placeholder = "PIN"
		self.entry.background_color = '#ffffff'
		self.entry.alignment = ui.ALIGN_CENTER
		self.entry.keyboard_type = ui.KEYBOARD_NUMBER_PAD
		# Questa riga mette gli asterischi * mentre scrivi
		self.entry.secure_text_entry = True 
		self.add_subview(self.entry)
		
		# Bottone centrato
		self.btn = ui.Button(title="ACCEDI")
		self.btn.frame = (w/2 - 50, h/2 + 30, 100, 45)
		self.btn.background_color = '#00ff00'
		self.btn.tint_color = '#1a1a1a'
		self.btn.corner_radius = 10
		self.btn.action = self.check
		self.add_subview(self.btn)
		
	def check(self, sender):
		# Usiamo il tuo PIN salvato 5381
		if self.entry.text == "5381":
			self.close() 
			console.hud_alert("Accesso Onion VPN...", "success")
		else:
			console.alert("ACCESSO NEGATO", "PIN non autorizzato.", "Riprova", hide_cancel_button=True)

# Avvio
v = LoginView()
v.present('fullscreen', hide_title_bar=True)
