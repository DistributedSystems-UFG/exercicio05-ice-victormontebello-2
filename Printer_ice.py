# -*- coding: utf-8 -*-

import Ice, IcePy

# Start of module Demo
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

_M_Demo._t_Printer = IcePy.defineValue('::Demo::Printer', Ice.Value, -1, (), False, True, None, ())
_M_Demo._t_Calculator = IcePy.defineValue('::Demo::Calculator', Ice.Value, -1, (), False, True, None, ())

if 'PrinterPrx' not in _M_Demo.__dict__:
    _M_Demo.PrinterPrx = Ice.createTempClass()
    class PrinterPrx(Ice.ObjectPrx):

        def printString(self, s, context=None):
            return _M_Demo.Printer._op_printString.invoke(self, ((s,), context))

        def printStringAsync(self, s, context=None):
            return _M_Demo.Printer._op_printString.invokeAsync(self, ((s,), context))

        def begin_printString(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_printString.begin(self, ((s,), _response, _ex, _sent, context))

        def end_printString(self, _r):
            return _M_Demo.Printer._op_printString.end(self, _r)

        def toUpper(self, s, context=None):
            return _M_Demo.Printer._op_toUpper.invoke(self, ((s,), context))

        def toUpperAsync(self, s, context=None):
            return _M_Demo.Printer._op_toUpper.invokeAsync(self, ((s,), context))

        def begin_toUpper(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_toUpper.begin(self, ((s,), _response, _ex, _sent, context))

        def end_toUpper(self, _r):
            return _M_Demo.Printer._op_toUpper.end(self, _r)

        def stringLength(self, s, context=None):
            return _M_Demo.Printer._op_stringLength.invoke(self, ((s,), context))

        def stringLengthAsync(self, s, context=None):
            return _M_Demo.Printer._op_stringLength.invokeAsync(self, ((s,), context))

        def begin_stringLength(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_stringLength.begin(self, ((s,), _response, _ex, _sent, context))

        def end_stringLength(self, _r):
            return _M_Demo.Printer._op_stringLength.end(self, _r)

        def repeat(self, s, times, context=None):
            return _M_Demo.Printer._op_repeat.invoke(self, ((s, times), context))

        def repeatAsync(self, s, times, context=None):
            return _M_Demo.Printer._op_repeat.invokeAsync(self, ((s, times), context))

        def begin_repeat(self, s, times, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_repeat.begin(self, ((s, times), _response, _ex, _sent, context))

        def end_repeat(self, _r):
            return _M_Demo.Printer._op_repeat.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.PrinterPrx.ice_checkedCast(proxy, '::Demo::Printer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.PrinterPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'

    _M_Demo._t_PrinterPrx = IcePy.defineProxy('::Demo::Printer', PrinterPrx)
    _M_Demo.PrinterPrx = PrinterPrx
    del PrinterPrx

    _M_Demo.Printer = Ice.createTempClass()
    class Printer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Printer', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Printer'

        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'

        def printString(self, s, current=None):
            raise NotImplementedError("servant method 'printString' not implemented")

        def toUpper(self, s, current=None):
            raise NotImplementedError("servant method 'toUpper' not implemented")

        def stringLength(self, s, current=None):
            raise NotImplementedError("servant method 'stringLength' not implemented")

        def repeat(self, s, times, current=None):
            raise NotImplementedError("servant method 'repeat' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_PrinterDisp)

        __repr__ = __str__

    _M_Demo._t_PrinterDisp = IcePy.defineClass('::Demo::Printer', Printer, (), None, ())
    Printer._ice_type = _M_Demo._t_PrinterDisp

    Printer._op_printString = IcePy.Operation('printString', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Printer._op_toUpper = IcePy.Operation('toUpper', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    Printer._op_stringLength = IcePy.Operation('stringLength', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    Printer._op_repeat = IcePy.Operation('repeat', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0)), (), ((), IcePy._t_string, False, 0), ())

    _M_Demo.Printer = Printer
    del Printer

if 'CalculatorPrx' not in _M_Demo.__dict__:
    _M_Demo.CalculatorPrx = Ice.createTempClass()
    class CalculatorPrx(Ice.ObjectPrx):

        def add(self, a, b, context=None):
            return _M_Demo.Calculator._op_add.invoke(self, ((a, b), context))

        def addAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_add.invokeAsync(self, ((a, b), context))

        def begin_add(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_add.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_add(self, _r):
            return _M_Demo.Calculator._op_add.end(self, _r)

        def multiply(self, a, b, context=None):
            return _M_Demo.Calculator._op_multiply.invoke(self, ((a, b), context))

        def multiplyAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_multiply.invokeAsync(self, ((a, b), context))

        def begin_multiply(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_multiply.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_multiply(self, _r):
            return _M_Demo.Calculator._op_multiply.end(self, _r)

        def describe(self, context=None):
            return _M_Demo.Calculator._op_describe.invoke(self, ((), context))

        def describeAsync(self, context=None):
            return _M_Demo.Calculator._op_describe.invokeAsync(self, ((), context))

        def begin_describe(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_describe.begin(self, ((), _response, _ex, _sent, context))

        def end_describe(self, _r):
            return _M_Demo.Calculator._op_describe.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.CalculatorPrx.ice_checkedCast(proxy, '::Demo::Calculator', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.CalculatorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Calculator'

    _M_Demo._t_CalculatorPrx = IcePy.defineProxy('::Demo::Calculator', CalculatorPrx)
    _M_Demo.CalculatorPrx = CalculatorPrx
    del CalculatorPrx

    _M_Demo.Calculator = Ice.createTempClass()
    class Calculator(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Calculator', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Calculator'

        @staticmethod
        def ice_staticId():
            return '::Demo::Calculator'

        def add(self, a, b, current=None):
            raise NotImplementedError("servant method 'add' not implemented")

        def multiply(self, a, b, current=None):
            raise NotImplementedError("servant method 'multiply' not implemented")

        def describe(self, current=None):
            raise NotImplementedError("servant method 'describe' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_CalculatorDisp)

        __repr__ = __str__

    _M_Demo._t_CalculatorDisp = IcePy.defineClass('::Demo::Calculator', Calculator, (), None, ())
    Calculator._ice_type = _M_Demo._t_CalculatorDisp

    Calculator._op_add = IcePy.Operation('add', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), (), ((), IcePy._t_int, False, 0), ())
    Calculator._op_multiply = IcePy.Operation('multiply', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), (), ((), IcePy._t_int, False, 0), ())
    Calculator._op_describe = IcePy.Operation('describe', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_string, False, 0), ())

    _M_Demo.Calculator = Calculator
    del Calculator

# End of module Demo
