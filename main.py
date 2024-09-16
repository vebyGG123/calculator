from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty



class Calculator(MDBoxLayout):
	uzmenenia_label = ObjectProperty()

	def button_0(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "0"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "0"


	def button_1(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "1"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "2"

	def button_2(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "2"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "2"


	def button_3(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "3"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "3"


	def button_4(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "4"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "4"

	def button_5(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "5"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "5"

	def button_6(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "6"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "6"

	def button_7(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "7"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "7"

	def button_8(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "8"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "8"

	def button_9(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "9"
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "9"

	
	def button_clear(self):
		self.uzmenenia_label.text = "0"

	def button_floatchange(self):
		if self.uzmenenia_label.text == "0" or self.uzmenenia_label.text[0] == "О":
			self.uzmenenia_label.text = "."
		else:
			self.uzmenenia_label.text = self.uzmenenia_label.text + "."

	def button_otvet(self):
		# if self.uzmenenia_label.text[0] == "√":
		# 	otvet = int(self.uzmenenia_label[1:]) ** -
		try:
			otvet = eval(self.uzmenenia_label.text)
			self.uzmenenia_label.text = f"Ответ: {otvet}"

		except Exception:
			self.uzmenenia_label.text = "Ошибка!"

	def button_plus(self):
		self.uzmenenia_label.text = self.uzmenenia_label.text + "+"
	
	def button_minus(self):
		self.uzmenenia_label.text = self.uzmenenia_label.text + "-"

	def button_ymnosh(self):
		self.uzmenenia_label.text = self.uzmenenia_label.text + "*"

	def button_delenua(self):
		self.uzmenenia_label.text = self.uzmenenia_label.text + "/"

	def button_stepen(self):
		self.uzmenenia_label.text = self.uzmenenia_label.text + "**"

	def button_corren(self):
		otvet = int(self.uzmenenia_label.text) ** 0.5

		self.uzmenenia_label.text = f"Ответ: {otvet}"



class MyApp(MDApp):
	def build(self) -> Calculator:
		return Calculator()


if __name__ == "__main__":
	MyApp().run()
