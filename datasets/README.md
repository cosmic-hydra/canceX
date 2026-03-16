# Datasets Module

Scripts for downloading and loading public cancer genomics datasets.

## Available Datasets

### TCGA (The Cancer Genome Atlas)
- Comprehensive cancer genomics data
- Access: https://portal.gdc.cancer.gov/
- Required: GDC Data Transfer Tool for full dataset

### COSMIC (Catalogue Of Somatic Mutations In Cancer)
- Database of somatic mutations in cancer
- Access: https://cancer.sanger.ac.uk/cosmic
- Required: Registration and license agreement

### ICGC (International Cancer Genome Consortium)
- International cancer genomics data
- Access: https://dcc.icgc.org/
- Required: DACO approval for controlled access

## Usage

### Download Datasets
```python
from datasets.download_datasets import DatasetDownloader

downloader = DatasetDownloader(output_dir="../data/reference")
downloader.download_tcga_sample_data(cancer_type="BRCA")
```

### Load and Standardize Data
```python
from datasets.loader import DatasetLoader

loader = DatasetLoader(data_dir="../data/reference")
mutations_df = loader.load_mutations("path/to/mutations.vcf")
standardized_df = loader.standardize_mutation_format(mutations_df)
```

## Data Format Standards

All mutation data is standardized to include:
- `chromosome`: Chromosome identifier
- `position`: Genomic position
- `ref`: Reference allele
- `alt`: Alternate allele
- `gene`: Gene symbol (when available)
