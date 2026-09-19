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

    hora_invalida = hora_entrada < 0 or hora_entrada > 23
    permanencia_invalida = horas_permanencia <= 0

    if hora_invalida or permanencia_invalida:
        print("Error: registro invalido (hora fuera de rango o permanencia <= 0). Vehiculo no contado.")
    else:
        advertencia = False
        if tipo != "E" and tipo != "D" and tipo != "V":
            tipo = "V"
            advertencia = True

        if tipo == "E":
            if horas_permanencia <= 2:
                tarifa = 0.0
            else:
                horas_adicionales = horas_permanencia - 2
                tarifa = horas_adicionales * 800
        elif tipo == "D":
            tarifa = horas_permanencia * 500
        else:
            if horas_permanencia <= 1:
                tarifa = 1500.0
            else:
                horas_adicionales = horas_permanencia - 1
                tarifa = 1500 + horas_adicionales * 1200
            if es_sabado:
                tarifa = tarifa * 0.8
                # Descuento nocturno: NO aplica si es sabado (logica reordenada)
        if (hora_entrada >= 19 or hora_entrada < 6) and not es_sabado:
            tarifa = tarifa * 0.9

        tarifa = round(tarifa, 2)

        registrados += 1
        total_recaudo += tarifa
        suma_horas += horas_permanencia

        if tipo == "E":
            count_estudiantes += 1
        elif tipo == "D":
            count_docentes += 1
        else:
            count_visitantes += 1

        print(f"Vehiculo {placa} registrado como {tipo}. Tarifa: ${tarifa}")
        if advertencia:
            print("Advertencia: tipo de usuario no reconocido, se trato como visitante.")

        if registrados == CUPOS:
            print("PARQUEADERO LLENO")

    i += 1