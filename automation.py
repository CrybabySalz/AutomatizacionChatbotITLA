import unittest
from chatbot import get_response

def test_horario_trabajo_ITLA():
    pregunta = "En qué horario trabaja el ITLA"
    respuesta_esperada = "El ITLA labora de lunes a viernes de 8:00 a.m. a 5:00 p.m."
    
    # Obtener la respuesta del chatbot
    respuesta_obtenida = get_response(pregunta)
    
    # Verificar si la respuesta obtenida es la esperada
    assert respuesta_obtenida == respuesta_esperada, f"Respuesta inesperada: {respuesta_obtenida}"

if __name__ == '__main__':
    test_horario_trabajo_ITLA()
