#ask user to input a number 
x = float(input("What's x? "))
y = float(input("What's y? "))

#multiply x and y and round the result to 3 decimal places
z = round(x * y, 3)

#display the result and format it with commas
print(f"{z:,}")