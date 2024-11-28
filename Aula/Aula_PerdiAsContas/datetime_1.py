from datetime import datetime, timedelta
import math

a = datetime(2023, 2, 1)
b = datetime(2023, 2, 1, 9, 30, 0)
c = datetime.now()
d = datetime.today()

print(a, type(a))
print(b, type(b))
print(c)
print(d)
print(math.sqrt(16))

f = datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")
g = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")
print(f)
print(g)

# g.day = 9
print(g.day) # Atributos
print(g.month)
print(g.year)
print(g.date()) # Métodos
print(g.time())
print(g.weekday())
print(g.strftime("%d/%m/%Y %H:%M"))
print(g.strftime("%A, %d/%B/%Y"))

t1 = timedelta(days=1, hours=10)
t2 = timedelta(hours = 1, minutes = 30)