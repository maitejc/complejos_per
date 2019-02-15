import unittest
class Complejo(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        
    def multiplicacion(self, otro):
        result = Complejo((self.real*otro.real-self.imag*otro.imag),(self.imag*otro.real+self.real*otro.imag))
        return result
        
    def division(self,otro):
        numerador = Complejo((self.real*otro.real-self.imag*otro.imag),(self.imag*otro.real+self.real*otro.imag))
        denominador = Complejo((otro.real**2) + (otro.imag**2))
        return numerador, "/", denominador


c1 = Complejo(5,1)
c2 = Complejo(8,6)
print(c1.multiplicacion(c2))

class TestComplejo(unittest.TestCase):
    def test_multiplicar(self):
        c1 = Complejo(5,1)
        c2 = Complejo(8,6) 
        multiplicacion = c1.multiplicacion(c2)
        self.assertEqual(multiplicacion.real, 34)
        self.assertEqual(multiplicacion.imag, 38)
        
c = TestComplejo()
print(c.test_multiplicar())
