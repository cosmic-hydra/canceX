# Pipelines Module

Main workflow implementation for processing tumor genomic data.

## Pipeline Overview

The cancer genomics pipeline processes tumor data through the following stages:

1. **Variant Calling** - Detect somatic mutations from sequencing data
2. **Mutation Annotation** - Annotate variants with functional information
3. **Driver Identification** - Identify cancer-driving mutations
4. **Neoantigen Prediction** - Predict immune-recognizable peptides
5. **Target Identification** - Rank potential therapeutic targets

## Usage

### Run Complete Pipeline

```python
from pipelines import CancerGenomicsPipeline

pipeline = CancerGenomicsPipeline(output_dir="../data/processed")

results = pipeline.run_full_pipeline(
    tumor_data="../data/raw/tumor.bam",
    normal_data="../data/raw/normal.bam",
    hla_alleles=['HLA-A*02:01', 'HLA-B*07:02'],
    patient_id="patient_001"
)
```

### Run Individual Steps

```python
from pipelines import VariantCaller, MutationAnnotator, NeoantigenPredictor

# Call variants
caller = VariantCaller()
vcf = caller.call_variants("tumor.bam", "normal.bam")

# Annotate mutations
annotator = MutationAnnotator()
annotated = annotator.annotate_mutations(mutations_df)

# Predict neoantigens
predictor = NeoantigenPredictor()
predictor.set_hla_type(['HLA-A*02:01'])
neoantigens = predictor.predict_mhc_binding(peptides)
```

## Pipeline Components

- `variant_calling.py` - Variant calling and annotation
- `neoantigen_prediction.py` - Neoantigen and target prediction
- `main_pipeline.py` - Complete workflow orchestration

## Output

Results are saved in the specified output directory:
- `{patient_id}_mutations.vcf` - Called variants
- `{patient_id}_driver_mutations.csv` - Driver mutations
- `{patient_id}_neoantigens.csv` - Predicted neoantigens
- `{patient_id}_therapeutic_targets.csv` - Ranked targets
- `{patient_id}_summary.json` - Pipeline summary
