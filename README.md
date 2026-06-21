# learn-gh-actions

Sandbox para aprender GitHub Actions rompiendo cosas de forma controlada.

Cada módulo es independiente: puedes introducir un error en un test, un fallo de lint o un import roto y observar cómo reacciona el pipeline sin afectar al resto.

## Estructura

| Archivo | Qué hace |
|---|---|
| `speed_tools.py` | Conversiones de velocidad y cálculo de distancia de frenado |
| `test_speed_tools.py` | Tests pytest para `speed_tools` |

## Cómo usarlo

```bash
pip install pytest
pytest
```

## Ideas para experimentar

- Romper un test → ver qué job falla y cuál pasa
- Introducir un error de sintaxis → ver cuándo lo detecta el pipeline
- Añadir un step de lint (ruff, flake8) y violar una regla
- Probar matrix builds con distintas versiones de Python
