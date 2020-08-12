input("Press Enter to Begin")

print (" ")

# Below are the title and border
print ("Change Calculator")
print ("-" *70)

# Below is Current Money and User Name
Name = input ("Enter name here: ")
CurrentMoney = int(input("Enter amount you have: $"))

print (" ")

# Below is money inputs 
FirstItem = int(input("Enter cost of first item: $"))
SecondItem = int(input("Enter cost of second item: $"))
ThirdItem = int(input("Enter cost of third item: $"))

# Quick Eqautions to make the final line look clean

Spent = str(FirstItem+SecondItem+ThirdItem)

Change = str(CurrentMoney-(FirstItem+SecondItem+ThirdItem))

# Below is final output 

print (" ")

print ("Hello " +Name+ " you have spent $" +Spent+ " your change is $" +Change+ ". Have a nice day.")

# Border 
print ("-" *70)

# Enter to End - Credit to Zac, for testing and recomending the idea :)

input("Press Enter to End")