
while True:
    text = "\"Calculator\""
    centered_text = text.center(30)
    print(centered_text)
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()
    choice = input("Choose an option (1/2/3/4/5): ")
    print()
    
    if choice == '5':
        print("Jao Yahan se me tum se baat nahi karna chahata hu")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print()

        if choice == '1':
            print("Result: ", num1 + num2)
        elif choice == '2':
            print("Result: ", num1 - num2)
        elif choice == '3':
            print("Result: ", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result: ", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")
                continue
        else:
            print("Invalid choice!")
            continue
            
    except ValueError:
        print("Galat kion kar rahe ho tum/pagal ho gaye kia")
        continue

    while True:
        continue_choice = input("Dobara karna he kuch hisaab ? (yes/no): ")
        if continue_choice.lower() == 'no':
            print("Haan to wese bhi tum pagalon ko mera calculator use karne ki zaroorat nahi he pagal nikal yahan se")
            exit()
        elif continue_choice.lower() == 'yes':
            print("\n")
            break
        else:
            print("Sirf yes ya no likho!")