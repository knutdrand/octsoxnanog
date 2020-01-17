rule trim:
    input:
        "reads/{name}.fastq.gz"
    output:
        temp("trimmed_reads/{name}.fastq.gz")
    shell:
        'cutadapt -a "GATCGGAAGAGCACACGTCTGAACTCCAGTCAC" -m 20 {input} | cutadapt -a "AATGATACGGCGACCACCGAGATCTACAC" -m 20 - -o {output}'

rule map:
    input:
        "trimmed_reads/{name}.fastq.gz"
    output:
        temp("mapped_reads/{name}.bam")
    shell:
        "bwa mem ../data/mm10.fa -t 16 {input} | samtools view -q 30 -S -b > {output}"

rule sort:
    input:
        "mapped_reads/{name}.bam"
    output:
        temp("sorted_reads/{name}.bam")
    shell:
        "samtools sort {input} -o {output}"

rule bamtobed:
    input:
        "sorted_reads/{name}.bam"
    output:
        temp("mapped_bed/{name}.bed")
    shell:
        "bedtools bamtobed -i {input} > {output}"

rule filter_dup:
    input:
        "mapped_bed/{name}.bed"
    output:
        "unique_bed/{name}.bed"
    shell:
        "macs2 filterdup -i {input} -o {output}"

rule callpeak:
    input:
        "unique_bed/{name}.bed"
    output:
        temp("macs_output/{name}_treat_pileup.bdg"),
        temp("macs_output/{name}_control_lambda.bdg"),
	"macs_output/{name}_peaks.narrowPeak"
    shell:
        "macs2 callpeak -t {input} -g mm --bdg --outdir macs_output -n {wildcards.name}"

rule create_pileup_track:
    input:
        "macs_output/{name}_treat_pileup.bdg"
    output:
        "macs_output/{name}_treat_pileup.bw"
    shell:
        "./bdg2bw {input} mm10.chrom.sizes"

rule create_peak_track:
    input:
        "macs_output/{name}_peaks.narrowPeak"
    output:
        "macs_output/{name_peaks.bb}"
    shell:
        "./narrowPeak2bb.sh {input} mm10.chrom.sizes"

rule move_track:
    input:
        "macs_output/{filename}"
    output:
        "../../var/www/html/trackhub_knut/mm10/{filename}"
    shell:
        "mv {input} {output}"
