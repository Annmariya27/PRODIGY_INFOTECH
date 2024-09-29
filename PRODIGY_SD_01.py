'''
    Create a program that converts temperatures between Celsius, Fahrenheit, 
    and Kelvin scales. The program should prompt the user to input a temperature 
    value and the original unit of measurement. It tre should then convert the 
    temperature to the other two units and display am the converted values to the user. 
    For example, if the user enters a temperature of 25 degrees Celsius, the program 
    should convert it to Fahrenheit and Kelvin, and present the converted values as outputs.
'''

def C_F(C):
    return (C * 9/5) + 32

def C_K(C):
    return C + 273.15

def F_C(F):
    return (F - 32) * 5/9

def F_K(F):
    return (F - 32) * 5/9 + 273.15

def K_C(K):
    return K - 273.15

def K_F(K):
    return (K - 273.15) * 9/5 + 32

def main():
    print("1. Celsius to Fahrenheit\n2. Celsius to Kelvin\n" +
          "3. Fahrenheit to Celsius\n4. Fahrenheit to Kelvin\n" +
          "5. Kelvin to Celsius\n6. Kelvin to Fahrenheit\n7. Exit")

    while True:
        ch = int(input("\nEnter your Choice: "))
       
        if ch == 1:
            num = float(input("Enter Celsius value: "))
            print(f"Fahrenheit value: {C_F(num):.2f}")
        elif ch == 2:
            num = float(input("Enter Celsius value: "))
            print(f"Kelvin value: {C_K(num):.2f}")
        elif ch == 3:
            num = float(input("Enter Fahrenheit value: "))
            print(f"Celsius value: {F_C(num):.2f}")
        elif ch == 4:
            num = float(input("Enter Fahrenheit value: "))
            print(f"Kelvin value: {F_K(num):.2f}")
        elif ch == 5:
            num = float(input("Enter Kelvin value: "))
            print(f"Celsius value: {K_C(num):.2f}")
        elif ch == 6:
            num = float(input("Enter Kelvin value: "))
            print(f"Fahrenheit value: {K_F(num):.2f}")
        elif ch == 7:
            print("Exiting...")
            break
        else:
            print("Invalid Input")

        again = input("Do you want to continue (yes/no)? ").strip().lower()
        if again == "no":
            break
        elif again != "yes":
            print("Invalid input! Exiting..")
            break

if __name__ == "__main__":
    main()
