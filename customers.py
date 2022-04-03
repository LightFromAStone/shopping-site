"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""

    # ------ Begin My Code ------
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __repr__(self):
        """Convenience method to show information about customers in console."""
        
        return f'<Customer: {self.first_name}, {self.last_name} - {self.email}>'


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: Customer(...)}
    """
    customers = {}
    
    with open(filepath) as file:
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.strip().split('|')
            
            customers[email] = Customer(first_name, last_name, email, password)
    
    return customers
    
    
def get_by_email(email):
    """Returns a Customer given an email address"""
    
    # This relies on access to the global dictionary `customers`
    return customers.get(email)


# Dictionary to hold customers.
#
# Format is {email: Customer(...), ... }
customers = read_customers_from_file('customers.txt')
    # ------ End My Code ------
