# Dalton Baum

print("Welcome to the Binary Decimal Converter")

options = ""

#Main program loop
while options != "3":
    #Declare options
    options = input("Enter an option: \n1. Binary-Decimal Conversion \n2. Decimal-Binary Conversion \n3. Quit \nOPTION> ")
    if int(options) > 3:
        print("ERROR: Please choose from [1-3] \nOUTPUT ERROR")

        #Ask user to continue 
        cont_prompt = input("Would you like to continue (y/n)? \nCONTINUE> ")
        if cont_prompt.lower() == "yes" or cont_prompt.lower() == "y":
            continue
        else:
            print("OUTPUT Goodbye!")
            options = "3"

##############################################################################    

#Binary to Decimal
    if options == "1":
        b2d = list(input("BINARY-STR> "))

        #Allowed binary 
        bin_allowed = ["0", "1"]

        #Checks if any value in b2d is not in allowed binary characters
        value_exceeds = False
        for i in b2d:
            if i not in bin_allowed:
                value_exceeds = True
                break

#Error catching
        
        #Catches error for values greater than 1 in b2d
        if value_exceeds == True:
            b2dstr = "".join(b2d)
            print(f"ERROR: Input {b2dstr} is NOT a binary number. \nOUTPUT ERROR")
            
            #Ask user to continue
            cont_prompt = input("Would you like to continue (y/n)? \nCONTINUE> ")
            if cont_prompt.lower() == "yes" or cont_prompt.lower() == "y":
                continue
            else:
                print("OUTPUT Goodbye!")
                options = "3"
        
        else:
        #Variables for conversion
            exponent = len(b2d) - 1
            sum1 = 0
            result = 0

            #Binary conversion
            for i in b2d:
                if i == "1":
                    result = 2 ** exponent
                    sum1 = sum1 + result

                #decrement exponent
                exponent = exponent - 1
            
            #Print output
            b2dstr = "".join(b2d)
            print(f"Binary {b2dstr} is Decimal {sum1} \nOUTPUT {sum1}")

        #Ask user to continue
        cont_prompt = input("Would you like to continue (y/n)? \nCONTINUE> ")
        if cont_prompt.lower() == "yes" or cont_prompt.lower() == "y":
            continue
        else:
            print("OUTPUT Goodbye!")
            options = "3"

    ##############################################################################

    #Decimal to binary conversion
    if options == "2":

        dec_num = input("DECIMAL-STR> ")

        #Decimal values allowed
        dec_allowed = ["0","1","2","3","4","5","6","7","8","9"]

    #checks user entered acceptable value
        value_exceeds_decimal = False
        for i in dec_num:
            if i not in dec_allowed:
                value_exceeds_decimal = True
                break

        if value_exceeds_decimal == True:
            print(f"ERROR: Input {dec_num} is NOT a decimal number. \nOUTPUT ERROR")
        
            #Ask user to continue
            cont_prompt = input("Would you like to continue (y/n)? \nCONTINUE> ")
            if cont_prompt.lower() == "yes" or cont_prompt.lower() == "y":
                continue
            else:
                print("OUTPUT Goodbye!")
                options = "3"
    #Otherwise run the conversion
        else:

            #Variables for conversion
            binary_num = []
            dec_numi = int(dec_num)

            if dec_numi == 0:
                binary_num = ["0"]
            #Decimal conversion
            while dec_numi >= 1:
                remainder = (dec_numi % 2)
                dec_numi = (dec_numi//2)
                binary_num.append(str(remainder))
            
            #Rearrange list and make it a string
            binary_num.reverse()
            binary_num = "".join(binary_num)
            print(f"Decimal {dec_num} is Binary {binary_num} \nOUTPUT {binary_num}")

            #Ask user to continue
            cont_prompt = input("Would you like to continue (y/n)? \nCONTINUE> ")
            if cont_prompt.lower() == "yes" or cont_prompt.lower() == "y":
                continue
            else:
                print("OUTPUT Goodbye!")
                options = "3"