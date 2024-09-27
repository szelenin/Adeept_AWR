import Adafruit_PCA9685 # Import the library used to communicate with PCA9685

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

#servo 2 - shoulder in almost open position (horizontal back) at 500
pwm.set_pwm(2, 0, 400) # ~45 degrees turned back
pwm.set_pwm(3, 0, 350) # ~60 degrees to shoulder
pwm.set_pwm(4, 0, 150) # ~100 degrees to elbow
pwm.set_pwm(5, 0, 300) # ~palm parallel to ground
pwm.set_pwm(6, 0, 250) # ~palm wide open
