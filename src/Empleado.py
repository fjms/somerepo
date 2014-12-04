__author__ = 'Fran'


class Empleado:
    """
    Clase Empleado, representa a los empleados de la empresa.
    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Constructor de la clase Empleado

        :param nombre: Nombre del empleado
        :type nombre: String
        :param apellidos: Apellido del empleado
        :type apellidos: String
        :param dni: Dni del empleado
        :type dni: String
        :param direccion: Direccion del empleado
        :type direccion: String
        :param edad: Edad del empleado
        :type edad: Integer
        :param email: Direccion de correo del empleado
        :type email: String
        :param salario: Salario anual del empleado
        :type salario: Float
        :return: None
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Devuelve el salario anual del empleado

        :return: salario
        :rtype: Float
        """
        return self.salario

    def get_dni(self):
        """
        Devuelve el dni del empleado

        :return: dni
        :rtype: String
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Devuelve el nombre y el apellido del empleado

        :return: Nombre_y_Apellidos
        :rtype: String
        """
        return self.nombre + ' ' + self.apellidos

    def get_edad(self):
        """
        Devuelve la edad del empleado

        :return: edad
        :rtype: Integer
        """
        return self.edad

    def get_email(self):
        """
        Devuelve el email del empleado

        :return: email
        :rtype: String
        """
        return self.email

    def get_direccion(self):
        """
        Devuelve la direccion del empleado

        :return: direccion
        :rtype: String
        """
        return self.direccion

    def get_salario_mensual(self):
        """
        Devuelve el salario mensual del empleado suponiendo 12 pagas anuales

        :return: salario_mensual
        :rtype: Float
        """
        return self.salario/12.0


