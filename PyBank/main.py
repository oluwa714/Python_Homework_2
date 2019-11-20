#! python3

import csv

with open("budget_data.csv") as budget:
    csv_reader = csv.reader(budget)
    header = next(csv_reader)
    print(header)
    num_months_data = 0
    net_total = 0
    profit_changes = 0
    greatest_profit_increase = 0
    greatest_profit_month = ""
    greatest_profit_decrease = 0
    greatest_loss_month = ""
    

    for row in csv_reader:
        print(row)


#open("budget_report.txt", "w+")
#budget_report.write()
#budget_report.close()
