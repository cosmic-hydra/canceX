# canceX - AI-Powered Cancer Genomics Research Pipeline

An automated research pipeline that uses artificial intelligence and bioinformatics to analyze tumor genomic data, identify cancer-driving mutations, predict protein structures, discover immune targets, and simulate potential therapies.

## Overview

This system automates the process from raw genomic input to ranked therapeutic hypotheses for research purposes. It combines:

- **Genomic Analysis**: Mutation calling, annotation, and driver identification
- **Machine Learning**: Prediction of treatment response and clinical outcomes
- **Protein Modeling**: Structure prediction and functional analysis
- **Drug Discovery**: Molecular generation, docking, and ADMET prediction
- **Immunotherapy**: Neoantigen prediction and immune target discovery

## Features

- 🧬 Comprehensive mutation analysis and driver identification
- 🤖 ML models for treatment response prediction
- 🧪 Protein structure prediction using AlphaFold-like methods
- 💊 AI-driven drug candidate generation and evaluation
- 🎯 Neoantigen prediction for immunotherapy
- 📊 Interactive Jupyter notebooks for exploration
- ✅ Comprehensive evaluation metrics

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA for GPU acceleration

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cosmic-hydra/canceX.git
   cd canceX
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python -c "import pipelines; print('Installation successful!')"
   ```

## Quick Start

### Run Complete Pipeline

```python
from pipelines import CancerGenomicsPipeline

# Initialize pipeline
pipeline = CancerGenomicsPipeline(output_dir="data/processed")

# Run analysis
results = pipeline.run_full_pipeline(
    tumor_data="data/raw/tumor.bam",
    normal_data="data/raw/normal.bam",
    hla_alleles=['HLA-A*02:01', 'HLA-B*07:02'],
    patient_id="patient_001"
)

# View results
print(f"Found {len(results['driver_mutations'])} driver mutations")
print(f"Predicted {len(results['neoantigens'])} neoantigens")
print(f"Identified {len(results['therapeutic_targets'])} therapeutic targets")
```

### Use Interactive Notebooks

```bash
cd notebooks
jupyter notebook
```

Open `01_quickstart.ipynb` for a guided walkthrough.

## Project Structure

```
canceX/
├── data/                    # Data storage
│   ├── raw/                 # Raw genomic data (FASTQ, BAM, VCF)
│   ├── processed/           # Processed results
│   └── reference/           # Reference genomes and databases
├── datasets/                # Dataset download and loading scripts
│   ├── download_datasets.py # Download TCGA, COSMIC, ICGC data
│   └── loader.py            # Load and standardize datasets
├── pipelines/               # Main analysis workflows
│   ├── variant_calling.py   # Mutation calling and annotation
│   ├── neoantigen_prediction.py # Neoantigen and target prediction
│   └── main_pipeline.py     # Complete workflow orchestration
├── models/                  # Machine learning models
│   ├── mutation_classifier.py   # Driver mutation classification
│   └── clinical_outcome.py      # Survival and recurrence prediction
├── protein/                 # Protein structure analysis
│   └── structure_prediction.py  # Structure prediction and analysis
├── drug_discovery/          # Drug candidate discovery
│   └── molecule_generation.py   # Generation, docking, ADMET
├── evaluation/              # Performance metrics
│   └── metrics.py           # Evaluation tools
├── notebooks/               # Interactive Jupyter notebooks
│   ├── 01_quickstart.ipynb
│   ├── 02_mutation_analysis.ipynb
│   ├── 03_protein_structures.ipynb
│   └── 04_drug_discovery.ipynb
└── requirements.txt         # Python dependencies
```

## Usage

### 1. Prepare Input Data

Place your tumor genomic data in `data/raw/`:
- Tumor sequencing data (FASTQ/BAM files)
- Normal/healthy reference (optional but recommended)
- Mutation calls (VCF format, optional)

### 2. Run Pipeline Components

#### Variant Calling
```python
from pipelines import VariantCaller, MutationAnnotator

caller = VariantCaller()
vcf_path = caller.call_variants("tumor.bam", "normal.bam")

annotator = MutationAnnotator()
annotated = annotator.annotate_mutations(mutations_df)
drivers = annotator.prioritize_driver_mutations(annotated)
```

#### Neoantigen Prediction
```python
from pipelines import NeoantigenPredictor

predictor = NeoantigenPredictor()
predictor.set_hla_type(['HLA-A*02:01', 'HLA-B*07:02'])

