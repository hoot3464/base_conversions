# This function will take a range of decimal numbers and convert to binary and write to a file

def dec_to_bin(int):
        
        dec = int
        bin = ""
        
        while dec > 0:
            bin = str(dec % 2) + bin
            dec = dec // 2
        
        return bin
    
def main():
    with open("dec_to_bin_list.txt", "w") as file:
        for i in range(1, (2 ** 8) + 1): # 256
            file.write(f"{i}: {dec_to_bin(i)}\n")
            
main()