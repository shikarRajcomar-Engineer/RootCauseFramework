"""
====================================================================
Root Cause Attribution Framework
====================================================================

File:
    dataset_config.py

Description:
    Central dataset configuration for the Root Cause Attribution
    Framework.

This module defines HOW a dataset is described.

It intentionally DOES NOT contain

    • Model configuration
    • Experiment configuration
    • Bayesian configuration
    • Signal configuration

Those are handled by their own configuration modules.

Author:
    Rajcomar

Framework Version:
    3.0.0

Python:
    3.10+

====================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path

# ============================================================
# FRAMEWORK CONSTANTS
# ============================================================

DEFAULT_DATASET_NAME = "Unnamed Dataset"
DEFAULT_AUTHOR = "Rajcomar"
DEFAULT_VERSION = "1.0"
DEFAULT_ENCODING = "utf-8"
DEFAULT_RANDOM_SEED = 42


# ============================================================
# ENUMS
# ============================================================

class FileType(Enum):
    """
    Supported dataset formats.
    """

    CSV = "csv"
    EXCEL = "xlsx"
    PARQUET = "parquet"
    PICKLE = "pickle"
    JSON = "json"

class ScalingMethod(Enum):
    """
    Feature scaling methods.
    """
    NONE = "None"
    STANDARD = "StandardScaler"
    MINMAX = "MinMaxScaler"
    ROBUST = "RobustScaler"
    MAXABS = "MaxAbsScaler"

class MissingValueStrategy(Enum):
    """
    Missing value handling.
    """

    NONE = "None"
    DROP = "Drop"
    MEAN = "Mean"
    MEDIAN = "Median"
    MODE = "Mode"
    FORWARD_FILL = "Forward Fill"
    BACKWARD_FILL = "Backward Fill"

# ============================================================
# DATASET INFORMATION
# ============================================================

@dataclass(slots=True)
class DatasetInfo:
    """
    General dataset information.
    """

    name: str = DEFAULT_DATASET_NAME
    description: str = ""
    author: str = DEFAULT_AUTHOR
    version: str = DEFAULT_VERSION
    created: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    dataset_id: str = "DATASET001"

# ============================================================
# FILE CONFIGURATION
# ============================================================


@dataclass(slots=True)
class FileConfig:
    """
    Dataset file configuration.
    --------------------------------------------------------
    Example:

    dataset.file.file_path =Path("datasets/CSTR/normal.csv")

    dataset.file.file_type =FileType.CSV

    dataset.file.encoding = "utf-8"

    dataset.file.has_header = True

    --------------------------------------------------------
    """


    file_path: Path = Path()
    file_type: FileType = FileType.CSV
    encoding: str = DEFAULT_ENCODING
    has_header: bool = True


# ============================================================
# COLUMN CONFIGURATION
# ============================================================


@dataclass(slots=True)
class ColumnConfig:
    """
    Dataset column definitions.
    --------------------------------------------------------
    Example
    
    dataset.columns.feature_columns =["Ci","Ti","T","Qc","Tci","Tc","C"]

    dataset.columns.target_column ="Fault"
    
    dataset.columns.timestamp_column ="Timestamp"

    dataset.columns.ignore_columns =["BatchID"]
    --------------------------------------------------------

    """ 

    feature_columns: list[str] = field(default_factory=list)
    target_column: str = ""
    timestamp_column: str = ""
    ignore_columns: list[str] = field(default_factory=list)


# ============================================================
# DATASET SPLIT CONFIGURATION
# ============================================================


@dataclass(slots=True)
class SplitConfig:
    """
    Dataset train, validation and test split configuration.
    --------------------------------------------------------
    Example

    dataset.split.train_size = 0.70

    dataset.split.validation_size = 0.15

    dataset.split.test_size = 0.15

    dataset.split.shuffle = True

    dataset.split.random_seed = 42

    --------------------------------------------------------

    """

    train_size: float = 0.70
    validation_size: float = 0.15
    test_size: float = 0.15
    shuffle: bool = True
    random_seed: int = DEFAULT_RANDOM_SEED

# ============================================================
# SCALING CONFIGURATION
# ============================================================


@dataclass(slots=True)
class ScalingConfig:
    """
    Feature scaling configuration.
    --------------------------------------------------------
    Example

    dataset.scaling.enabled = True

    dataset.scaling.method =ScalingMethod.MINMAX

    dataset.scaling.feature_range = (0, 1) Used by MinMaxScaler.

    dataset.scaling.fit_on_training_only = True Prevents data leakage.

    --------------------------------------------------------
    """

    enabled: bool = True
    method: ScalingMethod = ScalingMethod.MINMAX
    feature_range: tuple = (0.0, 1.0)
    fit_on_training_only: bool = True


    # ============================================================
# MISSING VALUE CONFIGURATION
# ============================================================


@dataclass(slots=True)
class MissingValueConfig:
    """
    Missing value handling.
    --------------------------------------------------------
    Example

    dataset.missing.enabled = False
    
    dataset.missing.strategy =MissingValueStrategy.MEAN

    dataset.missing.maximum_missing_percentage = 0.20

    --------------------------------------------------------

    """


    enabled: bool = False
    strategy: MissingValueStrategy = (MissingValueStrategy.NONE)
    maximum_missing_percentage: float = 0.20


# ============================================================
# LABEL CONFIGURATION
# ============================================================


@dataclass(slots=True)
class LabelConfig:
    """
    Target label configuration.
    --------------------------------------------------------
    Example

    dataset.labels.normal_label = 0

    dataset.labels.anomaly_label = 1

    dataset.labels.multiclass = False

    dataset.labels.label_mapping ={0:"Normal",1:"Fault"}

    --------------------------------------------------------
    """

    normal_label: int | str = 0
    anomaly_label: int | str = 1
    multiclass: bool = False
    label_mapping: dict = field(default_factory=dict)


    # ============================================================
# DATA VALIDATION CONFIGURATION
# ============================================================


@dataclass(slots=True)
class ValidationConfig:
    """
    Dataset validation rules.
    --------------------------------------------------------
    Example

    dataset.validation.validate_duplicates = True

    dataset.validation.validate_missing = True

    dataset.validation.validate_feature_names = True

    dataset.validation.validate_numeric = True

    --------------------------------------------------------
    """

    validate_duplicates: bool = True
    validate_missing: bool = True
    validate_feature_names: bool = True
    validate_numeric: bool = True