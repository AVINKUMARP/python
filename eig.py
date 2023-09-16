a=int(input("enter the number of days:"))
d={28:"february",30:"April, June, September, November",31:"January, March, May, July, August, October, December"}
print("The months with",a,"days are : ",d[a])
n=input("enter the month :")
if (n in d[30]):
    print("30 days")
elif (n in d[31]):
    print("31 days")
else:
    print("28 days")