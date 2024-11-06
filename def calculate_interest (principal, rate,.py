def calculate_interest (principal, rate, time):
    interest = (principal*rate*time)/100
    return interest

y = calculate_interest(1000, 5, 2)
 
print (f'answer:{y}')