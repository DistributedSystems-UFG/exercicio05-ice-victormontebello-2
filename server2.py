import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def __init__(self, t):
        self.t = t
        
    def printString(self, s, current=None):
        print(self.t, s)

    def toUpper(self, s, current=None):
        return f"{self.t} {s.upper()}"

    def stringLength(self, s, current=None):
        return len(s)

    def repeat(self, s, times, current=None):
        return s * max(0, times)


class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

    def multiply(self, a, b, current=None):
        return a * b

    def describe(self, current=None):
        return "Calculator from server2 ready"

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
calculator = CalculatorI()
adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))
adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))
adapter.activate()

communicator.waitForShutdown()
