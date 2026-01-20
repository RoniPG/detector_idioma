from langdetect import detect, LangDetectException


def detectar_idioma(texto: str) -> str:
    """
    Detecta el idioma de un texto dado
    """
    try:
        return detect(texto)
    except LangDetectException:
        return "Idioma no detectable"


if __name__ == "__main__":
    texto = input("Introduce un texto: ").strip()
    if not texto:
        print("No se ingresó ningún texto.")
    else:
        idioma = detectar_idioma(texto)
        print(f"Idioma detectado: {idioma}")
