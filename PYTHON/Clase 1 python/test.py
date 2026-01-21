def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Definimos la estructura de las materias y cuántas notas tiene cada una
configuracion = {
    "Materia 1": 5,
    "Materia 2": 4,
    "Materia 3": 5
}

promedios_materias = []

print("--- SISTEMA DE CALIFICACIONES ---")

# Proceso para cada materia
for nombre_materia, cantidad_notas in configuracion.items():
    print(f"\nIngresando notas para {nombre_materia}:")
    notas = []
    
    for i in range(cantidad_notas):
        nota = float(input(f"  Nota {i+1}: "))
        notas.append(nota)
    
    promedio_m = calcular_promedio(notas)
    promedios_materias.append(promedio_m)
    
    # Validar si aprobó la materia individual
    estado = "Aprobada" if promedio_m >= 4.0 else "No aprobada"
    print(f"  > Promedio {nombre_materia}: {promedio_m:.2f} - {estado}")

# --- CÁLCULO DEL PROMEDIO GENERAL ---
promedio_general = sum(promedios_materias) / len(promedios_materias)

print("\n" + "="*30)
print(f"PROMEDIO GENERAL FINAL: {promedio_general:.2f}")

# Lógica de decisión final
if promedio_general <= 3.9:
    print("ESTADO: Promedio insuficiente, volver a rendir.")
elif 4.0 <= promedio_general <= 4.9:
    print("ESTADO: Rendir Exámenes.")
else: # Para 5.0 o superior
    print("ESTADO: Aprobado.")
print("="*30)