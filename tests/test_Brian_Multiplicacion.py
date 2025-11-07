import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones.Brian_Multiplicacion import multiplicar

def test_multiplicar(): 
    assert multiplicar(3, 4) == 12 
    assert multiplicar(-2, 5) == -10