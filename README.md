# SantoRosarioMinimas
Aplicación renovada del santo rosario rezado por las madres minimas de la ciudad de México

## Características

- **Rezo Automático**: Reza el rosario del día según el calendario litúrgico
- **Selección Manual**: Elige qué tipo de misterios rezar (Gozosos, Dolorosos o Gloriosos)
- **Misterio Individual**: Reza un solo misterio específico (del 1 al 15)

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python rosario_app.py
```

### Controles

- **Rezar Rosario de Hoy**: Inicia automáticamente el rosario con los misterios del día
- **Seleccionar Misterios**: Elige manualmente qué tipo de misterios rezar
- **Rezar Misterio Individual**: Selecciona un misterio específico

Durante la reproducción:
- **Pausa/Play**: Pausa o reanuda
- **Detener**: Vuelve al menú principal

## Estructura del Audio

Rosario completo: Inicio → (Misterio → Canto) x5 → Final

Misterio individual: M.mp3

