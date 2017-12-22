# Master

# Master is a place that runs all the programs and sub-programs

# 1) Importing the classes

import time
import EES_Class
import Gen_class
import Load_class

# 2) Creating Instances of EES_Classes ==> "battery1" is our object

battery1 = EES_Class.EES() #battery1 is defined as EES_Class

# 2.1) Setting the properties for "battery1"
# the properties are called "fields"

battery1.name = "Battery 1"
battery1.SOC = 0.45
battery1.capacity = 200 #kWh
battery1.avg_temp = 25 #degree C
battery1.amp = 0.2 # Real Time Current in amps (Charging is -, Discharge is +)
battery1.timestep = 1 #timestep in second



#As can be seen above, fields within battery1 were modified,
#Those modifications can be evidenced by printing the "Method" below

# 3) Calling "Methods" 
# "Method" is a function inside a class

# 3.1) Calling "description" Method
# This Method will prints all the current "Fields" which are the State of the Battery

battery1.description()

# 3.2) Changing the properties and printing

battery1.c_ready = 1 # it has been defiend in EES-Class
battery1.current = 90
battery1.pack_voltage = 400

battery1.description()

# Test SoC Calculator

while battery1.SOC < .90:
    battery1.description()
    battery1.SOC_calc()
    time.sleep(battery1.timestep)


