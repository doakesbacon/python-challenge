import os
import csv

# Define the path to the CSV file
csvpath = os.path.join( "Resources", "budget_data.csv")
#print("Current working directory:", os.getcwd())
#print(csvpath)

# Define variables to store the financial data
months = 0
total = 0
previous_profit = 0
profit_changes = []
dates = []

# Open the CSV file using the csvpath variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract date and profit/loss from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months
        months += 1

        # Calculate the net total profit/loss
        total += profit_loss

        # Calculate the change in profit/loss
        if months > 1:
            profit_change = profit_loss - previous_profit
            profit_changes.append(profit_change)
            dates.append(date)

        # Set the previous profit/loss for the next iteration
        previous_profit = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_changes) / (months - 1)

# Find the greatest increase and decrease in profit/loss
increase = max(profit_changes)
increase_date = dates[profit_changes.index(increase)]
decrease = min(profit_changes)
decrease_date = dates[profit_changes.index(decrease)]

# Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

# Save the results to a text file
output_file = os.path.join("analysis" , "financial_analysis.txt")
# \n is new line 
with open(output_file, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {months}\n")
    output_file.write(f"Total: ${total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_date} (${increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease})\n")

