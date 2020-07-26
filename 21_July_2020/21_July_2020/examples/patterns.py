def left_centered_triangle(width):

    for x in range(width+1):
        for y in range(width+1):
            if x>=y:
                print("* ",end="")
            else:
                pass
        print()

def right_centered_triangle(width):
    for x in range(width+1):
        for y in range(width+1):
            #print("width",width)
            #print("x",x)
            #print("y",y)
            if x+y >= width:
                print("X\t",end="")
            else:
                print("\t",end="")
        print(end="\n")

def mid_centered_triangle(width):
    for x in range(width+1):
        for y in range(width+1):
            #print("width",width)
            #print("x",x)
            #print("y",y)
            if x+y >= width:
                print("X ",end="")
            else:
                print(" ",end="")
        print(end="\n")

input_width=int(input("Enter triangle width"))
left_centered_triangle(input_width)

print("-------------------------------")
right_centered_triangle(input_width)

print("-------------------------------")
mid_centered_triangle(input_width)