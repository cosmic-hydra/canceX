# Protein Analysis Module

Tools for protein structure prediction and structural analysis of cancer mutations.

## Overview

This module provides functionality for:

1. **Structure Prediction** - Predict 3D structures of mutated proteins
2. **Structural Analysis** - Analyze binding pockets, epitopes, and mutation impacts
3. **Interaction Analysis** - Study protein-protein interaction changes

## Components

### Protein Structure Predictor

Predicts 3D structures using AI-based methods (AlphaFold2, ESMFold).

```python
from protein import ProteinStructurePredictor

predictor = ProteinStructurePredictor()

# Get protein sequence
sequence = predictor.get_protein_sequence('EGFR', mutation='L858R')

# Predict structure
structure_file = predictor.predict_structure(sequence, 'EGFR_L858R')

# Compare with wild-type
comparison = predictor.compare_structures(wt_pdb, mutant_pdb)
```

### Structural Analyzer

Analyzes protein structures for functional features.

```python
from protein import StructuralAnalyzer

analyzer = StructuralAnalyzer()

# Find binding pockets
pockets = analyzer.identify_binding_pockets('protein.pdb')

# Analyze mutation impact
impact = analyzer.analyze_mutation_impact(position=858, structure_file='protein.pdb')

# Predict epitopes for immunotherapy
epitopes = analyzer.find_epitopes('protein.pdb')
```

### Protein-Protein Interaction Analyzer

Studies how mutations affect protein interactions.

```python
from protein import ProteinProteinInteractionAnalyzer

ppi_analyzer = ProteinProteinInteractionAnalyzer()

# Predict interaction changes
affected = ppi_analyzer.predict_interaction_changes(
    gene='EGFR',
    mutation='L858R',
    structure='egfr_mutant.pdb'
)
```

## Methods Used

### Structure Prediction
- **AlphaFold2**: State-of-the-art structure prediction
- **ESMFold**: Fast protein folding from ESM models
- **RoseTTAFold**: Alternative deep learning method

### Binding Site Detection
- **Fpocket**: Geometry-based pocket detection
- **SiteMap**: Druggability assessment
- **DoGSiteScorer**: Binding site prediction

### Epitope Prediction
- **BepiPred**: B-cell epitope prediction
- **NetMHC**: T-cell epitope prediction
- **ElliPro**: Conformational epitope detection

## Use Cases

1. **Drug Target Validation**: Identify druggable pockets in mutant proteins
2. **Immunotherapy Design**: Find neoepitopes on mutated protein surfaces
3. **Mechanism Studies**: Understand how mutations alter protein function
4. **Interaction Networks**: Map disrupted signaling pathways

## Output Formats

- PDB files for 3D structures
- CSV files for epitope predictions
- JSON for structural comparison metrics
