# This function will convert a range of decimals to hexadecimal and write to a file

def dec_to_hex(int):
        
        dec = int
        hexa = ""
        
        while dec > 0:
            
            remainder = dec % 16
            
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
            
            dec = dec // 16
        
        return hexa
    
    
def main():
    with open("dec_to_hex_list.txt", "w") as file:
        for i in range(1, (2 ** 16) + 1): # 65536
            file.write(f"{i}: {dec_to_hex(i)}\n")
            
main()