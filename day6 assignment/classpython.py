class Bankaccount: 
    def __init__(self, ownername ,balance): 
        self.ownername=ownername
        self.balance=balance
        
        
        
    def getdetails(self):
        print("Ownername",self.ownername)
        print("Balance",self.balance)

    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 

    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

s = Bankaccount("vinod",120000) 
s.getdetails()
s.deposit() 
s.withdraw() 
s.display() 