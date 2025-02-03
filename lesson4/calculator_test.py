import pytest
from lesson4.calculator import Calculator
calculator = Calculator()
@pytest.mark.parametrize ('num1,num2,result', [(4,5,9), (-6, -10, -16), (-6,6,0), (5.61,4.39,10), (10,0,10)])
def testsumnums (num1,num2,result):
    calculator = Calculator()
    res= calculator.sum(num1,num2)
    assert res == result


@pytest.mark.parametrize ('nums,result',[([],0),([1,2,3,4,5,6,7,8,9,5],5)])
def testavglist (nums,result):
    calculator=Calculator()
    numbers= []
    res = calculator.avg (nums)
    assert res==result

# def testavg_positive ():
#     calculator=Calculator()
#     numbers= [1,3,5,7,8]
#     res = calculator.avg (numbers)
#     assert res ==4.8

# res= testCalculator.avg(numbers)
# print (res)
# assert (res==5)


def testdiv ():
    calculator = Calculator ()
    res= calculator.div(15,5)
    assert (res==3)

def testdivnol ():
    calculator = Calculator ()
    with pytest.raises (ArithmeticError):
        calculator.div(15,0)
