"""
Main cancer genomics analysis pipeline.

Orchestrates the complete workflow from raw data to therapeutic predictions.
"""

import logging
from pathlib import Path
from typing import Optional, Dict
import pandas as pd
import json

from .variant_calling import VariantCaller, MutationAnnotator
from .neoantigen_prediction import NeoantigenPredictor, TherapeuticTargetFinder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CancerGenomicsPipeline:
    """Main pipeline for cancer genomics analysis."""

    def __init__(self, output_dir: str = "../data/processed"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize pipeline components
        self.variant_caller = VariantCaller()
        self.annotator = MutationAnnotator()
        self.neoantigen_predictor = NeoantigenPredictor()
        self.target_finder = TherapeuticTargetFinder()

        # Results storage
        self.results = {}

    def run_full_pipeline(self,
                         tumor_data: str,
                         normal_data: Optional[str] = None,
                         hla_alleles: Optional[list] = None,
                         patient_id: str = "patient_001") -> Dict:
        """
        Run complete analysis pipeline.

        Args:
            tumor_data: Path to tumor sequencing data (BAM/FASTQ/VCF)
            normal_data: Path to normal sequencing data (optional)
            hla_alleles: Patient HLA type for neoantigen prediction
            patient_id: Patient identifier

        Returns:
            Dictionary with all analysis results
        """
        logger.info("="*80)
        logger.info("Starting Cancer Genomics Pipeline for patient: %s", patient_id)
        logger.info("="*80)

        self.results['patient_id'] = patient_id

        # Step 1: Variant Calling
        logger.info("\n[Step 1/5] Variant Calling")
        logger.info("-" * 40)
        mutations_vcf = self._run_variant_calling(tumor_data, normal_data, patient_id)
        self.results['mutations_vcf'] = mutations_vcf

        # Step 2: Mutation Annotation
        logger.info("\n[Step 2/5] Mutation Annotation")
        logger.info("-" * 40)
        annotated_mutations = self._annotate_mutations(mutations_vcf)
        self.results['annotated_mutations_count'] = len(annotated_mutations)

        # Step 3: Driver Mutation Identification
        logger.info("\n[Step 3/5] Driver Mutation Identification")
        logger.info("-" * 40)
        driver_mutations = self._identify_drivers(annotated_mutations)
        self.results['driver_mutations'] = driver_mutations
        self._save_results(driver_mutations, f"{patient_id}_driver_mutations.csv")

        # Step 4: Neoantigen Prediction
        logger.info("\n[Step 4/5] Neoantigen Prediction")
        logger.info("-" * 40)
        if hla_alleles:
            neoantigens = self._predict_neoantigens(driver_mutations, hla_alleles)
            self.results['neoantigens'] = neoantigens
            self._save_results(neoantigens, f"{patient_id}_neoantigens.csv")
        else:
            logger.warning("No HLA alleles provided, skipping neoantigen prediction")
            neoantigens = pd.DataFrame()

        # Step 5: Therapeutic Target Identification
        logger.info("\n[Step 5/5] Therapeutic Target Identification")
        logger.info("-" * 40)
        targets = self._identify_targets(driver_mutations, neoantigens)
        self.results['therapeutic_targets'] = targets
        self._save_results(targets, f"{patient_id}_therapeutic_targets.csv")

        # Save summary
        self._save_summary(patient_id)

        logger.info("\n" + "="*80)
        logger.info("Pipeline Complete!")
        logger.info("="*80)
        logger.info("Results saved to: %s", self.output_dir)

        return self.results

    def _run_variant_calling(self, tumor_data: str,
                            normal_data: Optional[str],
                            patient_id: str) -> str:
        """Step 1: Call variants from sequencing data."""
        output_vcf = self.output_dir / f"{patient_id}_mutations.vcf"

        vcf_path = self.variant_caller.call_variants(
            tumor_bam=tumor_data,
            normal_bam=normal_data,
            output_vcf=str(output_vcf)
        )

        return vcf_path

    def _annotate_mutations(self, vcf_path: str) -> pd.DataFrame:
        """Step 2: Annotate mutations with functional information."""
        # In production, parse VCF
        # For now, create sample data
        mutations_df = pd.DataFrame({
            'chromosome': ['chr17', 'chr7'],
            'position': [7577548, 55249071],
            'ref': ['C', 'C'],
            'alt': ['T', 'T'],
            'gene': ['TP53', 'EGFR']
        })

        annotated = self.annotator.annotate_mutations(mutations_df)
        return annotated

    def _identify_drivers(self, mutations_df: pd.DataFrame) -> pd.DataFrame:
        """Step 3: Identify driver mutations."""
        drivers = self.annotator.prioritize_driver_mutations(mutations_df)
        return drivers

    def _predict_neoantigens(self, mutations_df: pd.DataFrame,
                            hla_alleles: list) -> pd.DataFrame:
        """Step 4: Predict neoantigens from mutations."""
        self.neoantigen_predictor.set_hla_type(hla_alleles)

        peptides = self.neoantigen_predictor.extract_mutant_peptides(mutations_df)
        predictions = self.neoantigen_predictor.predict_mhc_binding(peptides)
        neoantigens = self.neoantigen_predictor.rank_neoantigens(predictions)

        return neoantigens

    def _identify_targets(self, driver_mutations: pd.DataFrame,
                         neoantigens: pd.DataFrame) -> pd.DataFrame:
        """Step 5: Identify therapeutic targets."""
        targets = self.target_finder.identify_targets(
            driver_mutations,
            neoantigens
        )
        return targets

    def _save_results(self, df: pd.DataFrame, filename: str):
        """Save DataFrame to CSV."""
        if len(df) > 0:
            output_path = self.output_dir / filename
            df.to_csv(output_path, index=False)
            logger.info("Saved: %s (%d rows)", filename, len(df))

    def _save_summary(self, patient_id: str):
        """Save pipeline summary."""
        summary = {
            'patient_id': patient_id,
            'total_mutations': self.results.get('annotated_mutations_count', 0),
            'driver_mutations': len(self.results.get('driver_mutations', [])),
            'neoantigens': len(self.results.get('neoantigens', [])),
            'therapeutic_targets': len(self.results.get('therapeutic_targets', []))
        }

        output_path = self.output_dir / f"{patient_id}_summary.json"
        with open(output_path, 'w') as f:
            json.dump(summary, f, indent=2)

        logger.info("\nPipeline Summary:")
        for key, value in summary.items():
            logger.info("  %s: %s", key, value)


def main():
    """Run example pipeline."""
    pipeline = CancerGenomicsPipeline(output_dir="../data/processed")

    # Example run
    results = pipeline.run_full_pipeline(
        tumor_data="../data/raw/tumor.bam",
        normal_data="../data/raw/normal.bam",
        hla_alleles=['HLA-A*02:01', 'HLA-B*07:02', 'HLA-C*07:01'],
        patient_id="example_patient"
    )

    print("\nPipeline completed successfully!")
    print(f"Found {len(results.get('driver_mutations', []))} driver mutations")
    print(f"Predicted {len(results.get('neoantigens', []))} neoantigens")
    print(f"Identified {len(results.get('therapeutic_targets', []))} therapeutic targets")


if __name__ == "__main__":
    main()
