#!/usr/bin/env python
"""
HAL interface to labjack cards, only counter is implemented on the FIO4 pin and it is
not synchronized with filming.
"""
import numpy

import storm_control.hal4000.halLib.halMessage as halMessage

import storm_control.sc_hardware.baseClasses.hardwareModule as hardwareModule
import storm_control.sc_hardware.labjack.labjack_u3 as ljcontrol

import storm_control.sc_library.hdebug as hdebug
import storm_control.sc_library.halExceptions as halExceptions


class LabjackModuleException(halExceptions.HardwareException):
    pass


class LabjackFunctionality(hardwareModule.HardwareFunctionality):

    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.am_filming = False
        self.task = None
        
    def setFilming(self, start):
        pass




class CTTaskFunctionality(LabjackFunctionality):
    """
    Counter output.
    """
    def __init__(self, duty_cycle = None, **kwds):
        super().__init__(**kwds)
        self.duty_cycle = duty_cycle
        
    def pwmOutput(self, duty_cycle = 0.5, cycles = 0):
        if self.task is not None:
            self.task.stopPWM()
            self.task.shutDown()
            self.task = None
            
        if (duty_cycle > 0.0):
            self.task = ljcontrol.PWM()
            self.task.startPWM(duty_cycle*100)
            

class LabjackModule(hardwareModule.HardwareModule):

    def __init__(self, module_params = None, qt_settings = None, **kwds):
        super().__init__(**kwds)
        
        configuration = module_params.get("configuration")

        # Create functionalities we will provide, these are all Daq tasks.        
        self.daq_fns = {}
        for fn_name in configuration.getAttrs():

            task = configuration.get(fn_name)
            for task_name in task.getAttrs():
                task_params = task.get(task_name)
            
                daq_fn_name = ".".join([self.module_name, fn_name, task_name])
                if (task_name == "ct_task"):
                    task = CTTaskFunctionality(duty_cycle = task_params.get("duty_cycle"))
                else:
                    raise LabjackModuleException("Unknown task type", task_name)
                
                self.daq_fns[daq_fn_name] = task

    
    def processMessage(self, message):
        if message.isType("get functionality"):
            self.getFunctionality(message)
    
    def filmTiming(self, message):
        pass
            
    def getFunctionality(self, message):
        daq_fn_name = message.getData()["name"]
        if daq_fn_name in self.daq_fns:
            message.addResponse(halMessage.HalMessageResponse(source = self.module_name,
                                                              data = {"functionality" : self.daq_fns[daq_fn_name]}))
        
    def stopFilm(self, message):
        pass
