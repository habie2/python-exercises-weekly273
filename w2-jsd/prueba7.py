n = float(input('Introduce the number:'))
divisor = n
acum = 0
while divisor >= 2:
   if n % divisor == 0:
       acum += (n/divisor)
   divisor -= 1
if acum == n:
   print('It is a prefect number')
else:
   print('It is not a perfect number')
