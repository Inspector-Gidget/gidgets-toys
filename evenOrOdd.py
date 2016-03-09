#!/usr/bin/python

print("Gidget-5000: Hello, master. How may I service you?")
responseA = input(">>> ")

getFunky = "Them numbers, baby."

if responseA == getFunky:
	print("Gidget-5000: Oooh, evens or odds. What will be the number? ")
	usernum = input(">>> ")
	try:
		if (int(usernum) == 666): 
			print("Gidget-5000: Fuck yes, the number of the beast. That number is even, hail Satan.")
		elif (int(usernum) % 2 == 0):
			print("Gidget-5000: Your number is even. Goodbye master, I'll be waiting for you.")
		else:
			print("Gidget-5000: Your number is odd. Goodbye master, I'll be waiting for you.")
	except ValueError as err:
		print("If you want to pleasure me, you must provide an integer.")

else:
	print("What? I don't recognize that response... Go away stranger!")


