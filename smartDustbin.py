import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 17
GPIO_ECHO = 27
GPIO_SERVO = 22
GPIO_LED = 5

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_SERVO, GPIO.OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)

p = GPIO.PWM(22,50)
p.start(2.61)

def distance():
	GPIO.output(GPIO_TRIGGER, True)

	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2

	return distance

if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print ("jarak = %.1dcm" % (dist))
			time.sleep(0.2)
			if dist < 20:
				p.ChangeDutyCycle(8.7)
				GPIO.output(GPIO_LED,GPIO.HIGH)
				print("MASUKKAN SAMPAH")
				time.sleep(2)

			else:
				p.ChangeDutyCycle(2.61)
				GPIO.output(GPIO_LED,GPIO.LOW)
				time.sleep(0.0001)

	except KeyboardInterrupt:
		print("stop")
		GPIO.cleanup()
