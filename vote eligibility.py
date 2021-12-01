n=int(input("Enter your age: "))
if(n>=18):
    print("You are elegible to vote")
else:
    print("You are remaining with {} years to vote".format(18-n))
