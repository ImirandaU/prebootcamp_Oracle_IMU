
import csv

# 1. Lista de ventas original
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 800.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 10, "precio": 20.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 820.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 5, "precio": 30.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 4, "precio": 22.0},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 3, "precio": 28.0},
]

# 2. Cálculo de ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 3. Producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 4. Precio promedio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    total_precio = venta["precio"] * venta["cantidad"]
    cantidad = venta["cantidad"]
    if producto in precios_por_producto:
        suma_precio, total_cantidad = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precio + total_precio, total_cantidad + cantidad)
    else:
        precios_por_producto[producto] = (total_precio, cantidad)

# 5. Ingresos por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# 6. Resumen de ventas
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos = precios_por_producto[producto][0]
    promedio = ingresos / cantidad_total
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": round(ingresos, 2),
        "precio_promedio": round(promedio, 2)
    }

# Mostrar resultados por pantalla
print(f"Ingresos totales: ${ingresos_totales:.2f}")
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)\n")

print("Precio promedio por producto:")
for producto, (suma_precio, total_cantidad) in precios_por_producto.items():
    print(f"{producto}: ${suma_precio / total_cantidad:.2f}")
print()

print("Ingresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso:.2f}")
print()

print("Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"{producto}: {resumen}")

# 7. Exportar resumen a CSV
with open("resumen_ventas.csv", mode="w", newline="") as archivo_csv:
    campos = ["producto", "cantidad_total", "ingresos_totales", "precio_promedio"]
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    for producto, datos in resumen_ventas.items():
        fila = {"producto": producto}
        fila.update(datos)
        escritor.writerow(fila)

print("\nArchivo 'resumen_ventas.csv' creado con éxito.")
