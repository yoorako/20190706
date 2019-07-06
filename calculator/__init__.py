from calculator.model import CalculatorModel
import os

if __name__ == '__main__':
    calc = CalculatorModel()

    if not os.path.exists('saved_add_model/checkpoint'):
        calc.create_add_model()
    if not os.path.exists('saved_sub_model/checkpoint'):
        calc.create_sub_model()

    if not os.path.exists('saved_mul_model/checkpoint'):
        calc.create_mul_model()

    if not os.path.exists('saved_div_model/checkpoint'):
        calc.create_div_model()