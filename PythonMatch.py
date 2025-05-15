day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

print("-----------------")

day1 = 4

match day1:
     case 6:
         print("Today is Saturday")
     case 7:
         print("Today is Sunday")
     case _:
         print("Looking forward to the Weekend")
print("-----------------")


day2 = 4

match day2:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love Weekends")
print("-----------------")


month3 = 5
day3 = 4
match day3:
    case 1 | 2 | 3 | 4 | 5 if month3 == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month3 == 5:
        print("A weeday in May")
    case _:
        print("No match")