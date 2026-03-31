# proyecto-sam

Script en Python para analizar ficheros SAM: cuenta el total de lecturas alineadas y cuántas tienen un valor de MAPQ igual a 60.

## Requisitos

- Python >= 3.11
- [uv](https://github.com/astral-sh/uv) (gestor de proyectos y dependencias)
- Nextflow (para ejecutar el pipeline)

## Instalación

Clona el repositorio e instala las dependencias con `uv`:

```bash
git clone https://github.com/<tu-usuario>/proyecto-sam.git
cd proyecto-sam
uv sync
```

## Uso

### Ejecución directa

```bash
uv run main.py ~/dia9/nf/2-Align/WT.sam
```

Salida esperada:

```
╭─────────── Análisis SAM ───────────╮
│ Total de lecturas alineadas:  153284 │
│ Lecturas con MAPQ = 60:        81234 │
│ Porcentaje:                    53.0% │
╰──────────────────────────────────────╯
```

### Ejecución con Nextflow

```bash
nextflow run main.nf --sam ~/dia9/nf/2-Align/WT.sam
```

El resultado se guarda en `results/output.txt`.

## Estructura del proyecto

```
proyecto-sam/
├── main.py          # Script principal de análisis
├── main.nf          # Pipeline Nextflow
├── pyproject.toml   # Configuración del proyecto (uv)
└── README.md        # Este fichero
```
