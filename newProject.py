from itertools import count
from warnings import catch_warnings

from numpy.ma.core import append

first_name = "Tirtha Bepary"

split_name = first_name.split(" ")

print(split_name)

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10,4))
print(df.head())
print(df.tail())
strr = "python is the wrost lagyage"
print(strr.replace("wrost","Best"))

count = 0
ster3 = "Tirtha is the best student in DIU . DIU id one of the best University in the World DIU students are alowes best,so DIU is best"
list1 =[]
str6 = ster3.split(" ")
print(str6)
tap = (1,2,3,4,5)
print(type(tap))

list3 = ["a","e","i","o","u"]
str7 = "this is a good Student he lives in Dhaka"

for s in str7:
    for i in list3:
        if i == s:
            count += 1
print(count)
print(f"the number of valowel is {count}")
for i in str7:
    if(i!=" "):
        list1.append(i)

print(len(list1))
numb_of_con = len(list1)-count
print(numb_of_con)
list2 = [5,6,7,8]
list1 = [5,6,1,2]


set1 = set(list1)
set2 = set(list2)
print(set1.intersection(set2))


dict1 ={
    "Tirtha":[1,2,3,4,5],
    "Best":2,
    "DIU":3,


}
dict2={
        "Tirtha":[1,2,3,4,5],
      "  Best":2,
        "DIU":3,
}
dict2.update({"key2":6})
print(dict2)

del dict2["DIU"]
print(dict2)
dict2.pop("key2")
print(dict2)
print(dict2.values())
print(dict2.keys())


for key,value in dict2.items():
    print(key,value)





















