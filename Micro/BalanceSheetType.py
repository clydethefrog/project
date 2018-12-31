import typing
from collections import namedtuple

class BalanceSheetType(typing.NamedTuple):
    """
    Attributes
    ----------
    name : str
        name of the airline on the statement
    revenue : str
        {key => row number} representing the row name and the row index
    """
    name: str
    column_keys: hash