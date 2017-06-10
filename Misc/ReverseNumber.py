Number = 786865
Reverse = 0
print("\n Given number is = %d" %Number)
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10
 
print("\n Reverse of given number is = %d" %Reverse)
