#importo las biblitecas para los LEDS y el time sleep#
from gpiozero import LED
from time import sleep

#declaro las variables para los LEDS#
ledv = LED (13)
ledr = LED (19)
leda = LED (26)

#declaro un bucle para la secuencia de encendido de los LEDS#
while True:
 
#declaro la secuencia de encendido del LED rojo (se enciende 1 sg)
	ledr.on()
	sleep(1)
	ledr.off()

#declaro la secuencia de encendido del LED azul (se enciende 0.5 sg)
	leda.on()
	sleep(0.5)
	leda.off()

#declaro la secuencia de encendido del LED verde (se enciende 0.25 sg)
	ledv.on()
	sleep(0.25)
	ledv.off()

