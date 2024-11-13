import os
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

datos = [
    ("Nombre", "Edad", "Ciudad"), 
    ("Juan", 25, "Madrid"),
    ("María", 30, "Barcelona"),
    ("Carlos", 28, "Valencia")
]

for fila in datos:
    sheet.append(fila)

ruta_completa = os.path.abspath("ejemplo.xlsx")
print(f"El archivo se guardará en: {ruta_completa}")

wb.save("ejemplo.xlsx")
