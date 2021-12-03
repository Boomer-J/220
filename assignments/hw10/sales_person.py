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
        self.name = name
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

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() < other.total_sales():
            return -1
        else:
            return 0

    def __str__(self):
        return "{}-{}:{}".format(self.employee_id, self.name, self.total_sales())

def main():
    construct_person = SalesPerson(210, "Jon")
    print("New Sale: " + str(construct_person.enter_sale((int(100)))))
    print(construct_person)
    print("Print ID: " + str(construct_person.get_id()))
    print("Print Total Sales: " + str(construct_person.total_sales()))
    print("Print Get Name: " + str(construct_person.get_name()))
    print("Set Name: " + str(construct_person.set_name("Jon")) + str(construct_person.get_name()))

    print("Quota: " + str(construct_person.met_quota(1000)))
    person = SalesPerson(200, "Mike")
    person.enter_sale(200)
    print("Compare: " + str(construct_person.compare_to(person)))

main()
