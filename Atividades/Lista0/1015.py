x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

a = (x2 - x1)*(x2 - x1)
b = (y2 - y1)*(y2 - y1)

distancia = (a + b)**(1/2)

print("{:.4f}".format(distancia))