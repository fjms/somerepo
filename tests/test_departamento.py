from unittest import TestCase

from mockito import *

from src import Departamento
from src import Empleado


__author__ = 'Fran'


class TestDepartamento(TestCase):
    """
    Clase que realiza los test sobre la clase Departamento
    """
    def test_get_salario_total(self):
        """
        Comprueba la funcionalidad  get_salario_total de la clase Departamento

        :return: None
        """
        pepe = mock(Empleado.Empleado)
        fran = mock(Empleado.Empleado)
        juan = mock(Empleado.Empleado)
        when(pepe).get_salario().thenReturn(1200)
        when(fran).get_salario().thenReturn(2000)
        when(juan).get_salario().thenReturn(500)
        dep = Departamento.Departamento("RRHH", 001)
        dep.listaEmpleados = [pepe, fran, juan]
        self.assertEqual(dep.get_salario_total(), 3700)
        # self.assertIsNotNone(dep.get_salario_total())

    def test_get_salario_total_mensual(self):
        """
        Comprueba la funcionalidad get_salario_total_mensual de la clase
        Departamento

        :return: None
        """
        pepe = mock(Empleado.Empleado)
        fran = mock(Empleado.Empleado)
        juan = mock(Empleado.Empleado)
        when(pepe).get_salario_mensual().thenReturn(2000)
        when(fran).get_salario_mensual().thenReturn(2000)
        when(juan).get_salario_mensual().thenReturn(2500)
        dep = Departamento.Departamento("RRHH", 001)
        dep.listaEmpleados = [pepe, fran, juan]
        self.assertEqual(dep.get_salario_total_mensual(), 6500)
