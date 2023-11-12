print("                 Welcome To Fonty                        ")
print("*********************************************************")
print("         This Program is used for size-types Conversion      ")
while True:
    while True:
        From_type = str(input("What size type do you want to convert? (em/px/%): "))
        if From_type == "em":
            To_type = input("What size type are you converting to? (px/%): ")
            break
        elif From_type == "px":
            To_type = input("What size type are you converting to? (em/%): ")
            break
        elif From_type == "%":
            To_type = input("What size type are you converting to? (em/px): ")
            break
        else:
            print("Invalid input, choose again...")
    if From_type == "px" and To_type == "em":
        px = float(input("Enter the value of px: "))
        em = px * 0.0625
        print("Your px in em is: %.4fem" %em)
    elif From_type == "em" and To_type == "px":
        em = float(input("Enter the value of em: "))
        px = em * 16
        print("Your em in px is: %.2fpx" %px)
    elif From_type == "px" and To_type == "%":
        px = float(input("Enter the value of px: "))
        percentage = px * 6.25
        print("Your px in percentage is: %.4f" %percentage)
    elif From_type == "%" and To_type == "px":
        percentage = float(input("Enter the value of %: "))
        px = percentage * 0.16
        print("Your percentage in px is: %.4fpx" %px)
    elif From_type == "em" and To_type == "%":
        em = float(input("Enter the value of em: "))
        percentage = em * 100
        print("Your em in percentage is: %.2f" %percentage)
    elif From_type == "%" and To_type == "em":
        percentage = float(input("Enter the value of %: "))
        em = percentage * 0.01
        print("Your percentage in em is: %.4f em" %em)
    Reuse =  str(input("Do you want to use the program again? (Yes/No): "))
    if Reuse == "No":
        print("Thanks for using this program")
        break
    else:
        continue