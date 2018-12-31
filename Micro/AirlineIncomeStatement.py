import sys

sys.path.insert(0, '/Users/markmroz/Desktop/project/Micro/IncomeStatement')

from enum import Enum
from collections import namedtuple
from IncomeStatementType import IncomeStatementType
	
"""
Enum

Income statement keys for the Airline
----------
AirCanada : IncomeStatementType("AC", "{'account1' => 1'}")
"""

class AirlineIncomeStatement(Enum):
	
    AirCanada = IncomeStatementType("AC", "{'account1' => 1'}")

 