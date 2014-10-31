from unittest import TestCase
from mockito import *
from Empleado import *
from Departamento import *

__author__ = 'Fran'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        pepe = mock(Empleado)
        fran = mock(Empleado)
        juan = mock(Empleado)
        when(pepe).get_salario().thenReturn(1200)
        when(fran).get_salario().thenReturn(2000)
        when(juan).get_salario().thenReturn(500)
        dep = Departamento("RRHH", 001)
        dep.listaEmpleados = [pepe, fran, juan]
        self.assertEqual(dep.get_salario_total(), 3700)
        # self.assertIsNotNone(dep.get_salario_total())

    def test_get_salario_total_mensual(self):
        pepe = mock(Empleado)
        fran = mock(Empleado)
        juan = mock(Empleado)
        when(pepe).get_salario_mensual().thenReturn(2000)
        when(fran).get_salario_mensual().thenReturn(2000)
        when(juan).get_salario_mensual().thenReturn(2500)
        dep = Departamento("RRHH", 001)
        dep.listaEmpleados = [pepe, fran, juan]
        self.assertEqual(dep.get_salario_total_mensual(), 5500)
