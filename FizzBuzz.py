class FizzBuzz:
    def affiche():
        pass

#!/usr/bin/python3

def affiche():
	for i in range(1,35):
		if i%3==0 and i%5==0:
			print("FrisBee")
		elif i%5==0:
			print("Buzz")
		elif i%3==0:
			print("Fizz")
		else:
			print(i)
affiche()