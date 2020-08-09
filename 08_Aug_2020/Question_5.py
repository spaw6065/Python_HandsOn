# Calculate and print the sum of the elements in an array,
# keeping in mind that some of those integers
# may be quite large.
#
# Function Description
#
# Complete the aVeryBigSum function. It must print the sum of all array elements.
#
# aVeryBigSum has the following parameter(s):
#
# ar: an array of integers .

# Input Format
# The first line of the input consists of an integer .
# The next line contains  space-separated integers contained in the array.
#
# Output Format
#
# Print the integer sum of the elements in the array.

# Sample Input
#
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Output
# 5000000015

# Complete the aVeryBigSum function below.
def aVeryBigSum(list):
    sum = int()
    for x in list:
        sum += x
    print(sum)


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
aVeryBigSum(ar)



