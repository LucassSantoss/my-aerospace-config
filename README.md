# my-aerospace-config

Configuração pessoal do [AeroSpace](https://github.com/nikitabobko/AeroSpace), gerenciador de janelas para macOS.

## Requisitos

- macOS
- [AeroSpace](https://github.com/nikitabobko/AeroSpace) instalado
- Python 3

## Instalação

Clone o repositório e rode o script de instalação:

```bash
git clone https://github.com/LucasssSantoss/my-aerospace-config.git
cd my-aerospace-config
python3 install.py
```

O script copia `.aerospace.toml` para `~/.aerospace.toml`. Se já existir uma configuração anterior, um backup é criado automaticamente em `~/.aerospace.toml.bak`.

## Atualização

Após fazer alterações no repositório, rode novamente:

```bash
python3 install.py
```
