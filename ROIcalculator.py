class Calculator():

    def __init__(self):
        self.cost= 200000  #user input
        self.rentalincome = 2000 #user input
        self.taxes = 150
        self.insurance = 150
        self.vacancy = self.rentalincome*0.05
        self.repairs =100
        self.capex =100
        self.propertymanagement = self.rentalincome*0.1
        self.mortgage = 760 #user input 
        self.improvements = 7000 #userinput
        self.downpayment = self.cost*0.2
        self.closingcosts = self.cost*0.03

    
    def income(self):
      totalincome = self.rentalincome
      return totalincome
        
    def expenses(self):
        totalexpenses = self.taxes + self.insurance + self.vacancy + self.repairs + self.capex + self.propertymanagement
        return  totalexpenses
   


    def investment(self):
        totalinvestment  = self.downpayment + self.improvements + self.closingcosts
        return totalinvestment 
   
    def cashFlow(self):
        cashflow= Calculator.income(self) - Calculator.expenses(self)
        return cashflow

    def ROI(self):
        ROIpercent = ((Calculator.income(self)*12)/Calculator.investment(self))*100
        return ROIpercent
       
    def output(self):
        print(f"your cashflow is: {Calculator.cashFlow(self)}")
        print(f"your ROI is: {round(Calculator.ROI(self), 2)} %")

    def getinputs(self):
        self.cost = int(input("How much is the property? "))
        self.rentalincome = int(input("What's the rental income? "))
        self.mortgage = int(input("What is the mortgage? "))
        self.improvements = int(input("How much is it to upgrade the property? "))

        Calculator.output(self)


run = Calculator()
run.getinputs()




        
        
        
        
        
        
        
        
        
        
        
        