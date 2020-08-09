
2
# Given five positive integers, find the minimum and maximum values that can be calculated by
# summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated
# integers.
#
# For example, while entering 2 1 4 3 5. Our minimum sum is 10 and our maximum sum is 14. We would print
#
# 16 24
# Function Description
#
# Complete the miniMaxSum function. It should print two space-separated integers on one line:
# the minimum sum and the maximum sum of  of  elements.
#
# miniMaxSum has the following parameter(s):
#
# arr: a list of integers
# Input Format
#
# A single line of five space-separated integers.
#
# Output Format
#
# Print two space-separated long integers denoting the respective minimum and maximum values that can
# be calculated by summing exactly four of the five integers.
#
# Sample Input
#
# 3 5 6 8 7
# Sample Output
#
# 21 26


# Complete the miniMaxSum function below.
def miniMaxSum(list1):
    list1.sort()
    miniSum = int()
    maxSum = int()
    for cntr in range(0,len(list1)-1):
        miniSum += list1[cntr]
        maxSum += list1[(len(list1)-1)-cntr]

    print(f"{miniSum}  {maxSum}")

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
