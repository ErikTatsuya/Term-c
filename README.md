# Term-c

Biblioteca simples para interfaces de terminal em Python.

## Instalação

```bash
pip install git+https://github.com/ErikTatsuya/Term-c.git
```

## Uso

```python
from terminal import Terminal

terminal = Terminal()

terminal.box(
    "Olá mundo",
    style="double",
    color=terminal.green
)
```

Tem outros usos também, veja o terminal/terminal_cli.py
