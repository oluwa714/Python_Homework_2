#! python3

import csv





with open("budget_data.csv") as budget:
    csv_reader = csv.reader(budget)
    header = next(csv_reader)
    print(header)
    months_of_data = 0
    net_total = 0
    last_profit = 0
    profit_changes = 0
    gpi = 0
    gpd = 0
    greatest_profit_month = ""
    greatest_profit_decrease = 0
    greatest_loss_month = ""
    

    for row in csv_reader:
        months_of_data += 1
        profit = int(row[1])
        net_total += profit
        if profit > last_profit:
            if (profit - last_profit) > gpi:
                gpi = profit - last_profit
        else:
            if (profit - last_profit) < gpd:
                gpd = profit - last_profit

        last_profit = profit

print("Greatest profit increase was: ",  gpi, ". Greatest profit decrease was: ",  gpd)

#open("budget_report.txt", "w+")
#budget_report.write(months_of_data)
#budget_report.close()
