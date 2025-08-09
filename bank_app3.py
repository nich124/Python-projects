import os
from time import sleep
from datetime import datetime
import random
import phone as p

class bankApp:
    def __init__(self, name, acc, balance):
        self.name = name
        self.acc = acc
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            sleep(1)
            print(f'\n❌ You are broke! Go and hustle! 💸 Current balance: ${self.balance}')
        else:
            self.balance -= amount
            sleep(1)
            print(f'\n✅ Withdraw of ${amount} successful! 💰 New balance: ${self.balance}')

    def deposit(self, amount):
        self.balance += amount
        sleep(1)
        print(f'\n✅ Deposit successful! 📥 New balance: ${self.balance}')
        
    def showBalance(self):
        sleep(1)
        print(f'\n👤 Account Name: {self.name}')
        print(f'🔢 Account Number: {self.acc}')
        print(f'💰 Available Balance: ${self.balance}\n')

    def transfer(self, amount, recipient):
        if amount <= 0:
            print("❌ Transfer amount must be positive")
        elif amount > self.balance:
            print("❌ Insufficient funds for transfer")
        else:
            self.balance -= amount
            recipient.balance += amount
            sleep(1)
            print(f'\n✅ Transferred ${amount} to {recipient.name}')
            print(f'💳 Your new balance: ${self.balance}')

    def airtime(self, amount, phone):
        if amount <= 0:
            print("❌ Airtime amount must be positive")
        elif amount > self.balance:
            print("❌ Insufficient funds for airtime purchase")
        else:
            self.balance -= amount
            p.dummyPhones[phone].airBal += amount
            # recipient.balance += amount
            sleep(1)
            print(f'\n✅ Transferred ${amount} worth of airtime to {phone}')
            print(f'💳 Your new balance: ${self.balance}')
            print(f'{phone} Aitime balabe is {p.dummyPhones[phone].airBal}')


dummy_accounts = {
    123456: bankApp("John Doe", 123456, 1000),
    654321: bankApp("Jane Smith", 654321, 500),
    987654: bankApp("Wisdom Blaise", 987654, 7000),
    1:bankApp('a',1,122333)
}

def create_Account():
    print("\n" + "="*50)
    print("🏦 CREATE NEW ZENITH BANK ACCOUNT".center(50))
    print("="*50)
    
    name = input('\n👤 Enter your name: ')
    # acc_num = int(input('🔢 Enter account number: '))
    acc_num = random.randint(10**9, 10**10-1)

    while acc_num in dummy_accounts:
        acc_num = random.randint(10**9, 10**10-1)

    deposit = int(input('💰 Enter initial deposit amount: $'))
    
    dummy_accounts[acc_num] = bankApp(name, acc_num, deposit)
    
    print('\n🔄 Creating account...')
    sleep(1.5)
    print(f'✅ Account created successfully! \nWelcome to zenith bank {name} Your account number is{acc_num}')
    sleep(1)
    print('⏳ Redirecting to transaction menu...')
    sleep(2.5)
    runApp()

