
# This program converts decimal numbers to binary and hexadecimal and can convert binary to decimal
# There are explanation text files in the same folder as this program
# There are also text files that contain the results of the functions in this program using a range of numbers

def dec_to_bin():
    
    # simple error checking
    try:
        dec = int(input("Enter a decimal number: "))
    except ValueError:
        print("Invalid decimal number!")
        return dec_to_bin()  # If not, call the function again and return its result
    
    num_display = dec
    bin = ""
    
    # Inside the loop, the decimal number is divided by 2 and the remainder is added to the binary string
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    
    print(f"The binary number of {num_display} is: {bin}")

def bin_to_dec():
    
    bin = str(input("Enter a binary number: "))
    dec = 0
    
    # simple error checking
    if not all(char in '01' for char in bin):
        print("Invalid binary number!")
        return bin_to_dec()  # If not, call the function again and return its result
    
    # The loop iterates through the binary number and converts it into a decimal
    # The formula is: 2 ^ (length of binary - 1 - i) where i starts at 0    
    for i in range(len(bin)):
        dec += int(bin[i]) * (2 ** (len(bin) - 1 - i))
    
    print(f"The decimal number of {bin} is: {dec}")

def dec_to_hex():
    
    # simple error checking  
    try:
        dec = int(input("Enter a decimal number: "))
    except ValueError:
        print("Invalid decimal number!")
        return dec_to_hex()  # If not, call the function again and return its result
    
    num_display = dec
    hexa = ""
    
    # The loop iterates through the decimal number and converts it into a hexadecimal
    while dec > 0:
        
        # in base conversion, first we get the modulus of the number and add it to the string
        remainder = dec % 16
        
        # in hex conversion, after 10 there are 5 letters we use to represent the numbers
        if remainder < 10:
            hexa = str(remainder) + hexa
        elif remainder == 10:
            hexa = "A" + hexa
        elif remainder == 11:
            hexa = "B" + hexa
        elif remainder == 12:
            hexa = "C" + hexa
        elif remainder == 13:
            hexa = "D" + hexa
        elif remainder == 14:
            hexa = "E" + hexa
        elif remainder == 15:
            hexa = "F" + hexa
       
        # last, we divide the number by the base until the number is 0
        dec = dec // 16
    
    print(f"The hexadecimal number of {num_display} is: {hexa}")
    
def main():
        
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Exit\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        dec_to_bin()
    elif choice == 2:
        bin_to_dec()
    elif choice == 3:
        dec_to_hex()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice!")
        main()
        
main()