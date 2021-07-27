from Register import ProductRegister, CustomerRegister, EmployeeRegister, SalesRegister


class System:
    def __init__(self):
        self.__menu = {1: "create new product", 2: "show registered products",
                       3: "create new employee", 4: "show registered employees",
                       5: "create new customer", 6: "show registered customers",
                       7: "create new sale", 8: "show registered sales"}
        self.__product_register = ProductRegister()
        self.__customer_register = CustomerRegister()
        self.__employee_register = EmployeeRegister()
        self.__sale_register = SalesRegister()

    def welcome(self):
        print(f"Welcome to the Register System\n")

    def show_menu(self):
        for k, v in self.__menu.items():
            print(f"Type {k} to {v}")
        print("Type 0 to exit")

    def start(self):
        self.welcome()
        self.show_menu()
        while True:
            command = input("Command (0 to exit): ")

            if command == '1':
                self.__product_register.register()
                continue

            if command == '2':
                self.__product_register.list()
                continue

            if command == '3':
                self.__employee_register.register()
                continue

            if command == '4':
                self.__employee_register.list()
                continue

            if command == '5':
                self.__customer_register.register()
                continue

            if command == '6':
                self.__customer_register.list()
                continue

            if command == '7':
                self.__sale_register.register()
                continue

            if command == '8':
                self.__sale_register.list()
                continue

            if command == '0':
                break

            else:
                print("Type a valid number, please")
                continue

        print("End")
