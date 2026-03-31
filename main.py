#!/usr/bin/env python3

import sys


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

    print(f"Total de lecturas alineadas: {total}")
    print(f"Lecturas con MAPQ = 60: {mapq60}")
    print(f"Porcentaje: {pct:.1f}%")


if __name__ == "__main__":
    main()
