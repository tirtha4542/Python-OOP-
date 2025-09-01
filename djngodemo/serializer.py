from collections import Counter,namedtuple,OrderedDict

str = "aaaaavvvvbbbbcccc"
str2 = Counter(str)
print(str2.keys())

li1 = ["tirtha","is" ,"a","good","boy"]
str3 = " ".join(li1)
print(str3)
point = namedtuple("point","x,y")
pt = point(2,-5)
print(pt)
