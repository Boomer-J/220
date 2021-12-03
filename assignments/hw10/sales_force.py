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
    sales_people = []
    def __init__(self):
        sales_people = []
    def add_data(self, file_name):
        in_file = open(file_name, "r")
        list = in_file.readlines()
        for i in list:
            data = i.split(", ")
            person = SalesPerson(int(data[0]), data[1])
            sales = data[2].split()
            for j in sales:
                person.enter_sale(float(j))
            self.sales_people.append(person)
        in_file.close()



    def quota_report(self, quota):
        report = []
        for i in range(len(self.sales_people)):
            report.append([self.sales_people[i].get_id(), self.sales_people[i].get_name(), self.sales_people[i].total_sales(), self.sales_people[i].total_sales() > quota])
        return report

    def top_seller(self):
        seller1 = self.sales_people[0]
        best_seller = []
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].compare_to(seller1) > 0:
                seller1 = self.sales_people[i]
                best_seller = []
            elif self.sales_people[i].compare_to(seller1) == 0:
                best_seller.append(self.sales_people[i])
            best_seller.append(seller1)
        return best_seller

    def individual_sales(self, employee_id):
        individual = None
        for i in self.sales_people:
            if i.get_id() == employee_id:
                individual = i
        return individual
