class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description= ''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
    
    def withdraw(self, amount, description = ''):
        if amount > self.get_balance():
            return False
        self.ledger.append({
            'amount': (-1*amount),
            'description': description
        })
        return True
    
    def get_balance(self):
        amount = 0
        for entry in self.ledger:
            amount += entry['amount']
        return amount

    def transfer(self, amount, Category):
        if amount > self.get_balance():
            return False
        self.withdraw(amount, f'Transfer to {Category.name}')
        Category.deposit(amount, f'Transfer from {self.name}')
        return True
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        total = 30 - len(self.name)
        sides = '*'*int(total/2)
        printer = f"""{sides}{self.name}{sides}\n"""
        for N in self.ledger:
            if len(N['description']) < 23:
                printer += f"{N['description']:<23}{N['amount']:>7.2f}\n"
            else:
                cut_description = str(N['description'])
                cut_description = cut_description[:23]
                printer += f"{cut_description:<23}{N['amount']:>7.2f}\n"
        printer += f"Total: {self.get_balance()}"
        return printer
 
def create_spend_chart(categories):
    Print_string = f"Percentage spent by category\n"
    amount_spent = 0
    percentage_int = 100
    percentage_spent = []
    each_category_spent = []
    total_categories = 0
    current_spent = 0
    for category in categories:
        total_categories += 1
        for entry in category.ledger:
            if entry['amount'] < 0:
                amount_spent += abs(entry['amount']) 
                current_spent+= abs(entry['amount'])
        each_category_spent.append((current_spent))
        current_spent = 0
    for number in each_category_spent:
        total = ((number / amount_spent) * 100)
        total = int(total // 10) * 10
        percentage_spent.append(total)
    
    while percentage_int >= 0:
        Print_string += f"{percentage_int:>3}| "
        for entry in percentage_spent:
            if entry >= percentage_int:
                Print_string += 'o  '
            else:
                Print_string += '   '
        Print_string += "\n"
        percentage_int -= 10
    Print_string += "    " + (total_categories*3* "-") + ("-")
    category_names = []
    for category in categories:
        category_names.append(category.name)
    longest_name = 0
    for x in category_names:
        length = len(x)
        if length > longest_name:
            longest_name = length
    letter_index = 0
    while longest_name > 0:
        Print_string += "\n     "
        for names in category_names:
            if (letter_index+1) <= len(names):
                letter = names[letter_index]
                Print_string += f"{letter}  "
            else:
                Print_string += "   "
        letter_index += 1
        longest_name -= 1
    return Print_string



#Test Code
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
food.deposit(1000, "initial deposit")
food.withdraw(105.55)
food.withdraw(33.40)
clothing.deposit(500, "initial deposit")
clothing.withdraw(55.00)
auto.deposit(1000, "initial deposit")
auto.withdraw(450.00)

test = create_spend_chart([food, clothing, auto])
print(test)
