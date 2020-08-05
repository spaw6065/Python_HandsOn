#12) WAP to find out the leap year. (Except a year from the user using input)
dob = input("Enter the date of birth in format DD/MM/YYYY")

dob_list = dob.split(sep="/",maxsplit=2)
dob_date = int(dob_list[0])
dob_month = int(dob_list[1])
dob_year = int(dob_list[2])

##date suffix logic eg 1 is 1st 2 is 2nd
if dob_list[0].endswith("1"):
    date_suffix="st"
elif dob_list[0].endswith("2"):
    date_suffix="nd"
elif dob_list[0].endswith("3"):
    date_suffix="rd"
else:
    date_suffix="th"

##Month numeral to month string mapping
Month_dictionary = {1:"January",
                    2:"February",
                    3:"March",
                    4:"April",
                    5:"May",
                    6:"June",
                    7:"July",
                    8:"August",
                    9:"September",
                    10:"October",
                    11:"November",
                    12:"December"
                    }

print(f"As per the input you were born on {dob_date}{date_suffix},month of {Month_dictionary[dob_month]} in the year {dob_year} and ",end="")

if dob_year%4 == 0 and dob_year%400 == 0:
    print(f"year {dob_year} is a leap year")
else:
    print(f"year {dob_year} is not a leap year")