from langdetect import detect, LangDetectException


def detectar_idioma(texto: str) -> str:
    """
    Detecta el idioma de un texto dado
    """

    texto = texto.strip()

    if len(texto) < 5:
        return "El texto es demasiado corto"
    
    try:
        return detect(texto)
    except LangDetectException:
        return "No se pudo detectar el idioma"


if __name__ == "__main__":
    texto = input("Introduce un texto: ").strip()
    if not texto:
        print("No se ingresó ningún texto.")
    else:
        idioma = detectar_idioma(texto)
        print(f"Idioma detectado: {idioma}")
