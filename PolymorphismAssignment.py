

#polymorphism assignment
#author shalena Harris

#Parent class
class Course:
    name = 'Example gof course'
    player = 'Tom'
    password = 'TheBestEver'

    def getLoginInfo(self):
        entry_name = input('Please enter your name: ')
        entry_password = input('Please enter your password: ')
        if (entry_name == self.name and entry_password == self.password):
            print("Welcome, {}! It's a beautiful day for some golf!".format(entry_name))
        else:
            print('That combination does not appear to be correct. Please try again.')
#child class for the head professional
class HeadPro(Course):
    status = 'professional'
    name = 'John'
    department = 'golfshop'
    pin_number = '15963'

    #this will use the same method from the prior parent class but using the entry pin
    def getLoginInfo(self):
         entry_name = input('Please enter your name: ')
         entry_password = input('Please enter your password: ')
         entry_pin = input('Enter your pin: ')
         if (entry_email == self.email and entry_pin == self.pin_number):
             print("Welcome back, {}. Here are all of the rounds of golf today!".ormat(entry_name))

             
#second child class for a server
class server(Course):
    base_pay = 15.00
    department = 'clubhouse'
    user_name = 'best ever'

    def getLoginInfo(self):
         entry_name = input('Please enter your name: ')
         entry_password = input('Please enter your password: ')
         entry_user = input('Please enter your user name: ')
         if (entry_name == self.name and entry_user == self.user_name):
             print("Welcome to work, {}! We do not have any current reservations.".format(entry_name))


server = Course()
server.getLoginInfo
        

    
        
    

    
        
                           
        
    
