#
# Monika
# BMI calculator
#

while True:
   weight = float (input('Enter your weight in kilogram:'))
   height = float (input('Enter yout height in meters:'))

   bmi = weight/ height**2
   print (f'your BMI is:{bmi}')

   answer = input('continue? (yes/no):')
   if answer == 'no':
     break