peptides = predictor.extract_mutant_peptides(mutations_df)
neoantigens = predictor.predict_mhc_binding(peptides)
```

#### Protein Structure Analysis
```python
from protein import ProteinStructurePredictor, StructuralAnalyzer

predictor = ProteinStructurePredictor()
structure = predictor.predict_structure(sequence, gene_name)

analyzer = StructuralAnalyzer()
pockets = analyzer.identify_binding_pockets(structure)
epitopes = analyzer.find_epitopes(structure)
```

#### Drug Discovery
```python
from drug_discovery import MoleculeGenerator, MolecularDocking

generator = MoleculeGenerator()
molecules = generator.generate_molecules(target_protein="EGFR", num_molecules=100)

docker = MolecularDocking()
results = docker.dock_molecule(ligand_smiles, protein_pdb)
ranked = docker.rank_compounds(results)
```

#### Treatment Prediction
```python
from models import TreatmentResponsePredictor

predictor = TreatmentResponsePredictor()
signature = predictor.extract_genomic_signature(mutations_df)

response = predictor.predict_drug_response(signature, drug="gefitinib")
immuno_response = predictor.predict_immunotherapy_response(signature)
```

### 3. Evaluate Results

```python
from evaluation import PipelineEvaluator

evaluator = PipelineEvaluator()
evaluation = evaluator.evaluate_pipeline(pipeline_results)

print(f"Accuracy: {evaluation['metrics']['accuracy']:.3f}")
```

## Data Sources

The pipeline can work with data from:

- **TCGA** (The Cancer Genome Atlas): https://portal.gdc.cancer.gov/
- **COSMIC** (Catalogue Of Somatic Mutations In Cancer): https://cancer.sanger.ac.uk/cosmic
- **ICGC** (International Cancer Genome Consortium): https://dcc.icgc.org/

See `datasets/README.md` for download instructions.

## Methods and Tools

### Variant Calling
- Mutect2 (GATK) - Somatic variant calling
- VarScan - Mutation detection
- VEP/SnpEff - Variant annotation

### Machine Learning
- PyTorch/TensorFlow - Deep learning frameworks
- XGBoost - Gradient boosting
- scikit-learn - Classical ML algorithms

### Protein Analysis
- AlphaFold2 - Structure prediction
- ESMFold - Fast folding
- ProDy - Structural analysis

### Drug Discovery
- RDKit - Cheminformatics
- DeepChem - AI for chemistry
- AutoDock Vina - Molecular docking

### Immunology
- NetMHCpan - MHC binding prediction
- BepiPred - Epitope prediction

## Output

Pipeline generates:
- `{patient_id}_mutations.vcf` - Called variants
- `{patient_id}_driver_mutations.csv` - Driver mutations
- `{patient_id}_neoantigens.csv` - Predicted neoantigens
- `{patient_id}_therapeutic_targets.csv` - Ranked targets
- `{patient_id}_summary.json` - Analysis summary

## Performance Metrics

The pipeline tracks:
- **Mutation Classification**: Accuracy, precision, recall, F1-score, AUC-ROC
- **Neoantigen Prediction**: Binding affinity predictions, strong binder counts
- **Drug Docking**: Binding affinity, enrichment factors
- **Overall Pipeline**: End-to-end validation metrics

## Examples

See the `notebooks/` directory for detailed examples:
- Complete pipeline walkthrough
- Mutation pattern analysis
- Protein structure visualization
- Drug discovery workflow

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Citation

If you use this pipeline in your research, please cite:

```
canceX: AI-Powered Cancer Genomics Research Pipeline
https://github.com/cosmic-hydra/canceX
```

## License

See LICENSE file for details.

## Disclaimer

**IMPORTANT - RESEARCH USE ONLY**

This pipeline is designed for **research and educational purposes only**. It is NOT intended for:
- Clinical diagnosis
- Medical decision-making
- Treatment planning
- Patient care

Key limitations:
- Predictions are computational and require experimental validation
- Models may not generalize to all cancer types
- Results should be validated by qualified researchers
- No regulatory approval for clinical use

Always consult qualified medical professionals for health-related decisions. The authors and contributors are not responsible for any misuse of this software.

## Support

- **Documentation**: See README files in each module directory
- **Issues**: https://github.com/cosmic-hydra/canceX/issues
- **Discussions**: https://github.com/cosmic-hydra/canceX/discussions

## Acknowledgments

This project builds upon:
- Public cancer genomics databases (TCGA, COSMIC, ICGC)
- Open-source bioinformatics tools
- AI/ML frameworks and libraries
- The broader cancer research community

---

**Research Use Only - Not for Clinical or Medical Use**
