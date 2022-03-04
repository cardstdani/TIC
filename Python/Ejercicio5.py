l = []

l.append(float(input("Precio del producto: \n")))
l.append(int(input("Unidades: \n")))
l.append(input("Descuento (s/n)?: \n"))
l.append(input("Nombre del cliente: \n"))
l.append(input("NIF del cliente: \n"))
l.append(input("Dirección del cliente: \n"))
l.append(input("Nombre del producto: \n"))

total = round(l[0]*l[1], 2)
descuento = round(-((total)*0.15) * (1 if l[2] == "s" else 0), 2)
iva = round((total+descuento)*0.21, 2)

print(
    f"{'Factura:':<15}",
    f"\n{'':<15}{l[3]:>10}",
    f"\n{'':<15}{l[5]:>10}",
    f"\n{'':<15}{l[4]:>10}",
    f"\n{'Producto '}{l[6]}",
    f"\n{'Precio unitario':<15}{l[0]:>10}",
    f"\n{'Unidades':<15}{l[1]:>10}",
    f"\n{'Total':<15}{total:>10}",
    f"\n{'Descuento':<15}{descuento:>10}",
    f"\n{'Total tras descuento':<15}{total+descuento:>10}",
    f"\n{'I.V.A. (21%)':<15}{iva:>10}",
    f"\n{'Precio final':<15}{round((total+descuento) + iva, 2):>10}",
)
