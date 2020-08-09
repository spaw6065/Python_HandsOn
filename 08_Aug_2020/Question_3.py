# You are in charge of the cake for your niece's birthday and have decided the cake will have
# one candle for each year of her total age.
# When she blows out the candles, sheâ€™ll only be able to blow out the tallest ones.
# Your task is to find out how many candles she can successfully blow out.
#
# For example, if your niece is turning 5 years old, and the cake will have
# 5 candles say height 1,4 ,3 ,4 ,2 she will be able to blow out 2 candles successfully,
# since the tallest candles are of height 4 and there are 2 such candles.
#
# Function Description
#
# Complete the function birthdayCakeCandles in the editor below. It must print an integer
# representing the number of candles she can blow out.
#
# birthdayCakeCandles has the following parameter(s):
#
# list: a list of integers representing candle heights
# Input Format
#
# The first line contains a single integer, , denoting the number of candles on the cake.
# The second line contains  space-separated integers, where each integer  describes the height of candle .
#

# Sample Input
#
# 4
# 3 2 1 3
# Sample Output
# 2
# Explanation
#
# We have one candle of height 1, one candle of height 2, and two candles of height 3.
# Your niece only blows out the tallest candles, meaning 2 candles of height 3 .
# Because there are 2 such candles,




# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(list1):
    list1.sort()
    tallest_candle = list1[len(list1)-1]
    print(list1.count(tallest_candle))


ar_count = int(input("enter her age: "))
ar = list(map(int, input().rstrip().split()))
birthdayCakeCandles(ar)