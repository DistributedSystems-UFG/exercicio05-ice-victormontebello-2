import sys, Ice
import Demo
 
with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 11000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    printer.printString("Hello World!")
    print("Upper:", printer.toUpper("hello ice"))
    print("Length:", printer.stringLength("hello ice"))
    print("Repeat:", printer.repeat("ice-", 3))

    calculator_base = communicator.stringToProxy("SimpleCalculator:default -p 11000")
    calculator = Demo.CalculatorPrx.checkedCast(calculator_base)
    if not calculator:
        raise RuntimeError("Invalid calculator proxy")

    print("Calculator description:", calculator.describe())
    print("2 + 5 =", calculator.add(2, 5))
    print("3 * 4 =", calculator.multiply(3, 4))
