__author__ = 'Fran'


class Departamento:
    def __init__(self, nombre_depto, id_depto):
        self.nombre_dep = nombre_depto
        self.id_dep = id_depto
        self.listaEmpleados = []

    def aniadir_empleado(self, empleado):
        self.listaEmpleados.append(empleado)

    def get_salario_total(self):
        suma=0
        for emp in self.listaEmpleados:
            suma=suma+emp.get_salario()
        return suma

    def get_nombre_depto(self):
        return self.nombre_dep

    def get_salario_total_mensual(self):
        suma=0
        for emp in self.listaEmpleados:
            suma=suma+emp.get_salario_mensual()
        return suma
    
