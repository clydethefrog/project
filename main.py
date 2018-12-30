from Macro import Macro
from Airline import Airline
from calculation_runner import CalculationRunner

def main():

    stock_ticker = "AC"

    air_canada = Airline("AC", "Air Canada")
    macro_calculation = Macro.perform_discount_cash_flow_analysis(air_canada)
    micro_calculation = 0
    news_calculation = 0
    CalculationRunner.simple_calculation(macro_calculation, micro_calculation, news_calculation)

if __name__ == '__main__':
    main()