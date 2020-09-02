from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertAlmostEqual(0, motor.velocidade)

# Não esquecer de importar TestCase e começar a função com o prefixo teste
