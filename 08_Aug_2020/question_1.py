# Complete the plusMinus function below.
def plusMinus(arr):
    total_digits = len(arr)
    positive_digits = int()
    negative_digits = int()
    zeroes = arr.count(0)
    for x in arr:
        if x > 0:
            positive_digits += 1
        elif x < 0:
            negative_digits += 1
        else:
            pass

    # print(f"positive_digits in arr {arr} is {positive_digits}")
    # print(f"negative_digits in arr {arr} is {negative_digits}")

    positive_ratio = positive_digits/total_digits
    negative_ratio = negative_digits/total_digits

    print("{:.8f}".format(positive_ratio))
    print("{:.8f}".format(negative_ratio))
    print("{:.8f}".format(zeroes/total_digits))


##Driver code
n = int(input())
arr = list(map(int, input().rstrip().split()))
if (n == len(arr)):
    plusMinus(arr)