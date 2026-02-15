class Transaction:
    def __init__(self,amount,description,types,category):
        self.amount = amount
        self.description = description
        self.types = types
        self.category = category

    def __str__(self):
        return f"Amount : {self.amount} | Category : {self.category} | Description: {self.description} | {self.types}"

class financeApp:
    def __init__(self,):
        self.transactions = []
        self.budget = {}
        
        

    def addTransactions(self,amount,description,types,category):
        transaction = Transaction(amount,description,types,category)
        self.transactions.append(transaction)
        print(f"{transaction}")
        

    def trackExpense(self,amount,description,types,category):
        transaction = Transaction(amount,description,types,category)
        self.transactions.append(transaction)
        print(f"{transaction}")

    def categorizeTransaction(self):
        categorized = {
            "Income":{},
            "Expense":{}
        }
        for transaction in self.transactions:
            mainType = transaction.types
            subcategory = transaction.category
            if subcategory not in categorized[mainType]:
                categorized[mainType][subcategory] = []
            categorized[mainType][subcategory].append(transaction)
            return categorized

    def mainCategory(self):
        print("\n Main Categories")
        print("1. Income")
        print("2. Expense")


    def subcategories(self,mainType):
        subCategories = set()
        for transaction in self.transactions:
            if transaction.types == mainType:
                subCategories.add(transaction.category)
        return subCategories

    def viewCategory(self,mainType,selectedCategory):
        total = 0
        found = False
        print(f"\n Transactions in {selectedCategory}({mainType}):")
        for transaction in self.transactions:
            if transaction.types == mainType and transaction.category == selectedCategory:
                print(f"{transaction.description} | {transaction.amount}")
                total += transaction.amount
                found = True

        if not found:
            print("No transaction found.")
        else:
            print(f"Total:{total}")
     
    def setbudgets(self,category,amount):
        self.budget[category] = amount
        print(f"Budget for {category} : {amount}")



    def getcategoryTotal(self,category):
        total = 0
        for transaction in self.transactions:
            print("transaction count:", len(self.transactions))
            if transaction.types == "Expense" and transaction.category == category:
                print("adding amount:", transaction.amount)
                total += transaction.amount
                return total
        

    def checkBudget(self,category):
        print("debug category passed to check budget:", repr(category))
        print("debug budget keys:", self.budget.keys())
        if category not in self.budget:
            print("No budget set for this category.")
        else:  
            budget = self.budget[category]
            spent = self.getcategoryTotal(category)
            print(f"\n  category: {category}")
            print(f"Budget :{budget}")
            print(f"Spent:{spent}")

            if spent > budget:
                print("Budget Exceeded!")

            else:
                print(f"Remaining {budget - spent}")

        

        

    def generateReports(self):
        pass 



    
app = financeApp()
while(True):
    print("\n---------- Personal Finance Tracker----------\n")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Category")
    print("4. Set Budget")
    print("5. View Budget")
    print("6. View Report")
    print("7. Exit")

    choice = input("Enter your choice :")
    if choice == "1":
        amount = float(input("Enter Income amount:"))
        category = input("Enter the category e.g: Salary,Freelance,Gift :")
        description = input("Enter the descriprion e.g: March Salary :")
        types = "Income"
        app.addTransactions(amount,description,types,category)
        print("Transaction has been added successfully")
        app.categorizeTransaction()
    elif(choice == "2"):
        amount = float(input("Enter Expense amount:"))
        category = input("Enter the category e.g: food,bills,Gift :")
        description = input("Enter the descriprion e.g: March Salary :")
        types = "Expense"
        app.addTransactions(amount,description,types,category)
        print("Transaction has been removed successfully")
        app.categorizeTransaction()

    elif(choice == "3"):
        app.mainCategory()
        number = input("Enter the number of the category you wish to view:")
        if number == "1":
            mainType = "Income"
        elif number == "2":
            mainType = "Expense"
        
        else:
            print("Invalid choice")
            continue

        subCategories = app.subcategories(mainType)
        if not subCategories:
            print("\n No Categories")
        else:
            print("\n Available Categories")
            for category in subCategories:
                print(f"{category}")
            selectedCategory = input("Enter category name:")
            app.viewCategory(mainType,selectedCategory)

        


    elif(choice == "4"):
       category = input("Enter expense category e.g food:")
       amount = float(input("Enter budget amount:"))
       app.setbudgets(category,amount)

    elif(choice == "5"):
        category = input("Enter expense category e.g food:")
        app.checkBudget(category)
         
     
    elif(choice == "6"):
        print("Existing The Application........")
        exit() 
    else:
        print("invalid syntax, Please enter a valid input")