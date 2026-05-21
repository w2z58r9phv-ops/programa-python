print("Restaurante- Comida Rapida-: Donde Simon")

menu = [
    ["Hamburguesa", "Comida", 18000],
    ["Pizza", "Comida", 25000],
    ["Gaseosa", "Bebida", 12000],
    ["Jugo Natural", "Bebida", 9000],
    ["Helado", "Postre", 8000],
    ["Café", "Bebida", 15000]
]

categoria_objetivo = "Bebida"
umbral = 10000

def calcular_precio_final(categoria, precio_base):

    if categoria == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final

print("=== MENÚ CON PROMOCIÓN ===\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: ${precio_base}")
    print(f"Precio Final: ${precio_final:.0f}")
    print("--------------------------")
