available_funds = [50, 120, 250, 400, 90]

def check_security_flag(funds):
    for amount in funds:  # 1. Added the colon here!
        if amount > 200:  # 2. This colon requires the next line to indent further
            print(f"Warning: High transaction amount of {amount} detected!") 
            # 3. This must be indented 8 spaces (inside the 'for' AND inside the 'if')
# Call the function
check_security_flag(available_funds)
