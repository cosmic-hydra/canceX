"""Protein analysis module."""

from .structure_prediction import (
    ProteinStructurePredictor,
    StructuralAnalyzer,
    ProteinProteinInteractionAnalyzer
)

__all__ = [
    'ProteinStructurePredictor',
    'StructuralAnalyzer',
    'ProteinProteinInteractionAnalyzer'
]
