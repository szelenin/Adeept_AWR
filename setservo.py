import Adafruit_PCA9685 # Import the library used to communicate with PCA9685

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

pwm.set_pwm(1, 0, int((540 + 72) / 2)) # range is between 72 and 539