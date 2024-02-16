# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:10:43 2024

@author: nhopk
"""

#@todo payroll calculator
    #get name and hours and rate,
    #calc overtime or not,
    #and 14% tax
   
    
from functools import wraps
    

def getInput():
    name = input("Yeah, see... The boss he wants to know your name, see...") #1940s gangster
    

def calculateGross(hours, rate):
    pass

def deductTaxes(gross, tax_bracket):
    pass

def printCheck(net, name):
    pass


def logger(func):
    @wraps(func)
    def logging(*args, **kwargs):
        with open("payroll.log", "a") as log:
            log.write("just ran the "+ func.func_name + "function. \n")
        return func(*args, **kwargs)
    return logging





if __name__ == "__main__":
    pass