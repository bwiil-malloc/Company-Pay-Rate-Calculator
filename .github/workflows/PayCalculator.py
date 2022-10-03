#my pay-rate calculator

print("Hello there, welcome to our pay calculator! \n Please enter your data below:")

#Ask for user data.
Hours = input("Enter Hours: ")
Rate = input('Enter Rate: ')

#Convert to integer and calculate
Calc = int(Hours) * int(Rate)
Gum = (Calc) * 5
Ram = (Gum) * 4
Sam = (Ram) * 12

#Check for overtime or regular payment
if Calc > 1000:
	print("Overtime")
else:
	print("Regular")

#Calculation result
print("Your pay is:", Calc, "dollars a day,")
print(Gum, "dollars a week,")
print(Ram, "dollars a month, AND")
print(Sam, "dollars a year!" "\n CONGRATULATIONS!🌟")
print("Thank you for working with us!")

#Ask for user input
clit= input('Enter a room number: ')

try:
	swill =int (clit)
except:
	swill= -1
	
	
if swill > 0:
	print('Thank you for your data, we will get back to you.')
else:
	print('Not a number')
	print('Please insert a number.')
	Sun = input('Enter room number: ')
	
	
	print("Thanks for your data, we will get back to you.")
