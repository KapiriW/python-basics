# Ask the user for their name
username= input("What is your name? ")
# Ask the user for their favourite integer
# Double, halve and square the number
fav_num = int(input("Favourite Number? "))
# Greet the user
# Output the results of doubling, halving # and squaring their favourite number
double = fav_num *2
half = fav_num / 2
squared = fav_num * fav_num


print()

print("Hi {}, you favourite number is {}".format(username, fav_num))
print()


print("double {} is {}".format(fav_num, double))
print("half {} is {}".format(fav_num, half))
print("{} squared is {}".format(fav_num, squared))
print()