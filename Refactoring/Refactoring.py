from Customer import Customer
from Rental import Rental
from Movie import Movie

c1 = Customer("Sasi")
m1 = Movie("zero", 1)
m2 = Movie("aero", 0)
m3 = Movie("ae", 2)
r1 = Rental(m1,20)
r2 = Rental(m2,5)
r3 = Rental(m3,5)
c1.addRental(r1)
c1.addRental(r2)
c1.addRental(r3)
results = c1.statement()
print(results)