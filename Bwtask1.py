class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited successfully!")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please try again.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn successfully!")

    def atm_interface(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: "))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice.Please select a valid option")
my_atm = ATM(balance=1000.0)
my_atm.atm_interface()
