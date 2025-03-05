def es_primo(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def es_def(n):
    suma = 1
    for i in range(2, n - 1):
        if n % i == 0:
            suma += i
    if suma < n:
        return True
    return False


class Empresa:
    def __init__(self, n_empleados, mes_trabajo):
        self.tarifas = {
            "ingeniero": 25,
            "arquitecto": 10,
            "obrero": 5
        }
        self.mes_trabajo = mes_trabajo
        self.empleados = {}
        self.monto_pagado = 0

    def añadir_empleado(self, idx):
        print(f"--- Empleado {idx + 1} ---")
        nom = input("Ingrese el nombre del empleado: ")
        ap = input("Ingrese el apellido del empleado: ")
        ced = input("Ingrese la cédula del empleado: ")
        cargo = input("Ingrese el cargo del empleado: ")
        esp = input("Ingrese la especialidad del empleado: ")
        datos_personales = {
            "nombre": nom,
            "apellido": ap,
            "cédula": ced,
            "cargo": cargo,
            "especialidad": esp
        }
        self.empleados[idx] = Empleado(self, datos_personales)
    
    def calcular_pagos(self):
        for empleado in self.empleados.values():
            empleado.calcular_pago()

    def resumir(self):
        print("Resumen de la empresa:")
        print(f"Mes de trabajo: {self.mes_trabajo}")
        print(f"Empleados: {len(self.empleados)}")
        pago_ing, pago_arq, pago_obr = [], [], []
        m1, m2, m3 = 0, 0, 0
        for empleado in self.empleados.values():
            if empleado.datos["cargo"] == "ingeniero":
                pago_ing.append(empleado.pago)
                if empleado.pago > m1:
                    m1 = empleado.pago
                    max_ing = empleado
            elif empleado.datos["cargo"] == "arquitecto":
                pago_arq.append(empleado.pago)
                if empleado.pago > m2:
                    m2 = empleado.pago
                    max_arq = empleado
            elif empleado.datos["cargo"] == "obrero":
                pago_obr.append(empleado.pago)
                if empleado.pago > m3:
                    m3 = empleado.pago
                    max_obr = empleado
        print(f"Monto total pagado: {self.monto_pagado}")
        print(f"Cantidad de ingenieros: {len(pago_ing)}")
        print(f"Cantidad de arquitectos: {len(pago_arq)}")
        print(f"Cantidad de obreros: {len(pago_obr)}")
        print(f"Promedio de pago para ingenieros: {sum(pago_ing) / len(pago_ing)}")
        print(f"Promedio de pago para arquitectos: {sum(pago_arq) / len(pago_arq)}")
        print(f"Promedio de pago para obreros: {sum(pago_obr) / len(pago_obr)}")
        print(f"Ingeniero con más pago: {max_ing.datos['nombre']} {max_ing.datos['apellido']} con un pago de {max_ing.pago}")
        print(f"Arquitecto con más pago: {max_arq.datos['nombre']} {max_arq.datos['apellido']} con un pago de {max_arq.pago}")
        print(f"Obrero con más pago: {max_obr.datos['nombre']} {max_obr.datos['apellido']} con un pago de {max_obr.pago}")


class Empleado():
    def __init__(self, empresa, datos_personales):
        self.datos = datos_personales
        self.empresa = empresa
        self.honorarios = empresa.tarifas[self.datos["cargo"]]
        self.horas = None
    
    def registrar_horas(self):
        self.horas = int(input(f"Ingrese el número de horas que {self.datos['nombre']} trabajó en el mes de {self.empresa.mes_trabajo}: "))
    
    def calcular_pago(self):
        if not self.horas:
            print("Para calcular el pago del mes, debe registrar las horas trabajadas.")
            self.registrar_horas()
        self.pago = self.horas * self.honorarios
        if es_primo(self.horas):
            self.pago *= 1.05
        if es_def(int(self.pago)):
            self.pago *= 1.1
        self.empresa.monto_pagado += self.pago
    
