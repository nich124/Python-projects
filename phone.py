class Phone:
    def __init__(self, number, network, airBal, daBal):
        self.number = number
        self.network = network
        self.airBal = airBal
        self.daBal = daBal

    def buyData(self, amount):
        if amount <= 0: print('Amount must be positive or more than zero')
        elif amount > self.airBal: print('Insfficient funds... buy airtime and try again')
        else: 
            if amount == 500:
                self.airBal -= amount
                self.daBal += 1.5
            elif amount == 1000:
                self.airBal -= amount
                self.daBal += 3  
            elif amount == 2000:
                self.airBal -= amount
                self.daBal += 6 
            print(f'transaction succesful your new data balance is {self.daBal} and youhave ${self.airBal} airtime left')
                  
        

dummyPhones = {
9110121081 : Phone('09110121081', 'Airtel', 1000, 2 ),
8101801298 : Phone('08101801298', 'MTN', 2000, 7 ),
7065178696 : Phone('07065178696', 'MTN', 300, 2 ),
9189854567 : Phone('09189854567', 'GLO', 800, 0 )
}


def data():
    num = int(input('Enter your phone number: 0'))
    while num not in dummyPhones:
        num = int(input('Enter a valid phone number: 0'))
    amount = float(input('Enter amount'))
    dummyPhones[num].buyData(amount)
    print(dummyPhones[7065178696])

