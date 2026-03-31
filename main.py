#!/usr/bin/env python3

import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def analyze_sam(sam_path: str) -> tuple[int, int, float]:
    """Lee un fichero SAM y devuelve el total de lecturas, las que
    tienen MAPQ=60 y el porcentaje correspondiente."""
    total_reads = 0
    mapq60_reads = 0

    with open(sam_path, "r") as f:
        for line in f:
            # Las cabeceras SAM empiezan por '@' y se ignoran
            if line.startswith("@"):
                continue

            fields = line.strip().split("\t")
            # La columna 5 del SAM (índice 4) es el valor MAPQ
            mapq = int(fields[4])
            total_reads += 1

            if mapq == 60:
                mapq60_reads += 1

    percentage = (mapq60_reads / total_reads * 100) if total_reads > 0 else 0.0
    return total_reads, mapq60_reads, percentage


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <fichero.sam>")
        sys.exit(1)

    sam_path = sys.argv[1]
    total, mapq60, pct = analyze_sam(sam_path)

    console = Console()

    result = Text()
    result.append("Total de lecturas alineadas: ", style="bold white")
    result.append(f"{total}\n", style="green")
    result.append("Lecturas con MAPQ = 60:      ", style="bold white")
    result.append(f"{mapq60}\n", style="cyan")
    result.append("Porcentaje:                  ", style="bold white")
    result.append(f"{pct:.1f}%", style="yellow bold")

    console.print(Panel(result, title="[bold blue]Análisis SAM[/bold blue]", border_style="blue"))


if __name__ == "__main__":
    main()
