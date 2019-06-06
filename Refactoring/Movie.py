class Movie(object):
    def __init__(self,title,priceCode):
        self.title = title
        self.priceCode =    priceCode
    def getPriceCode(self):
        return self.priceCode
    def set_priceCode(self,priceCode):
        self.priceCode=priceCode
    def getTitle(self):
        return self.title


