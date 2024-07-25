#Binary Conversion math with function
def convert(num): 
    if num == 0:
        return 0
    return (num % 2 + 10 * convert(num // 2)) 
user = int(input("Enter number: "))
print(convert(user))