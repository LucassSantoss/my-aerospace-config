#!/usr/bin/env python3
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).parent / ".aerospace.toml"
DEST = Path.home() / ".aerospace.toml"


def main():
    if not SOURCE.exists():
        print(f"Erro: arquivo de origem não encontrado: {SOURCE}")
        sys.exit(1)

    if DEST.exists():
        backup = DEST.with_suffix(".toml.bak")
        shutil.copy2(DEST, backup)
        print(f"Backup criado: {backup}")

    shutil.copy2(SOURCE, DEST)
    print(f"Configuração instalada em: {DEST}")


if __name__ == "__main__":
    main()
