import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def toUpper(self, s, current=None):
        return s.upper()

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
        return "Calculator object ready"

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
calculator = CalculatorI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))
adapter.activate()

communicator.waitForShutdown()
