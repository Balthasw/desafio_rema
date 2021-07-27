from Product import Product
from Customer import Customer
from Sale import Sale
from Employee import Employee

class ProductRegister:
    def __init__(self):
        self.__prod_id = 0
        self.__products = []

    # TODO: testes de entrada
    def register(self):
        id = self.__id
        name = input("Type the product's name: ").title()
        price = float(input("Type the price of the product: "))
        stock_quantity = int(input("Type the stock quantity of the product: "))
        product = Product(id, name, price, stock_quantity)
        self.add(product)

    def add(self, product):
        self.__products.append(product)
        print("Product Registered")
        self.__prod_id += 1

    def list(self):
        if not self.__products:
            print("No registered products")
        else:
            for product in self.__products:
                print(f"ID: {product.id}, Name: {product.name}, "
                      f"Price: {product.price}, Quantity: {product.stock_quantity}")

class CustomerRegister:
    def __init__(self):
        self.__cust_id = 0
        self.__customers = []

    # TODO: testes de entrada
    def register(self):
        id = self.__cust_id
        name = input("Type the customer's name: ").title()
        age = int(input("Type the age of the customer: "))
        address = input("Type the address of the customer: ")
        customer = Customer(id, name, age, address)
        self.add(customer)

    def add(self, customer):
        self.__customers.append(customer)
        print("Customer Registered")
        self.__cust_id += 1

    def list(self):
        if not self.__customers:
            print("No registered costumers")
        else:
            for customer in self.__customers:
                print(f"ID: {customer.id}, Name: {customer.name}, "
                      f"Address: {customer.address}, Age: {customer.age}")

class EmployeeRegister:
    def __init__(self):
        self.__emp_id = 0
        self.__employees = []

    # TODO: testes de entrada
    def register(self):
        id = self.__emp_id
        name = input("Type the employe's name: ").title()
        age = int(input("Type the age of the employee: "))
        address = input("Type the address of the employee: ")
        wage = float(input("Type the wage of the employee: "))
        employee = Employee(id, name, age, address, wage)
        self.add(employee)

    def add(self, employee):
        self.__employees.append(employee)
        print("Employee Registered")
        self.__emp_id += 1

    def list(self):
        if not self.__employees:
            print("No registered employees")
        else:
            for employee in self.__employees:
                print(f"ID: {employee.id}, Name: {employee.name}, "
                      f"Address: {employee.address}, Age: {employee.age}"
                      f"Wage: {employee.wage}")

class SalesRegister:
    def __init__(self):
        self.__sale_id = 0
        self.__sales = []

    # TODO: testes de entrada
    def register(self):
        id = self.__sale_id
        prod_id = int(input("Type the product id: "))
        cust_id = int(input("Type the customer id: "))
        quantity = int(input("Type the quantity: "))
        final_price = float(input("Type the final price: "))
        sale = Sale(id, prod_id, cust_id, quantity, final_price)
        self.add(sale)

    def add(self, sale):
        self.__sales.append(sale)
        print("Sale Registered")
        self.__sale_id += 1

    def list(self):
        if not self.__sales:
            print("No registered employees")
        else:
            for sale in self.__sales:
                print(f"ID: {sale.id_sale}, Prod ID: {sale.id_product}, "
                      f"Customer ID: {sale.id_customer}, Quantity: {sale.quantity}, "
                      f"Final price: {sale.final_price}")
