import sys
name = input("Enter name a")
print(name)

print(name, sep=' ', end='', file=sys.stdout, flush=True)