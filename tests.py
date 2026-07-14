import json

# Simulación del output que recibes de la IA
data_from_ai = '{"titulo": "Caloventor 2000W", "descripcion": "Ideal para invierno", "redes": "Oferta increíble"}'

def test_json_structure():
    try:
        data = json.loads(data_from_ai)
        assert "titulo" in data
        assert "descripcion" in data
        print("Test pasado: El JSON tiene la estructura correcta.")
    except Exception as e:
        print(f"Test fallido: {e}")

if __name__ == "__main__":
    test_json_structure()
