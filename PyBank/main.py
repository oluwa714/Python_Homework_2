#! python3

import csv

with open("budget_data.csv") as budget:
    csv_reader = csv.reader(budget)
    header = next(csv_reader)
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
        prof_chng = profit - last_profit
        profit_changes += prof_chng
        if profit > last_profit:
            if prof_chng > gpi:
                greatest_profit_month = row[0]
                gpi = prof_chng
        else:
            if prof_chng < gpd:
                greatest_loss_month = row[0]
                gpd = prof_chng

        last_profit = profit
    avg_profit_change = ('%.2f'%(profit_changes/months_of_data))

budget_report = open("budget_report.txt", "w+")
print("     Budget Report \n ____________________")
print("The net profit over this {0} month time frame was: ${1}.".format(months_of_data, net_total))
print("The greatest profit increase was: $ {0} in {1}. The greatest profit decrease was: $ {2} in {3}.".format(gpi, greatest_profit_month, gpd, greatest_loss_month))
print("The average change in profit was: ${0}.".format(avg_profit_change))

print("     Budget Report \n ____________________", file = budget_report)
print("The net profit over this ", months_of_data, " month time frame was: $", net_total, ".", file = budget_report)
print("Greatest profit increase was: $",  gpi, ". Greatest profit decrease was: $",  gpd, file = budget_report)
print("The average change in profit was: $", avg_profit_change, ".", file = budget_report)

budget_report.close()
