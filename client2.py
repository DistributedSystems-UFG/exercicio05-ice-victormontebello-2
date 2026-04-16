import sys, Ice
import Demo
 
with Ice.initialize(sys.argv) as communicator:
    base1 = communicator.stringToProxy("SimplePrinter1:default -p 11000")
    base2 = communicator.stringToProxy("SimplePrinter2:default -p 11000")
    printer1 = Demo.PrinterPrx.checkedCast(base1)
    printer2 = Demo.PrinterPrx.checkedCast(base2)
    if (not printer1) or (not printer2):
        raise RuntimeError("Invalid proxy")

    printer1.printString("Hello World from printer1!")
    printer2.printString("Hello World from printer2!")
    print("printer1 upper:", printer1.toUpper("distributed systems"))
    print("printer2 length:", printer2.stringLength("distributed systems"))
    print("printer1 repeat:", printer1.repeat("ice ", 2))

    calculator_base = communicator.stringToProxy("SimpleCalculator:default -p 11000")
    calculator = Demo.CalculatorPrx.checkedCast(calculator_base)
    if not calculator:
        raise RuntimeError("Invalid calculator proxy")

    print("Calculator:", calculator.describe())
    print("10 + 20 =", calculator.add(10, 20))
    print("6 * 7 =", calculator.multiply(6, 7))
