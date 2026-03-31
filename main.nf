#!/usr/bin/env nextflow

params.sam = "WT.sam"

process analyze_sam {

    publishDir "results/", mode: 'copy'

    input:
    path sam

    output:
    file "output.txt"

    script:
    """
    SAM_ABS=\$(readlink -f ${sam})
    uv run --directory ${projectDir} python ${projectDir}/main.py \$SAM_ABS > output.txt

    """
}

workflow {
    sam_ch = Channel.fromPath(params.sam)
    analyze_sam(sam_ch)
}
