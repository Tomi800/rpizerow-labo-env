from gpiozero import LED, Button
from signal import pause

#importo librerias para los pines GPIO (LED, botón)y libreria para pause 
 
led = LED(26)
button = Button(18)

#declaro variables para el LED y el botón

button.when_pressed = led.on
button.when_released = led.off

#declaro las condiciones, cuando presiono el botón, se enciende el LED y cuando no se presione, el LED no se enciende

pause()
