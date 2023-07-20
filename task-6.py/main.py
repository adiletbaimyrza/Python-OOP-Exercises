import datetime


class Solution:
    def output_result():
        [print(key) for key  in datetime.__dict__]

Solution.output_result()


'''
output:

__name__
__doc__
__package__
__loader__
__spec__
__file__
__cached__
__builtins__
__all__
sys
MINYEAR
MAXYEAR
timedelta
date
tzinfo
time
datetime
timezone
datetime_CAPI
'''