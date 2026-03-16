# Evaluation Module

Test pipeline accuracy and model performance using comprehensive metrics.

## Overview

This module provides evaluation tools for:

1. **Mutation Classification** - Accuracy, precision, recall, AUC-ROC
2. **Neoantigen Prediction** - Binding prediction validation
3. **Docking Quality** - Binding affinity and enrichment metrics
4. **Pipeline Performance** - End-to-end evaluation

## Components

### Mutation Prediction Evaluator

Evaluate driver mutation classification performance.

```python
from evaluation import MutationPredictionEvaluator

evaluator = MutationPredictionEvaluator()

# Classification metrics
metrics = evaluator.calculate_classification_metrics(
    y_true=[1, 1, 0, 0, 1],
    y_pred=[1, 1, 0, 1, 1],
    y_scores=[0.9, 0.8, 0.3, 0.6, 0.85]
)

print(f"Accuracy: {metrics['accuracy']:.3f}")
print(f"Precision: {metrics['precision']:.3f}")
print(f"Recall: {metrics['recall']:.3f}")
print(f"F1-Score: {metrics['f1_score']:.3f}")
print(f"AUC-ROC: {metrics['auc_roc']:.3f}")

# Validate against known drivers
known_drivers = ['TP53', 'KRAS', 'EGFR', 'BRAF']
driver_eval = evaluator.evaluate_driver_prediction(predicted_df, known_drivers)
```

### Neoantigen Evaluator

Evaluate MHC binding predictions.

```python
from evaluation import NeoantigenEvaluator

evaluator = NeoantigenEvaluator()

# Evaluate predictions
metrics = evaluator.evaluate_binding_predictions(predictions_df)

print(f"Total predictions: {metrics['total_predictions']}")
print(f"Strong binders: {metrics['strong_binders']}")
print(f"Weak binders: {metrics['weak_binders']}")

# Compare with experimental data
metrics = evaluator.evaluate_binding_predictions(
    predictions_df,
    experimental_data=validation_df
)
print(f"Correlation: {metrics['correlation']:.2f}")
```

### Docking Evaluator

Evaluate molecular docking results.

```python
from evaluation import DockingEvaluator

evaluator = DockingEvaluator()

# Quality metrics
metrics = evaluator.evaluate_docking_quality(docking_results_df)

print(f"Best affinity: {metrics['best_affinity']:.2f} kcal/mol")
print(f"Mean affinity: {metrics['mean_affinity']:.2f} kcal/mol")
print(f"High-affinity compounds: {metrics['high_affinity_compounds']}")

# Enrichment factor
enrichment = evaluator.calculate_enrichment_factor(
    docking_results_df,
    known_actives=['compound1', 'compound2'],
    top_n=100
)
print(f"Enrichment factor: {enrichment:.2f}")
```

### Pipeline Evaluator

Evaluate complete pipeline performance.

```python
from evaluation import PipelineEvaluator

evaluator = PipelineEvaluator()

# Evaluate all pipeline components
evaluation = evaluator.evaluate_pipeline(pipeline_results)

print("Driver Prediction:")
print(f"  Precision: {evaluation['metrics']['driver_prediction']['precision']:.2f}")

print("Neoantigen Prediction:")
print(f"  Strong binders: {evaluation['metrics']['neoantigen_prediction']['strong_binders']}")

print("Therapeutic Targets:")
print(f"  Total targets: {evaluation['metrics']['therapeutic_targets']['total_targets']}")
```

## Metrics Explained

### Classification Metrics

- **Accuracy**: Overall correct predictions
- **Precision**: Positive predictive value (TP / (TP + FP))
- **Recall**: Sensitivity (TP / (TP + FN))
- **F1-Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Area under receiver operating characteristic curve

### Binding Affinity Metrics

- **Strong Binders**: IC50 ≤ 50 nM or affinity ≤ -9 kcal/mol
- **Weak Binders**: 50 nM < IC50 ≤ 500 nM
- **Correlation**: Agreement with experimental data

### Docking Metrics

- **Binding Affinity**: Predicted protein-ligand binding energy (kcal/mol)
- **Enrichment Factor**: Ratio of actives in top N vs random selection
- **Success Rate**: Percentage of near-native poses

## Validation Datasets

For rigorous evaluation, use:

- **COSMIC Cancer Gene Census**: Validated driver genes
- **IEDB**: Experimental MHC binding data
- **DUD-E**: Directory of Useful Decoys Enhanced
- **ChEMBL**: Bioactivity database

## Usage Example

```python
from pipelines import CancerGenomicsPipeline
from evaluation import PipelineEvaluator

# Run pipeline
pipeline = CancerGenomicsPipeline()
results = pipeline.run_full_pipeline(
    tumor_data="tumor.bam",
    hla_alleles=['HLA-A*02:01']
)

# Evaluate results
evaluator = PipelineEvaluator()
evaluation = evaluator.evaluate_pipeline(results)

# Save evaluation report
import json
with open('evaluation_report.json', 'w') as f:
    json.dump(evaluation, f, indent=2)
```

## Reproducibility

To ensure reproducible evaluation:

1. Use fixed random seeds
2. Document software versions
3. Save evaluation parameters
4. Version control test datasets
5. Report confidence intervals
