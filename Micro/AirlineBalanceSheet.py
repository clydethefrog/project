import sys

sys.path.insert(0, '/Users/markmroz/Desktop/project/Micro')

from enum import Enum
from collections import namedtuple
from BalanceSheetType import BalanceSheetType
	
"""
Enum

Income statement keys for the Airline
----------
AirCanada : BalanceSheetType("AC", "{'account1' => 1'}")
"""

class AirlineBalanceSheet(Enum):
	
    AirCanada = BalanceSheetType("AC", "{'account1' => 1'}")

 