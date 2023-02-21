"""
Ordinary statements are perishable
- Cannot undo member assignment
- Cannot directly serialize a sequence of actions(calls)

Want an object that represents an operation
- person should change its age to value 22
- car should do explode()
Uses: GUI commands, multi-level undo/redo, macro recording(record a sequence of commands
so that you can play back that sequence once again when you need to) etc.

Command -An object which represents an instruction to perform a particular action. 
Contains all the information necessary for the action to be taken.

Summary
- Encapsulate all details of an operation in a seperate object
- Define instruction for applying the command(either in the command itself or elsewhere)
- Optionally define instructions for undoing the command
- Can create composite commands (a.k.a macros)

"""
from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT =-500
    
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance ={self.balance}')
        
    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance ={self.balance}')
            return True
        return False
    
    def __str__(self):
        return f'Balance ={self.balance}'
    
# optional
class Command(ABC):
    def invoke(self):
        pass
    def undo(self):
        pass
    
class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None
        
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1
        
    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
            
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
            
    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
            
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)
            
if __name__=='__main__':
    ba = BankAccount()
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print('After $100 deposit:', ba)
    
    cmd.undo()
    print('$100 deposit undone:', ba)
    
    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    illegal_cmd.invoke()
    print('After impossible withdrawal:', ba)
    illegal_cmd.undo()
    print('After undo:', ba)