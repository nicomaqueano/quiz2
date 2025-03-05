from empresa import *

def main():
    n_empleados = int(input("Ingrese el número de empleados: "))
    mes = input("Ingrese el mes de trabajo: ")
    empresa = Empresa(n_empleados, mes)
    for i in range(n_empleados):
        empresa.añadir_empleado(i)
    empresa.calcular_pagos()
    empresa.resumir()

main()

