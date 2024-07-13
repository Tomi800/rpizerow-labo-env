from gpiozero import PWMLED
import ADS1x15
import time
import math

#pin de I2C y el registro
ADS = ADS1x15.ADS1115(1,0x48)
#modo que usa
ADS.setMode(ADS.MODE_SINGLE)
#ganancia ADC +-6.144V
ADS.setGain(ADS.PGA_4_096V)
#convierte el valor del adc en un valor de voltaje
factor = ADS.toVoltage()

#pines 26 y 19 (LEDs rojo y azul)
blue = PWMLED(26)
red = PWMLED(19)

#variables para el calculo de temperatura
vcc = 3.3
vrt = 0
rt = 0
t = 0
r = 10000
AuTe = 3977

while True :

	#el ADC lee el pin 3 (potenciometro) y el pin 1 (termistor)
	Pval = ADS.readADC(3)
	Tval = ADS.readADC(1)
	#multiplica los anteriores valores obtenidos por el factor de incremento del ADC.
	PvalV = Pval * factor
	TvalV = Tval * factor

	#calculo de la temperatura 
	vrt = (3.3*TvalV)/4095
	rt = r/((vcc/vrt)-1)
	t = AuTe/(math.log10(rt/r)+(AuTe/298.0))
	t = t - 273.15
	
##seguir el ejercicio en clase (falta completar)##