
#Author Shalena Harris
#May 05, 2022
#Assignment objective to create two classes that inherit from a parent class


class Profile:
    name = "No name provided"
    email = ''
    password = 'p@$$w0rd'

class Contractor(Profile):
    base_pay = 495.00
    department = 'Security'

class Influencer(Profile):
    mailing_address = ''
    socialMedia_handle = ''
    
    

