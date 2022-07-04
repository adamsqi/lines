from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

lista_elementow = []
for obj in acad.iter_objects():
    print(obj.ObjectName)
    lista_elementow.append(obj)
print(lista_elementow)

print(len(lista_elementow))
print("current layer: "  + lista_elementow[6].Layer)

lista_projektowane_linie = []

for i in range(len(lista_elementow)):
    if lista_elementow[i].Layer == 'Proli':
        lista_projektowane_linie.append(lista_elementow[i])

print(lista_projektowane_linie)

pz1 = []

for i in range(len(lista_elementow)):
    print(lista_projektowane_linie[0].IntersectWith(lista_elementow[i],0))
    if len(lista_projektowane_linie[0].IntersectWith(lista_elementow[i],0)) > 0:
        pz1.append(lista_projektowane_linie[0].IntersectWith(lista_elementow[i],0))
print(pz1)

for i in range(len(pz1)):
    acad.model.AddLine(APoint(pz1[i][0],pz1[i][1]),APoint(pz1[i][0],pz1[i][1]+30))
    
    





