############################################################################
# CalCul Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

import math

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/09/17'

class DoCalCul():
    def __init__(self):
        self.list = []
        self.dummy = []

# Calculation functions
    def docalcul(self, list):
        self.list = list

        while "" in self.list:
            self.list.remove("")

        while len(self.list) != 1:
            status = self.onecalcul()
            if self.find_next():
                pass

            if status != True:
                return "ERROR1" , status

        return str(self.list[0])

    def onecalcul(self):
        index = 0
        for item in self.list:
            if item == "+":
                try:
                    temp_result = self.addition(float(self.list[index - 1]), float(self.list[index + 1]))
                    del self.list[index - 1 : index + 2]
                    self.list.insert(0, temp_result)
                except:
                    return False
                else:
                    return True

            elif item == "-":
                try:
                    temp_result = self.subtraction(float(self.list[index - 1]), float(self.list[index + 1]))
                    del self.list[index - 1 : index + 2]
                    self.list.insert(0, temp_result)
                except:
                    return False
                else:
                    return True

            elif item == "*":
                try:
                    temp_result = self.multiplication(float(self.list[index - 1]), float(self.list[index + 1]))
                    del self.list[index - 1 : index + 2]
                    self.list.insert(0, temp_result)
                except Exception as e:
                    return e
                else:
                    return True

            elif item == "/":
                try:
                    temp_result = self.division(float(self.list[index - 1]), float(self.list[index + 1]))
                    del self.list[index - 1 : index + 2]
                    self.list.insert(0, temp_result)
                except:
                    return False
                else:
                    return True

            elif item == "sqrt":
                try:
                    temp_result = self.sqrt(float(self.list[index + 1]))
                    del self.list[index : index + 2]
                    self.list.insert(0, temp_result)
                except:
                    return False
                else:
                    return True

            index += 1
        return True

    def find_next(self):
        try:
            if self.list[1] and self.list[2] != "0123456789.000":
                self.dummy.append(self.list[0], self.list[1])
                del self.list[0], self.list[1]
        except:
            pass
        else:
            return True

# operation functions
    def addition(self, num1, num2):
        return  num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2

    def sqrt(self, num):
        return math.sqrt(num)