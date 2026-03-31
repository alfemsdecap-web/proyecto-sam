# Documentación del trabajo — proyecto-sam

## 1. ¿Qué hace el programa?

El script `main.py` analiza un fichero SAM, que es el formato estándar de salida de los alineadores de secuencias como HISAT2 o STAR. Este tipo de fichero contiene, por cada lectura, información sobre cómo se ha alineado contra el genoma de referencia: posición, calidad del alineamiento, secuencia, etc.

El programa lee el fichero línea a línea. Las líneas que empiezan por `@` son cabeceras del formato SAM y se ignoran. Para el resto, que son los alineamientos reales, extrae el valor MAPQ (columna 5), que indica la confianza con la que el alineador ha colocado esa lectura en ese punto del genoma. Un MAPQ de 60 es el valor máximo que asigna HISAT2, y significa que la lectura se ha alineado de forma única y con alta fiabilidad.

Al final, imprime tres valores: el número total de lecturas procesadas, cuántas tienen MAPQ = 60, y el porcentaje que eso representa. El resultado se muestra formateado con la librería `rich`, que añade colores y un panel visual que hace la salida más legible.

## 2. ¿Cómo se usa?

Para ejecutar el script directamente:

```bash
uv run main.py ~/dia9/nf/2-Align/WT.sam
```

Salida esperada:

```
╭──────────── Análisis SAM ────────────╮
│ Total de lecturas alineadas: 545606   │
│ Lecturas con MAPQ = 60:      294603   │
│ Porcentaje:                  54.0%    │
╰───────────────────────────────────────╯
```

También se puede ejecutar a través del pipeline de Nextflow, que recibe el fichero como parámetro:

```bash
nextflow run main.nf --sam ~/dia9/nf/2-Align/WT.sam
```

En este caso, el resultado se guarda automáticamente en la carpeta `results/output.txt`.

## 3. Organización del proyecto

El proyecto se ha inicializado con `uv`, lo que crea una estructura clara y reproducible:

```
proyecto-sam/
├── main.py          # Script principal: lee el SAM y calcula las métricas
├── main.nf          # Pipeline Nextflow que llama a main.py
├── pyproject.toml   # Define el proyecto y sus dependencias (generado por uv)
└── README.md        # Instrucciones de uso e instalación
```

`pyproject.toml` es el fichero clave del entorno `uv`: registra el nombre del proyecto, la versión de Python requerida y las dependencias externas. En este caso, la única dependencia añadida ha sido `rich`.

## 4. Uso de Git

El proyecto se ha gestionado con Git y publicado en GitHub. Se han hecho varios commits a lo largo del desarrollo, cada uno marcando un punto de avance concreto:

- **Primer commit**: estructura básica del proyecto tras `uv init`, con el `pyproject.toml` y un `main.py` inicial que ya leía el SAM e imprimía los resultados por pantalla.
- **Segundo commit**: integración de `rich` para mejorar el formato de salida, tras ejecutar `uv add rich`.
- **Tercer commit**: creación del fichero `main.nf` con el pipeline de Nextflow.
- **Cuarto commit**: `README.md` con instrucciones de uso e instalación.

Git ha sido útil sobre todo para tener un historial claro de cambios. Si algo dejaba de funcionar al añadir una nueva parte, era fácil consultar qué había cambiado y volver a una versión anterior. También ha permitido publicar el código en GitHub de forma organizada, con todos los ficheros necesarios en el repositorio.

## 5. Entorno: gestión con uv

Para crear el entorno del proyecto se ha usado `uv`, siguiendo los pasos indicados en el curso:

```bash
# Inicializar el proyecto
uv init proyecto-sam
cd proyecto-sam

# Añadir la dependencia externa
uv add rich
```

El comando `uv init` crea el `pyproject.toml` y la estructura básica del proyecto. `uv add rich` añade `rich` como dependencia y la registra automáticamente en el `pyproject.toml`. No hace falta gestionar manualmente ningún entorno virtual: `uv` lo crea y mantiene de forma transparente.

Para que el proyecto funcione en otra máquina, basta con clonar el repositorio y ejecutar:

```bash
uv sync
```

Esto instala exactamente las versiones de las dependencias definidas en el proyecto. Con `uv run main.py <fichero.sam>` se ejecuta el script dentro del entorno correcto, sin tener que activar nada manualmente.

## 6. Problemas encontrados

**Índice de la columna MAPQ.** El formato SAM describe MAPQ como la columna 5, pero al dividir la línea en Python con `split("\t")`, la indexación empieza en 0. Por tanto, la columna 5 del SAM es el elemento en la posición 4 de la lista. Es un detalle pequeño pero que genera un error de resultado difícil de detectar si no se revisa el formato SAM con cuidado.

**Salida de `rich` en Nextflow.** Al redirigir la salida del script hacia un fichero (`> output.txt`), los caracteres de color de `rich` podrían aparecer como secuencias de escape ANSI en el fichero de texto. Afortunadamente, `rich` detecta automáticamente si está escribiendo a un terminal o a un fichero, y en el segundo caso suprime los colores. El fichero `output.txt` resultante es texto limpio y legible.
