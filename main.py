import sys

sys.path.insert(0, '/Users/markmroz/Desktop/project/Macro')
sys.path.insert(0, '/Users/markmroz/Desktop/project/Model')
sys.path.insert(0, '/Users/markmroz/Desktop/project/Micro')
sys.path.insert(0, '/Users/markmroz/Desktop/project/Model/Airline')

from Macro import Macro
from Airline import Airline
from AirlineIncomeStatement import AirlineIncomeStatement
from AirlineBalanceSheet import AirlineBalanceSheet
from calculation_runner import CalculationRunner

def main():

    stock_ticker = "AC"


    # Or stand alone 
    # Replace air_canada = Airline("AC", "Air Canada", AirlineIncomeStatement.AirCanada)
    # with IncomeStatementType("Delta", "{'account1' => 1'}")

    air_canada = Airline("AC", "Air Canada", AirlineIncomeStatement.AirCanada, AirlineBalanceSheet.AirCanada) 
    macro_calculation = Macro.perform_discount_cash_flow_analysis(air_canada)
    micro_calculation = 0
    news_calculation = 0
    CalculationRunner.simple_calculation(macro_calculation, micro_calculation, news_calculation)

if __name__ == '__main__':
    main()