import random

class ATM:
    def _init_(self,card_number,pin,money):
        self.card_number = card_number
        self.pin=pin
        self.money=money

    def withdrawal(self):
       withdrawal_amount= int(input("how much do you want withrawed?"))  
       if money > withdrawal_amount: 
        money = money-withdrawal_amount
        print("Money Withdrawed")
        
       else:
        print("insufficient money in bank,try again")
   
    

def main():
    card_number=input("enter your card number ")
    pin =input("enter your pin")
    money=input("how much do you have in your account?")
    new_user = ATM(card_number,pin,money)
    
    print("choose your activity")
    print("1-withdraw money  2-balance enquiry")
    activity= int(input("enter the number"))
    if(activity ==1):
      new_user.withdrawal()

    elif(activity==2):
        print(money)
    else:
        print("click 1 or 2!! Read the instructions next time")

main()

    