from abc import ABC, abstractmethod
class dress(ABC):
    def garmentReceipt(self, amount):
        print("Your total is: ", amount)
#This function is instructing to pass in an argument, but it does not tell us
#how or what kind of data it will be.
        @abstractmethod
        def payment(self, amount):
            pass

class VisaPayment(dress):
    #this is where we define how to implement the payment function from the garmentReceipt class
    def payment(self, amount):
        print('Your purchase amount of {} is within youu $1000.00 limit'.format(amount))

obj = VisaPayment()
obj.garmentReceipt('$700')
obj.payment('$700')
