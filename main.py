from project import Macro
from project.calculation_runner import CalculationRunner

def main():

    stock_ticker = "AC"

    macro_calculation = Macro.calculate_tourism(stock_ticker)
    micro_calculation = 0
    news_calculation = 0
    CalculationRunner.simple_calculation(macro_calculation, micro_calculation, news_calculation)

if __name__ == '__main__':
    main()