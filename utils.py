# utils.py
#ECE444 Assignment 1: Activity 4 - Nicholas Heeralal

class Utils:
    @staticmethod
    def reversed(number):
        if isinstance(number, int):
            return int(str(number)[::-1])
        else:
            raise Exception("Exception, reversed method did not recieve an int")

    @staticmethod
    def formatter(number):
        if isinstance(number, int):
            return {
                "binary": bin(number),
                "octal": oct(number),
            }
        else:
            raise Exception("Exception, formatter method did not recieve an int")