#ask user for their name and strip any whitespace and  capitalize the first letter of each word
name = input("what's your name? ").strip().title()

#say hello to the user
print(f"Hello, {name}!")