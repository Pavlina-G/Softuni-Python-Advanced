class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative

# -------------------------------------------

# class ValueCannotBeNegative(Exception):
#     pass
#
#
# values = [int(input()) for _ in range(5)]
#
# for value in values:
#     if value < 0:
#         raise ValueCannotBeNegative(f'{value} should be >= 0')
