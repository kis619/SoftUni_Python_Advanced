class ValueCannotBeNegative(Exception):
    """Does shit"""
    pass


class ValueTooSmallError(ValueCannotBeNegative):
    """Raised when the input value is too small""" #### TODO


for i in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative


