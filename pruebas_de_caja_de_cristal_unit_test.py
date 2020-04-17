import unittest

def es_mayor_de_edad_(edad):
    if(edad >=18):
        return True
    return False

class prueba_de_cristal_test(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad=20
        resiultado= es_mayor_de_edad_(edad)
        self.assertEqual(resiultado, True)
    def test_es_menor_de_edad(self):
        edad=15 
        resultado=es_mayor_de_edad_(edad)

        self.assertEqual(resultado,False)

if __name__=='__main__':
    unittest.main()