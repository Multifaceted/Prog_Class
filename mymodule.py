def concatenate(str1, str2):
    return str1 + str2


# Python assigns to the special variable
# __name__ the value "__main__" 
# only when the file is executed as a script
# (e.g. from a terminal with `python mymodule.py`
# or in a jupyter notebook ẁith `%run mymodule.py`)
if __name__ == "__main__":
    print("Testing module...")
    # assert raises an error if the expression is False
    assert concatenate('a','b') == 'ab' 
    print("... tests passed!")