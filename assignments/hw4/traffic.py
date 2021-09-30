"""
name: Jenks, Boomer
traffic.py

Problem: The DOT has put out traffic counters on several city roads and
needs to know the average number of vehicles that travel each road per day and the
overall number and average number of vehicles that have traveled over all roads. .

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
def main():

    num_roads = eval(input("How many roads were surveyed?: "))
    tot_vehicles = 0
    for x in range(num_roads):
        days = eval(input("how many days was road " + str(x + 1) + " surveyed? "))
        acc = 0
        for i in range(days):
            cars = eval(input("how many cars traveled on that day " + str(i + 1) + " ? "))
            acc = acc + cars
            tot_vehicles = tot_vehicles + cars
            average = acc / days
        print("Road " + str(x + 1) + " average vehicles per day: ", round(average, 2))
    average_cars = tot_vehicles / num_roads
    print("the number of vehicles traveled on all roads: ", str(tot_vehicles))
    print("Average number of vehicles per road: ", round(average_cars, 2))

if __name__ == '__main__':
    main()
