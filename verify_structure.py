#!/usr/bin/env python3
"""
Verify the canceX pipeline structure and basic functionality.

This test script checks that all modules are properly structured
without requiring external dependencies to be installed.
"""

import os
import sys
from pathlib import Path

def check_structure():
    """Check that all required directories and files exist."""
    base_dir = Path(__file__).parent

    required_structure = {
        'requirements.txt': 'Dependencies file',
        'README.md': 'Main documentation',
        '.gitignore': 'Git ignore rules',
        'data/README.md': 'Data directory documentation',
        'data/raw/.gitkeep': 'Raw data placeholder',
        'data/processed/.gitkeep': 'Processed data placeholder',
        'data/reference/.gitkeep': 'Reference data placeholder',
        'datasets/__init__.py': 'Datasets module',
        'datasets/download_datasets.py': 'Dataset downloader',
        'datasets/loader.py': 'Dataset loader',
        'datasets/README.md': 'Datasets documentation',
        'pipelines/__init__.py': 'Pipelines module',
        'pipelines/variant_calling.py': 'Variant calling pipeline',
        'pipelines/neoantigen_prediction.py': 'Neoantigen prediction',
        'pipelines/main_pipeline.py': 'Main pipeline orchestration',
        'pipelines/README.md': 'Pipelines documentation',
        'models/__init__.py': 'Models module',
        'models/mutation_classifier.py': 'Mutation classifier model',
        'models/clinical_outcome.py': 'Clinical outcome models',
        'models/README.md': 'Models documentation',
        'protein/__init__.py': 'Protein module',
        'protein/structure_prediction.py': 'Protein structure prediction',
        'protein/README.md': 'Protein analysis documentation',
        'drug_discovery/__init__.py': 'Drug discovery module',
        'drug_discovery/molecule_generation.py': 'Molecule generation',
        'drug_discovery/README.md': 'Drug discovery documentation',
        'evaluation/__init__.py': 'Evaluation module',
        'evaluation/metrics.py': 'Evaluation metrics',
        'evaluation/README.md': 'Evaluation documentation',
        'notebooks/01_quickstart.ipynb': 'Quickstart notebook',
        'notebooks/02_mutation_analysis.ipynb': 'Mutation analysis notebook',
        'notebooks/03_protein_structures.ipynb': 'Protein structures notebook',
        'notebooks/04_drug_discovery.ipynb': 'Drug discovery notebook',
        'notebooks/README.md': 'Notebooks documentation',
    }

    print("Checking canceX pipeline structure...\n")

    missing = []
    found = []

    for file_path, description in required_structure.items():
        full_path = base_dir / file_path
        if full_path.exists():
            found.append(f"✓ {file_path} - {description}")
        else:
            missing.append(f"✗ {file_path} - {description}")

    # Print results
    for item in found:
        print(item)

    if missing:
        print("\nMissing files:")
        for item in missing:
            print(item)
        return False

    print(f"\n✓ All {len(found)} required files found!")
    return True

def check_python_files():
    """Check that Python files have basic valid syntax."""
    base_dir = Path(__file__).parent

    python_files = [
        'datasets/__init__.py',
        'datasets/download_datasets.py',
        'datasets/loader.py',
        'pipelines/__init__.py',
        'pipelines/variant_calling.py',
        'pipelines/neoantigen_prediction.py',
        'pipelines/main_pipeline.py',
        'models/__init__.py',
        'models/mutation_classifier.py',
        'models/clinical_outcome.py',
        'protein/__init__.py',
        'protein/structure_prediction.py',
        'drug_discovery/__init__.py',
        'drug_discovery/molecule_generation.py',
        'evaluation/__init__.py',
        'evaluation/metrics.py',
    ]

    print("\nChecking Python file syntax...\n")

    all_valid = True
    for py_file in python_files:
        full_path = base_dir / py_file
        try:
            with open(full_path, 'r') as f:
                compile(f.read(), py_file, 'exec')
            print(f"✓ {py_file} - Valid Python syntax")
        except SyntaxError as e:
            print(f"✗ {py_file} - Syntax error: {e}")
            all_valid = False

    if all_valid:
        print(f"\n✓ All {len(python_files)} Python files have valid syntax!")

    return all_valid

def main():
    """Run all verification checks."""
    print("=" * 80)
    print("canceX Pipeline Verification")
    print("=" * 80)
    print()

    structure_ok = check_structure()
    syntax_ok = check_python_files()

    print("\n" + "=" * 80)
    if structure_ok and syntax_ok:
        print("✓ All checks passed! Pipeline is properly structured.")
        print("=" * 80)
        return 0
    else:
        print("✗ Some checks failed. Please review the output above.")
        print("=" * 80)
        return 1

if __name__ == "__main__":
    sys.exit(main())