def runApp():
    dob = str(datetime.now())
    
    print("\n" + "="*50)
    print("🏦 ZENITH BANK LOGIN".center(50))
    print("="*50)
    
    try:
        user = input('\n👤 Enter your name: ')
        yrAcc = int(input('🔢 Enter your Account Number: '))
    except ValueError as d:
        print(f'❌Wrong Input!!! {d}')
        runApp()

    if yrAcc in dummy_accounts and user.lower() == dummy_accounts[yrAcc].name.lower():
        while True:
            try:
                print("\n" + "🔷 MAIN MENU 🔷".center(50, '~'))
                transactions = int(input(
                    '\n1. 💸 Withdraw\n2. 📥 Deposit\n3. 📤 Transfer\n4. 💳 Check Balance\n5. 📤 Airtime\n6. 📤 Data\n7. 🚪 Exit\n'
                    '📝 Enter choice (1-6): '
                ))
                
                if transactions == 1: 
                    print("\n" + "💸 WITHDRAWAL".center(50, '-'))
                    amountToWith = int(input('\n💰 Enter amount to withdraw: $'))
                    dummy_accounts[yrAcc].withdraw(amountToWith)
                    
                    if dummy_accounts[yrAcc].balance >= amountToWith:
                        dw = f"""Name: {dummy_accounts[yrAcc].name}
Amount withdrawn: ${amountToWith}
Balance before: ${dummy_accounts[yrAcc].balance + amountToWith}
Balance now: ${dummy_accounts[yrAcc].balance}
{dob}"""
                    else:
                        dw = f"""Name: {dummy_accounts[yrAcc].name}
Withdrawal attempt: ${amountToWith} (FAILED)
Reason: Insufficient funds
Available balance: ${dummy_accounts[yrAcc].balance}
{dob}"""
                    receipt(dummy_accounts[yrAcc].name, dw)
                    
                elif transactions == 2:  
                    print("\n" + "📥 DEPOSIT".center(50, '-'))
                    amountToDepo = int(input('\n💰 Enter amount to deposit: $'))
                    dummy_accounts[yrAcc].deposit(amountToDepo)
                    dd = f"""Name: {dummy_accounts[yrAcc].name}
Amount deposited: ${amountToDepo}
Balance before: ${dummy_accounts[yrAcc].balance - amountToDepo}
Balance now: ${dummy_accounts[yrAcc].balance}
{dob}"""
                    receipt(dummy_accounts[yrAcc].name, dd)

                elif transactions == 3:  
                    print("\n" + "📤 TRANSFER".center(50, '-'))
                    amountToTra = int(input('\n💸 Enter amount to transfer: $'))
                    accountNumber = int(input('🔢 Enter recipient account number: '))
                    
                    while accountNumber not in dummy_accounts:
                        accountNumber = int(input('❌ Account not found! Try again: '))
                        
                    reciever = dummy_accounts[accountNumber]
                    sleep(1)
                    confirm = input(
                        f'\n⚠️ Confirm transfer: ${amountToTra} to {reciever.name}'
                        f'\n1. ✅ Proceed\n2. ❌ Cancel\nChoice: '
                    )
                    
                    while confirm not in ('1', '2'):
                        confirm = input('❌ Invalid choice! Enter 1 or 2: ')
                    
                    if confirm == '1':
                        dummy_accounts[yrAcc].transfer(amountToTra, reciever)
                        sender_receipt = f""" 
TRANSFER RECEIPT
From: {dummy_accounts[yrAcc].name} (Acc: {yrAcc})
To: {reciever.name} (Acc: {reciever.acc})
Amount: ${amountToTra}
New Balance: ${dummy_accounts[yrAcc].balance}
Date: {dob}
🔒 Secured by Zenith Bank 🔒
------------------------------"""
                        receipt(dummy_accounts[yrAcc].name, sender_receipt)
                
                elif transactions == 4:  
                    print("\n" + "💳 ACCOUNT BALANCE".center(50, '-'))
                    dummy_accounts[yrAcc].showBalance()
                    db = f"""Name: {dummy_accounts[yrAcc].name}
Account Number: {dummy_accounts[yrAcc].acc}
Available Balance: ${dummy_accounts[yrAcc].balance}
{dob}"""
                    receipt(dummy_accounts[yrAcc].name, db)

                elif transactions == 5:
                    print("\n" + "💳 AIRTIME PURCHASE".center(50, '-'))
                    net = input('\n1. MTN\n2. AIRTEL\n3. GLO\nSELECT NETWORK: ')
                    while net not in ('1','2','3'):
                        net = input('\n1. MTN\n2. AIRTEL\n3. GLO\nSELECT NETWORK: ')
                    if net == '1': net = 'MTN'
                    elif net == '2': net = "AIRTEL"
                    elif net == '3': net = 'GLO'
                    pNum = int(input(f'Enter an {net} Phone Number: '))
                    while pNum not in p.dummyPhones:
                        any = 'an' if net[0] in 'aeiou' else 'a'
                        pNum = int(input(f'Enter {any} {net} Phone Number: '))
                    while p.dummyPhones[pNum].network.lower() != net.lower():
                        an = 'an' if net[0] in 'aeiou' else 'a'
                        pNum = int(input(f'Number must be {an} {net} Netork: '))
        
                    airAmo = int(input("Enter Amount"))
                    dummy_accounts[yrAcc].airtime(airAmo,pNum)
                    ab = f""" 
AIRTME PURCHASE RECEIPT
From: {dummy_accounts[yrAcc].name} (Acc: {yrAcc})
Phone Number: {pNum} (Network: {net})
Amount: ${airAmo}
New Balance: ${dummy_accounts[yrAcc].balance}
Date: {dob}
🔒 Secured by Zenith Bank 🔒
------------------------------"""
                    receipt(f'{net}Airime_Purchase', ab)


                elif transactions == 6:
                    p.data() 
                
                elif transactions == 7:  
                    exit_choice = input('\n🚪 Exit application? (Y/N): ').lower()
                    while exit_choice not in ('y', 'n'):
                        exit_choice = input('❌ Invalid input! Enter Y/N: ').lower()
                    if exit_choice == 'n':
                        continue
                    print('\n' + '='*50)
                    print('🙏 Thank you for banking with Zenith!'.center(50))
                    print('🔒 Your money is safe with us!'.center(50))
                    print('='*50)
                    break
                
                else:
                    print('❌ Please enter a number between 1-5')
                    continue
                    
            except ValueError:
                print('❌ Invalid input! Numbers only please')
    
    else:
        print('\n❌ Invalid name or account number!')
        sleep(1)
        create = input('\n1. 🆕 Create account\n2. 🔄 Try again\nChoice: ')
        while create not in ('1', '2'):
            create = input('❌ Invalid choice! Enter 1 or 2: ')
        if create == '1':
            create_Account()
        else:
            runApp()

def receipt(name, content):
    choice = input('\n🧾 Print receipt? (Y/N): ').lower()
    while choice not in ('y', 'n'):
        choice = input('❌ Invalid input! Enter Y/N: ').lower()
    
    if choice == 'y':
        filename = f"{name}_receipt.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("🏦 ZENITH BANK RECEIPT 🔒\n")
                file.write("="*50 + "\n")
                file.write(content)
                file.write("\n" + "="*50)
            print(f'✅ Receipt saved as {filename}')
        except Exception as e:
            print(f'❌ Error saving receipt: {e}')
    else:
        print('⏭️ Receipt skipped')

def welcome():
    print('\n' + '='*50)
    print('🏦 WELCOME TO ZENITH BANK MOBILE APP'.center(50))
    print('🔒 WE KEEP YOUR MONEY SAFE'.center(50))
    print('='*50)
    
    service = input('\n1. 💼 Transaction Menu\n2. 🆕 Create Account\nChoice: ')
    while service not in ('1', '2'):
        service = input('❌ Invalid choice! Enter 1 or 2: ')
    
    if service == '1':
        runApp()
    else:
        create_Account()


if __name__ == "__main__":
    welcome()