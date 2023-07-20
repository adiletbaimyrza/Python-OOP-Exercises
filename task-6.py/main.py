import datetime


'''
6. Import the built-in datetime module and display the namespace of this module (sorted alphabetically) as
given below.

Tip: Use the _dict_ attribute of the datetime module.

Expected result:
MAXYEAR
MINYEAR
_builtlns_
_cached_
_doc_
_file_
_loader_
_name_
_package_
_spec_
date
datetime
datetime_CAPI
sys
time
timedelta
timezone
tzinfo
'''
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