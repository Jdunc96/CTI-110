# Description:This program takes input from the user then calculates and
#             and diplays the profit.
# Date:2 February 2020
# CTI-110 P2T1 - Sales Prediction
# Jason Duncan
#

#Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#calculate the prfit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit
print('The profit is $', format(profit, ',.2f'))
