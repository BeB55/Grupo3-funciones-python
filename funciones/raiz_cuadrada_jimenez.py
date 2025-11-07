import math

def raiz_cuadrada_jimenez(x):
  """
  Devuelve la raíz cuadrada de un número positivo.
  Función de Jimenez.
  """
  if x < 0:
    return None
  
  # Usamos math.sqrt() para la operación
  return math.sqrt(x)