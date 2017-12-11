import pandas as pd

# Do not change this function name and inputs
def infos(callback_input: dict, raw_data: pd.DataFrame, filtered_data: pd.DataFrame) -> list:
    """
    Receives the callback input and return a list of dicts.

    The callback_input is a dict that contains the information set by the user using the components. The key is the
    data-title given at config.py and the value can be a int/float/str/tuple, depending on the component.

    The dictionary containing the information has the following structure:
    {'name' : 'Mean: ',
     'value': int/float/str}

    Note that the order of the info in this list is the same order that it is going to be
    shown on the screen.

    :param callback_input:
    :return: list of dicts
    """



    return

# Do not change this line
output = {'infos': infos}

if __name__ == '__main__':
    pass
