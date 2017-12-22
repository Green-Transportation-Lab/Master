# EES_Class

class EES:
    name = ""
    capacity = 0 #kwh 
    c_ready = 0 # 0 = not ready, 1 = ready
    c_rate = 0 # kW
    d_ready = 0 # 0 = not ready, 1 = ready
    max_temp = 25 #C
    pack_voltage = 0
    timestep = 1
    cur_capacity = 0
    n_capacity = 310
    current = 0 # Amps, positive for charging, negative for discharge
    power = pack_voltage*current/1000 = 0 # kW, positive for charging, negative for discharging
    
        
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
        if self.power > 0:
            print("%s is charging at %dkW" % (self.name, self.c_rate))
        if self.power < 0:
            print("%s is discharging at %dkW" % (self.name, self.d_rate))
        print("%s Maximum Temperature is %d (Celcuis)" %(self.name, self.avg_temp))
        print("%s Pack Voltage is %d \n" % (self.name, self.pack_voltage))
                  
        return 0
    
     #use max temp
    def temp_check(self):
        if self.max_temp > 30:
            self.c_ready = 0
            self.d_ready = 0
        return 0 # return some error code
    
    def voltage_check(self):
        if self.pack__voltage < 300 or self.pack_voltage > 450:
            self.c_ready = 0
            self.d_ready = 0
        return 0 # return some error code

    def SOC_calc(self):
        self.cur_capacity = self.capacity
        self.capacity = self.cur_capacity + self.power*self.timestep/3600
        self.SOC = self.capacity/self.n_capacity

    
    
    #Maybe Check here if there are any error codes associated with EES and send error to user

    #If no error codes and no temp and voltage problems, set self.c_ready and self.d_ready to 1

    #Archive All Data
