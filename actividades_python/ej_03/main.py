from gpiozero import LED 
from gpiozero import Buzzer 
rgb_red = LED (19)
rgb_green = LED (13) 
rgb_blue = LED (26) 
Buzzer = Buzzer (22) 

while True:

	prompt = input ("Prompt: ")
	#declaro a prompt como una entrada para pedir datos al usuario# 

	if (prompt == "buzz on"):
		Buzzer.on()
	#si el usuario declara 'buzz on' se encenderá el buzzer#

	if prompt == ("buzz off"):
		Buzzer.off()
	#si el usuario declara 'buzz off' se apagará el buzzer#

	if prompt == ("rgb red"):
		rgb_red.on()
	#si el usuario declara 'rgb red' se encenderá el led#

	if prompt == ("rgb green"):
		rgb_green.on()
	#si el usuario declara 'rgb green' se encenderá el led verde#

	if prompt == ("rgb blue"):
		rgb_blue.on()
	#si el usuario declara 'rgb blue' se encenderá el led azul#

	if prompt == ("rgb off"):
		rgb_red.off()
		rgb_green.off()
		rgb_blue.off()
	#si el usuario declara 'rgb off' se apagarán el o los leds encendidos#


	
