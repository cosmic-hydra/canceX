"""
Load and standardize cancer genomics datasets.
"""

import pandas as pd
from pathlib import Path
from typing import Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatasetLoader:
    """Load and standardize cancer genomics datasets."""

    def __init__(self, data_dir: str = "../data/reference"):
        self.data_dir = Path(data_dir)

    def load_mutations(self, file_path: str) -> pd.DataFrame:
        """
        Load mutation data from various formats.

        Args:
            file_path: Path to mutation file (CSV, VCF, or TSV)

        Returns:
            Standardized DataFrame with mutation information
        """
        file_path = Path(file_path)

        if file_path.suffix == '.vcf':
            return self._load_vcf(file_path)
        elif file_path.suffix in ['.csv', '.tsv']:
            return pd.read_csv(file_path, sep=',' if file_path.suffix == '.csv' else '\t')
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")

    def _load_vcf(self, vcf_path: Path) -> pd.DataFrame:
        """Load VCF file and convert to DataFrame."""
        mutations = []

        with open(vcf_path, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue

                parts = line.strip().split('\t')
                if len(parts) >= 5:
                    mutations.append({
                        'chromosome': parts[0],
                        'position': int(parts[1]),
                        'ref': parts[3],
                        'alt': parts[4],
                        'quality': parts[5] if len(parts) > 5 else None
                    })

        return pd.DataFrame(mutations)

    def standardize_mutation_format(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize mutation DataFrame to common format.

        Expected columns: chromosome, position, ref, alt, gene (optional)
        """
        required_cols = ['chromosome', 'position', 'ref', 'alt']

        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        # Add gene column if missing
        if 'gene' not in df.columns:
            df['gene'] = None

        return df[['chromosome', 'position', 'ref', 'alt', 'gene']]

    def load_clinical_data(self, file_path: str) -> pd.DataFrame:
        """
        Load clinical/phenotype data.

        Args:
            file_path: Path to clinical data file

        Returns:
            DataFrame with clinical information
        """
        return pd.read_csv(file_path)

    def merge_datasets(self, mutations_df: pd.DataFrame,
                      clinical_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        Merge mutation and clinical data.

        Args:
            mutations_df: Mutation data
            clinical_df: Clinical data (optional)

        Returns:
            Merged DataFrame
        """
        if clinical_df is None:
            return mutations_df

        # Merge on sample_id if available
        if 'sample_id' in mutations_df.columns and 'sample_id' in clinical_df.columns:
            return mutations_df.merge(clinical_df, on='sample_id', how='left')

        return mutations_df


def main():
    """Example usage of dataset loader."""
    loader = DatasetLoader()

    logger.info("Dataset loader initialized")
    logger.info("Use loader.load_mutations(file_path) to load mutation data")
    logger.info("Use loader.load_clinical_data(file_path) to load clinical data")


if __name__ == "__main__":
    main()
