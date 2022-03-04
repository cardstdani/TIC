l = []

l.append(float(input("Precio del producto: \n")))
l.append(int(input("Unidades: \n")))
l.append(input("Descuento (s/n)?: \n"))
l.append(input("Nombre del cliente: \n"))
l.append(input("NIF del cliente: \n"))
l.append(input("Dirección del cliente: \n"))
l.append(input("Nombre del producto: \n"))

total = round(l[0]*l[1], 2)
descuento = round(-((total)*0.10) * (1 if l[2] == "s" else 0), 2)
totalTrasDescuento = total+descuento
iva = round((total+descuento)*0.21, 2)
final = round((total+descuento) + iva, 2)

total = "{:.2f}".format(total)
descuento = "{:.2f}".format(descuento)
totalTrasDescuento = "{:.2f}".format(totalTrasDescuento)
iva = "{:.2f}".format(iva)
final = "{:.2f}".format(final)

print(
    f"{'Factura:':<30}",
    f"\n{'':<30}{l[3]:>10}",
    f"\n{'':<30}{l[5]:>10}",
    f"\n{'':<30}{l[4]:>10}",
    f"\nProducto {l[6]:>12}",
    f"\n{'Precio unitario':<30}{l[0]:>10}",
    f"\n{'Unidades':<30}{l[1]:>10}",
    f"\n{'Total':<30}{total:>10}",
    f"\n{'Descuento':<30}{descuento:>10}",
    f"\n{'Total tras descuento':<30}{totalTrasDescuento:>10}",
    f"\n{'I.V.A. (21%)':<30}{iva:>10}",
    f"\n{'Precio final':<30}{final:>10}")
