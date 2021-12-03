"""
name: Jenks, Boomer
sales_person.py

Problem:  write a class for sales person

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
class SalesPerson:
    """this is a class for sales person
    attributes: get_id, get_name, set_name, enter_sale, total_sales
     set_name(name), enter_sale(int(value)), get_sales, metQuota, compare_to(Salesperson(other))"""

    def __init__(self, employee_id, name):
        self.name =name
        self.sales = []
        self.employee_id = employee_id

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name


    def set_name(self, name):
        self.name = name


    def enter_sale(self, value):
        self.sales.append(value)


    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def metQuota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() == other.total_sales:
            return int(0)
        elif self.total_sales() < other.total_sales():
            return -1


    def __str__(self):
        return "{} -{} :{}".format(self.employee_id, self.name, self.total_sales())

def main():
    construct = SalesPerson(210, "bob")
    print("new sale" + str(construct.enter_sale(int(100))))
    print(construct)
    print("print id"+ str(construct.get_id()))
    print("print total sales: "+ str(construct.total_sales()))
    print("print get_name"+str(construct.get_name()))
    print("set name" + str(construct.set_name("bill")) + str(construct.get_name()))

    print("quota"+str(construct.metQuota(1000)))
    person = SalesPerson(200, "joe")
    person.enter_sale(100)
    print("compare: " +str(construct.compare_to(person)))

main()
