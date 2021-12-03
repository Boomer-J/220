"""
name: Jenks, Boomer
sales_force.py

Problem:  write a class for sales force

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson
class SalesForce:
    """this is a class for sales person
       attributes: add_data(file_name), quota_report(quota),
       top_seller, individual_sales(employee_id)"""

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, "r")
        for line in in_file:
            data = line.replace(",", "").split()
            seller = SalesPerson(float(data[0]), data[1] + " " + data[2])
            sales = data[3:]
            i = 0
            while i < len(sales):
                seller.enter_sale(float(sales[i]))
                i += 1
            self.sales_people += [seller]

    def quota_report(self, quota):
        report = []
        for employee in self.sales_people:
            report.append([employee.get_id(), employee.get_name(),
                            employee.total_sales(), employee.met_quota(quota)])
        return report

    def top_seller(self):
        seller_one = self.sales_people[0]
        best_seller = []
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].compare_to(seller_one) > 0:
                seller_one = self.sales_people[i]
                best_seller = []
            elif self.sales_people[i].compare_to(seller_one) == 0:
                best_seller.append(self.sales_people[i])
            best_seller.append(seller_one)
        return best_seller

    def individual_sales(self, employee_id):
        individual = None
        for i in self.sales_people:
            if i.get_id() == employee_id:
                individual = i
        return individual
