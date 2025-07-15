character = input("Enter a character (0 to exit): ")

while character != "0":
    if character in "aeiouAEIOU":
        print("It is a vowel")
    else:
        print("It is a consonant")
    
    character = input("Enter another character (0 to exit): ")

print("Program ended.")

