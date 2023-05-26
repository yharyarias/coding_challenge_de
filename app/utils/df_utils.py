def fillStr(column, default_val=''):
    """
    Fill missing values in a string column with a default value.

    column: The column to fill missing values.
    default_val: The default value to use.

    Returns:
    The column with missing values filled.

    """
    column = fillDefault(column, default_val)
    return column

def fillInt(column, default_val=0, set_int=False):
    """
    Fill missing values in an integer column with a default value.

    column: The column to fill missing values.
    default_val: The default value to use.
    set_int: Flag to convert the column to integer.

    Returns:
    The column with missing values filled.

    """
    column = fillDefault(column, default_val)
    if set_int == True:
        column = setIntColumn(column)
    return column

def fillDefault(column, default_val):
    """
    Fill missing values in a column with a default value.

    column: The column to fill missing values.
    default_val: The default value to use.

    Returns:
    The column with missing values filled.

    """
    column = column.fillna(default_val)
    return column

def setIntColumn(column):
    """
    Convert a column to integer data type.

    column: The column to convert to integer.

    Returns:
    The column converted to integer.

    """
    column = column.astype(int)
    return column