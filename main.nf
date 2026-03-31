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
    uv run --directory ${projectDir} python ${projectDir}/main.py ${sam} > output.txt
    """
}

workflow {
    sam_ch = Channel.fromPath(params.sam)
    analyze_sam(sam_ch)
}
