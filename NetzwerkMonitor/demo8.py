def culculate(bill, percentage):
    t_sum = bill * (percentage / 100)
    return t_sum

bill_amount = float(input("What is your bill? "))
percentage_amount = float(input("What is the percentage amount? "))

t_sum = culculate(bill_amount, percentage_amount) # fine the t_sum percentage amount
total = bill_amount + t_sum  # Add the total sum bill sum with percentage

print(f"Tip percentage amount: ${t_sum}")
print(f"Total to pay: ${total}")

