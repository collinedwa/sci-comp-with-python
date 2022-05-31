import math
class Category:
  
  def __init__(self, list_category):
    self.list_category = list_category
    list_category = list_category.capitalize()
    self.ledger = []
    self.funds = 0.00
    self.spending = 0.00

  def __str__(self):
    name_list = []
    for i in range(len(self.ledger)):
        valuelist = []
        for value in (self.ledger[i].values()):
            valuelist.append(value)
        number = str(valuelist[0])
        if number.endswith(".0"):
            number += "0"
        name = str(valuelist[1])
        sentence = (str(name[:23] + number.rjust(30-len(name[:23])))+'\n')
        name_list.append(sentence)
    return (self.list_category.center(30,'*')+'\n'+ ''.join(name_list) + f"Total: {self.funds}")

  def check_funds(self, amount):
    if self.funds - float(amount) >= 0:
      return True
    else:
      return False
 
  def deposit(self, deposit_value, deposit_desc=""):
    deposit_amount = round(float(deposit_value),2)
    self.ledger.append({"amount": deposit_amount, "description": deposit_desc})
    self.funds += deposit_amount
    
  def withdraw(self, withdraw_value, withdraw_desc=""):  
    withdraw_amount = round(float(withdraw_value),2)
    if self.check_funds(withdraw_amount) == True:
      self.funds -= withdraw_amount
      self.ledger.append({"amount": 0-withdraw_amount, "description": withdraw_desc})
      self.spending += (0-withdraw_amount)
      return True
    else:
      return False
      
  def get_balance(self):
    return self.funds
    
  def transfer(self, amount, destination):
    transfer_amount = amount
    if self.check_funds(transfer_amount) == True:
      self.withdraw(transfer_amount, f"Transfer to {destination.list_category}")
      destination.deposit(transfer_amount, f"Transfer from {self.list_category}")
      return True
    else:
      return False
      
 
def create_spend_chart(categories):
    total_sum = 0
    names = []
    percentages = []
    
    for i in range(len(categories)):
        total_sum += categories[i].spending
        
    for i in range(len(categories)):
        names.append(categories[i].list_category)
        percentages.append((math.trunc(((categories[i].spending)/total_sum)*10))*10)
     
    return(graph(names,percentages))
    
def graph(names, percentages):
    text = 'Percentage spent by category\n'
    maxlength = len(max(names, key = len))
    bottomline = "    "+"-"*(3*len(names)+1)+"\n"
    index = 0
    percent = 100
    while percent >= 0:
        text += str(percent).rjust(3) + '|'
        for i in range(len(percentages)):
            if percentages[i] >= percent:
                text += 'o'.center(3)
            else:
                text += ' '.center(3)
        percent -= 10
        text += ' \n'
    text += bottomline
    while index <= maxlength:
        text += "    "
        for name in names:
            if index <= len(name)-1:
                text += name[index].center(3)
            else:
                text += ' '.center(3)
        index += 1
        if index == maxlength:
          text += ' '
          break
        else:  
          text += ' \n'
    return(text)