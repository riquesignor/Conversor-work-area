from pathlib import Path
from PIL import Image

FORMATOS_SAIDA = {"jpg", "png", "webp"}


def converter_imagem(caminho_entrada: str, formato_saida: str) -> Path:
    """Converte uma imagem para o formato indicado e retorna o caminho do novo arquivo."""
    formato_saida = formato_saida.lower().lstrip(".")
    if formato_saida not in FORMATOS_SAIDA:
        raise ValueError(f"Formato não suportado: {formato_saida}")

    origem = Path(caminho_entrada)
    if not origem.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado: {origem}")

    destino = origem.with_suffix(f".{formato_saida}")

    with Image.open(origem) as img:
        # JPG não suporta transparência, então converte para RGB
        if formato_saida == "jpg" and img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(destino)

    return destino


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: python conversor.py <arquivo> <formato>")
        sys.exit(1)

    novo = converter_imagem(sys.argv[1], sys.argv[2])
    print(f"Convertido: {novo}")