__author__ = 'Fran'


class Departamento:
    """
    Clase Departamento, representa los departamentos de la empresa.

    """
    def __init__(self, nombre_depto, id_depto):
        """
        Constructor de la clase Departamento

        :param nombre_depto: Nombre del departamento
        :type nombre_depto: String
        :param id_depto: Identificacion del departamento
        :type id_depto: Integer
        :return: None
        """
        self.nombre_dep = nombre_depto
        self.id_dep = id_depto
        self.listaEmpleados = []

    def aniadir_empleado(self, empleado):
        """
        Aniade un empleado a la lista interna del departamento

        :param empleado: Empleado a aniadir a la lista interna de empleados
        :type empleado: Empleado
        :return: None
        """
        self.listaEmpleados.append(empleado)

    def get_salario_total(self):
        """
        Devuelve el salario total de todos los empleados del departamento

        :return: salario
        :rtype: Float
        """
        suma = 0
        for emp in self.listaEmpleados:
            suma = suma + emp.get_salario()
        return suma

    def get_nombre_depto(self):
        """
        Devuelve el nombre del departamento

        :return: Nombre del departamento
        :rtype: String
        """
        return self.nombre_dep

    def get_salario_total_mensual(self):
        """
        Devuelve el salario total mensual de todos los empleados del departamento

        :return: Salario total mensual de todos los empleados
        :rtype: Float
        """
        suma = 0
        for emp in self.listaEmpleados:
            suma = suma + emp.get_salario_mensual()
        return suma