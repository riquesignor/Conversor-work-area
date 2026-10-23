import os
import platform
import sys
from pathlib import Path


def pasta_area_de_trabalho() -> Path:
    return Path.home() / "Desktop"


def criar_atalho_linux(alvo: Path, pasta: Path) -> None:
    atalho = pasta / "Conversor de Imagens.desktop"
    conteudo = f"""[Desktop Entry]
Type=Application
Name=Conversor de Imagens
Exec={sys.executable} {alvo}
Terminal=false
"""
    atalho.write_text(conteudo, encoding="utf-8")
    atalho.chmod(0o755)
    print(f"Atalho criado em: {atalho}")


def criar_atalho_windows(alvo: Path, pasta: Path) -> None:
    # Cria um .bat simples que abre o script (sem depender de bibliotecas extras)
    atalho = pasta / "Conversor de Imagens.bat"
    conteudo = f'@echo off\r\n"{sys.executable}" "{alvo}"\r\npause\r\n'
    atalho.write_text(conteudo, encoding="utf-8")
    print(f"Atalho criado em: {atalho}")


if __name__ == "__main__":
    alvo = Path(__file__).parent / "gui.py"
    pasta = pasta_area_de_trabalho()
    pasta.mkdir(parents=True, exist_ok=True)

    if platform.system() == "Windows":
        criar_atalho_windows(alvo, pasta)
    else:
        criar_atalho_linux(alvo, pasta)