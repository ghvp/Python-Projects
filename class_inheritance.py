
class user:
    name = ''
    email = ''
    phone_number = ''

    
class customer(user):
    account_number = 0
    address = ''

    
class employee(user):
    emp_id = 0
    schedule = 'M-F'
