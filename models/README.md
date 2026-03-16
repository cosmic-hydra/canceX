# Models Module

Machine learning models for cancer genomics analysis and prediction.

## Overview

This module contains ML models for:

1. **Driver Mutation Classification** - Identify cancer-driving mutations
2. **Treatment Response Prediction** - Predict drug sensitivity/resistance
3. **Survival Prediction** - Estimate patient survival probabilities
4. **Recurrence Risk** - Assess cancer recurrence risk

## Models

### Driver Mutation Classifier

Classifies mutations as drivers (cancer-causing) or passengers (neutral).

```python
from models import DriverMutationClassifier

classifier = DriverMutationClassifier()
predictions = classifier.predict(mutations_df)

# Get driver mutations
drivers = predictions[predictions['is_driver'] == True]
```

### Treatment Response Predictor

Predicts patient response to specific therapies based on genomic features.

```python
from models import TreatmentResponsePredictor

predictor = TreatmentResponsePredictor()
signature = predictor.extract_genomic_signature(mutations_df)

# Predict drug response
response = predictor.predict_drug_response(signature, 'gefitinib')

# Predict immunotherapy response
immuno = predictor.predict_immunotherapy_response(signature)
```

### Survival Predictor

Estimates survival probability at different time points.

```python
from models import SurvivalPredictor

predictor = SurvivalPredictor()
features = predictor.prepare_features(genomic_data, clinical_data)
survival = predictor.predict_survival(features, time_points=[12, 24, 60])
```

### Recurrence Predictor

Assesses risk of cancer recurrence after treatment.

```python
from models import RecurrencePredictor

predictor = RecurrencePredictor()
risk = predictor.assess_recurrence_risk(genomic_data)
print(f"Risk category: {risk['risk_category']}")
print(f"Risk score: {risk['risk_score']:.2f}")
```

## Features Used

Models consider various genomic and clinical features:

- Mutation counts and locations
- Driver mutation status
- Tumor mutational burden (TMB)
- Microsatellite instability (MSI)
- Gene pathway alterations
- Conservation scores
- Variant allele frequency
- Clinical variables (age, stage, grade)

## Model Training

In production, models should be trained on large-scale datasets:
- TCGA clinical outcomes
- Drug sensitivity databases (GDSC, CCLE)
- Immunotherapy response cohorts

The current implementations provide placeholder predictions and should be trained on real data for clinical research use.
