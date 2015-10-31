# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:54:02 2015
The abstract measurement class for Baja Electrical
@author: Glenn
"""

from abc import ABCMeta

# Abstract class for a measurement
# Reads raw data from the system, may perform some filtering
# Retunrn refined measurements
class BajaMeasurement:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def systemRead():
        """Reads the raw measurement values from the hardware."""
        return
    
    @abstractmethod
    def update():
        """Updates the filtered measurements and returns the current value."""
    
    @abstractmethod
    def save():
        """"Saves the raw and updated measurements to a csv file."""