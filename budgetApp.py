import sys
class Budget:
    
    def __init__ (self):
        pass


    def AddBalance (self):        
        total_budget = int (input ('Enter amount you want to deposit: \n'))
        print ('Updating Balance....')
        category_balance['total_balance'] += total_budget
        print ('Balance updated successfully')
        print ("Present Balance is", category_balance['total_balance'])



    def Deposit (self, category):    
        while True:
            category = input ('Please enter Category\n')
            deposit_amount = int(input (f'Please enter amount to add to {category} Budget: \n'))
            if deposit_amount <= category_balance ['total_balance']:
                category_balance[category] = deposit_amount
                print (f'Depositing {deposit_amount} in {category} Budget')
                category_balance['total_balance'] -= deposit_amount
                print('Deposit successful')
                print ("Remaining balance is", category_balance['total_balance'])
                break 
            else:
                print('Deposit amount is higher than Total Balance. Please deposit a lower amount')
                continue
            

    def Withdraw (self, category):
        while True:
            withdrawal_category = input ('Please enter category you want to withdraw from: \n')
            withdrawal_amount = int (input (f'Please enter amount to withdraw from {withdrawal_category} Budget: \n'))
            break
        if withdrawal_amount <= category_balance['total_balance']:
            category_balance[category] = withdrawal_amount
            print (f'You are withdrawing {withdrawal_amount} from {withdrawal_category} Budget')
            category_balance['total_balance'] += withdrawal_amount
            print ('Withdrawal successful')
            print ("Remaining balance is", category_balance['total_balance'])
        else:
            print ('Withdrawal amount is higher than Total Balance. Please withdraw a lower amount')



    def Balance (self, category):
        check_category = input ('Please select category')
        print(f" Your {category}'s balance is {category_balance[category]}")


    def Transfer (self, category):
        while True:
            try:
                transfer_from = input ('What category are you transfering from?\n')
                transfer_to = input ('What category are you transferring to?\n')
                break
                if transfer_from in category and transfer_to in category:
                    transfer_amount = int(input ('Please enter transfer amount\n'))
                    category_balance[transfer_to] += transfer_amount
                    print ('Your Budget Balance is being Updated')
                    print (f"Your {tranfer_to}'s balance is now {category_balance[transfer_to]}")
                    category_balance[transfer_from] -= transfer_amount
                    print (f"Your {transfer_from.title()}'s balance is now {category_balance[transfer_from.title()]}")
                else:
                    print ("Category not found. Please enter valid category")
            except:
                continue



category = ['Savings', 'Rent', 'Transport']
options = ['Add', 'Deposit', 'Withdraw', 'Balance,' 'Transfer']
category_balance =  {'total_balance' : 150000, 'Saving' : 50000, 'Rent' : 30000, 'Transport' : 10000}
category = Budget()
category.AddBalance()
category.Deposit('Saving')
category.Withdraw('Saving')
category.Balance('Saving')
category.Transfer('Saving')
