__author__ = 'Fran'


class Empresa:
    """
    Clase Empresa, necesaria para crear una nueva empresa
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        Constructor de la clase Empresa

        :param nombre_empresa: Nombre de la empresa
        :type nombre_empresa: String
        :param cif: Numero CIF de la empresa
        :type cif: String
        :param razon_social: Domicilio de la empresa
        :type razon_social: String
        :return: None
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.listaDepartamentos = []
