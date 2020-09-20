#
# DSA Final Assessment Question 4 - HashTest.py
#
# Name : 
# ID   :
#
# 
from DSAHashTable import *

tab = DSAHashTable(20)
data = ["11111112", "11111121", "11111211", "11112111", "11121111", "11211111", "12111111", "21111111"]
print("Table size is: " + str(tab.getArrayLength()) )

for i in range (0, len(data)):
	tab.put(data[i], "O"+data[i])	

tab.display()
print("Load Factor is: " + str(tab.getLoadFactor()) )