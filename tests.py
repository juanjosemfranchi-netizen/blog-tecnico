import json

data_from_ai = '{"titulo": "Caloventor 2000W", "descripcion": "Ideal para invierno", "redes": "Oferta increíble"}'

REQUIRED_FIELDS = ["titulo", "descripcion", "redes"]

def validate_ai_output(payload: str) -> dict:
    data = json.loads(payload)  # si no es JSON, levanta excepción

    for field in REQUIRED_FIELDS:
        assert field in data, f"Falta el campo obligatorio: {field}"
        assert isinstance(data[field], str) and data[field].strip(), f"Campo inválido o vacío: {field}"

    return data

def test_json_structure():
    try:
        validate_ai_output(data_from_ai)
        print("Test pasado: El JSON cumple la estructura y campos obligatorios.")
    except Exception as e:
        raise AssertionError(f"Test fallido: {e}")

if __name__ == "__main__":
    test_json_structure()
