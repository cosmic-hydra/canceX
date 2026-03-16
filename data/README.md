# Data Directory

This directory stores raw and processed biological datasets for the cancer genomics pipeline.

## Structure

- `raw/` - Raw tumor genome sequences and input data
  - Tumor DNA sequences (FASTQ/BAM files)
  - Normal/healthy reference genomes
  - Mutation files (VCF format)

- `processed/` - Processed and analyzed data
  - Filtered mutation calls
  - Annotated variants
  - Neoantigen predictions
  - Protein structure predictions

- `reference/` - Reference datasets
  - Human reference genome
  - Known mutation databases
  - Protein sequence databases

## Usage

Place your tumor genomic data in the `raw/` directory before running the pipeline. The pipeline will automatically process the data and store results in `processed/`.

## File Formats

- FASTQ: Raw sequencing reads
- BAM/SAM: Aligned sequencing reads
- VCF: Variant call format for mutations
- FASTA: Protein/DNA sequences
- PDB: Protein structure files

**Note**: Due to file size, genomic data files are not included in version control. Add large data files to `.gitignore`.
