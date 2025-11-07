from funciones.raiz_cuadrada_jimenez import raiz_cuadrada_jimenez

def test_raiz_cuadrada_jimenez():
  """Prueba la función de raiz_cuadrada_jimenez."""
  
  # Probamos que funcione correctamente
  assert raiz_cuadrada_jimenez(9) == 3
  assert raiz_cuadrada_jimenez(25) == 5
  assert raiz_cuadrada_jimenez(0) == 0
  
  # Probamos el caso especial (números negativos)
  assert raiz_cuadrada_jimenez(-4) is None
  assert raiz_cuadrada_jimenez(-100) is None