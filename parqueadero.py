CUPOS = 30

n = int(input("Ingrese el numero de vehiculos a registrar (N): "))
es_sabado_str = input("Es sabado? (True/False): ")
es_sabado = es_sabado_str.strip().lower() == "true"

registrados = 0
total_recaudo = 0.0
count_estudiantes = 0
count_docentes = 0
count_visitantes = 0
suma_horas = 0.0

i = 0
while i < n and registrados < CUPOS:
    print(f"\n--- Vehiculo {i + 1} ---")
    placa = input("Placa: ")
    tipo = input("Tipo de usuario (E/D/V): ").strip().upper()
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas que permanecera parqueado: "))

    i += 1