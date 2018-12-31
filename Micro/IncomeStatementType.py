import typing
from collections import namedtuple

class IncomeStatementType(typing.NamedTuple):
    """
    Attributes
    ----------
    name : str
        name of the airline on the statement
    revenue : str
        {key => row number}
    """
    name: str
    column_keys: hash