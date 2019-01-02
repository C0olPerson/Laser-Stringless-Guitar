from gpiozero import LightSensor
class Guitar_String(object):
    def __init__(self,receiver):
        self.__receiver = receiver.light_detected()
    def getReceiver(self):
        return self.__receiver

class EL_String(Guitar_String):
    def __init__(self):
        super().__init__(reciever)
class A_String(Guitar_String):
    def __init__(self):
        super().__init__(reciever)
class D_String(Guitar_String):
    def __init__(self):
        super().__init__(reciever)
class G_String(Guitar_String):
    def __init__(self):
        super().__init__(reciever)
class B_String(Guitar_String):
    def __init__(self):
        super().__init__(reciever)
class EH_String(Guitar_String):
    def __init__(self):
        super().__init__(reciever)


    
