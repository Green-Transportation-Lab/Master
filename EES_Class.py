# EES_Class


class EES:
    name = ""
    capacity = 0 #kwh 
    c_ready = 0 # 0 - not ready, 1 - ready
    c_rate = 0
    d_ready = 0 # 0 - not ready, 1 - ready
    d_rate = 0
    avg_temp = 25 #C
    pack_voltage = 0
    t = 1
    cur_cap = 0
    n_cap = 310
     
    def description(self): #When called, this function enters defined values into a string
        print("EES Name = %s" % (self.name))
        print("SOC = %.2f" % (self.SOC))
        print("Capacity = %.2f" % (self.capacity))
        if self.c_ready == 1:
            print("Charge Ready")
        else:
            print("Charge Not Ready")
        if self.d_ready == 1:
            print("Discharge Ready")
        else:
            print("Discharge Not Ready")
        if self.c_rate > 0:
            print("%s is charging at %d" % (self.name, self.c_rate))
        if self.d_rate > 0:
            print("%s is discharging at %d" % (self.name, self.d_rate))
        print("%s Average Temperature is %d" %(self.name, self.avg_temp))
        print("%s Pack Voltage is %d \n" % (self.name, self.pack_voltage))\
                  
        return 0
    
     #use max temp
    def temp_check(self):
        if self.avg_temp > 30:
            self.c_ready = 0
            self.d_ready = 0
        return 0 # return some error code
    
    def voltage_check(self):
        if self.pack__voltage < 300 or self.pack_voltage > 450:
            self.c_ready = 0
            self.d_ready = 0
        return 0 # return some error code

    def SOC_calc(self):
        self.cur_cap = self.capacity
        self.capacity = self.cur_cap + self.c_rate*self.t/3600
        self.SOC = self.capacity/self.n_cap

    
    
    #Maybe Check here if there are any error codes associated with EES and send error to user

    #If no error codes and no temp and voltage problems, set self.c_ready and self.d_ready to 1

    #Archive All Data
