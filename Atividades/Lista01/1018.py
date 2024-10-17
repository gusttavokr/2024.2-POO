x = int(input())

cem = x//100
cinq = (x%100)//50
vint = ((x%100)%50)//20
dez = (((x%100)%50)%20)//10
cinco = ((((x%100)%50)%20)%10)//5
dois = (((((x%100)%50)%20)%10)%5)//2
um = (((((x%100)%50)%20)%10)%5)%2

print(x)
print(cem,'nota(s) de R$ 100,00')
print(cinq,'nota(s) de R$ 50,00')
print(vint ,'nota(s) de R$ 20,00')
print(dez, 'nota(s) de R$ 10,00')
print(cinco, 'nota(s) de R$ 5,00')
print(dois, 'nota(s) de R$ 2,00')
print(um, 'nota(s) de R$ 1,00')