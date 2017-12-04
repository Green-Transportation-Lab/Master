# Master

import time
import EES_Class
import Gen_class
import Load_class

battery1 = EES_Class.EES() #battery1 is defined as class EES

#The following modifys defining elements of the object
battery1.name = "Battery 1"
battery1.SOC = .45
battery1.capacity = 200
battery1.avg_temp = 25
battery1.c_rate = 0
battery1.t = 1


#As can be seen above, elements within battery1 were modified,
#Those modifications can be evidenced by pring the function below


battery1.description()

battery1.c_ready = 1
battery1.c_rate = 90

battery1.description()


while battery1.SOC < .90:
    battery1.description()
    battery1.SOC_calc()
    time.sleep(battery1.t)

