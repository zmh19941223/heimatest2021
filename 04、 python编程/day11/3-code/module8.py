# import my_pack1
# my_pack1.m1.m1_func()
# my_pack1.m1.m1_test()
# my_pack1.m2.m2_func()
from my_pack1.m1 import m1_test
from my_pack1.m1 import m1_func
from my_pack1.m2 import m2_func
m1_test()
m1_func()
m2_func()
