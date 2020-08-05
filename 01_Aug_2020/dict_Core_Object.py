dict1  = {"id":101,"name":"Sumit","salary":5000}
dict2 =  {"id":102,"name":"Diviz","salary":15000}

dictList = [dict1,dict2]
print("Extracted ",dictList[0]["id"])

print(dict2.pop("id"))
print(dictList)

print(dict1["id"])
print(dict1.get("id"))

##list of dictionaries


##
x=(1,2,3)
y=("one","two","three")

dict1 = dict.fromkeys(x,y)
print(dict1)

dict1.update({1:"updated"})
print(dict1)

y =dict1.setdefault(6,"TWO")
print(dict1)