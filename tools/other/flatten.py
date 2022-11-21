from typing import Union, List, Tuple, Set


def flatten(arr: Union[List, Tuple, Set]):
    arr = list(arr)
    try:
        for i, val in enumerate(arr):
            while isinstance(val, (list, set, tuple)):
                arr[i:i+1] = val
                val = arr[i]
    except IndexError:
        pass
    return arr


if __name__ == "__main__":
    print(flatten([[132131], {13213}, [123213, 112313, [13213, 1231313, [7, 4]]]]))