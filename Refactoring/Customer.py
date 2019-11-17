from Rental import Rental

class Customer():
    REGULAR = 0
    CHILDERNS = 2
    NEW_RELEASE = 1
    #write constractor
    def __init__(self,name):
        self.name = name
        self.rentals = []
    def addRental(self,args):
        self.rentals.append(args)
    def getName(self):
        return self.name
    def statement(self):
        totalAmount = 0
        frequentRenterPoints = 0
        rentals = self.rentals
        result = "Rental Record for " + self.getName() + "\n"
        for each in self.rentals:
            thisAmount =0;
            if(each.getMovie().getPriceCode() == self.REGULAR):
                thisAmount += 2
                if(each.getDaysRented() > 2):
                    thisAmount += (each.getDaysRented()-2)*1.5 
            elif(each.getMovie().getPriceCode() ==  self.NEW_RELEASE):
                thisAmount +=  each.getDaysRented() *3
            elif(each.getMovie().getPriceCode() ==  self.CHILDERNS):
                thisAmount += 1.5
                if(each.getDaysRented() > 3):
                    thisAmount += (each.getDaysRented()-3)*1.5
            else:
                pass
            # add frequent Renter Points
            frequentRenterPoints += 1
            #add bonus for two days new release rental
            if(each.getMovie().getPriceCode() == self.NEW_RELEASE and each.getDaysRented() > 1 ):
                frequentRenterPoints += 1
            #show figures for this rental
            result += "\t {0} \t {1} \n".format(each.getMovie().getTitle(),thisAmount)
            totalAmount += thisAmount
            #add footer lines
        result += "amount owes is {0} \n you earned is {1} frquent rental point.".format(totalAmount,frequentRenterPoints)
        return result\\