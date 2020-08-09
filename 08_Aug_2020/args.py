def add(*args):
    for x in args:
        print(x)

add(2,3,4,5)


print("-----------------")
import sys
listvalues = sys.argv[1]
scriptname = sys.argv[0]
sum = int()

print("Script :",scriptname)
for x in range(1,len(sys.argv)):
    print(f"Number {x} :" ,sys.argv[x])
    sum += int(sys.argv[x])

print("sum ",sum)

add(sys.argv[1:len(sys.argv)])