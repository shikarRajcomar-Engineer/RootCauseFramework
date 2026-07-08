"""
====================================================================
Root Cause Attribution Framework
====================================================================

File:
    experiment_config.py

Description:
    Central experiment configuration for the Root Cause Attribution
    Framework.

This module defines WHAT experiment should be performed.

It intentionally DOES NOT contain

    • Dataset configuration
    • Model architecture
    • Bayesian implementation
    • Signal implementation

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

# ============================================================
# FRAMEWORK CONSTANTS
# ============================================================

DEFAULT_EXPERIMENT_NAME = "Root Cause Attribution Experiment"
DEFAULT_AUTHOR = "Rajcomar"
DEFAULT_VERSION = "1.0"
DEFAULT_RANDOM_SEED = 42
DEFAULT_CONFIDENCE_LEVEL = 0.95
DEFAULT_BOOTSTRAP_ITERATIONS = 1000
DEFAULT_TOP_K = 1

# ============================================================
# ENUMS
# ============================================================


class WindowType(Enum):
    """
    Determines how the anomalous evidence window is selected.
    """

    PERCENTAGE = "Percentage"
    FIXED_SAMPLES = "Fixed Samples"


class SummaryStatistic(Enum):
    """
    Statistic used to summarise the attribution scores.
    """

    MEAN = "Mean"
    MEDIAN = "Median"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    STANDARD_DEVIATION = "Standard Deviation"
    VARIANCE = "Variance"
    RANGE = "Range"
    IQR = "Interquartile Range"
    PERCENTILE_95 = "95th Percentile"


class RankingMethod(Enum):
    """
    Ranking strategy.
    """

    DESCENDING = "Descending"
    ASCENDING = "Ascending"


class ExperimentStatus(Enum):
    """
    Experiment status.
    """

    DEVELOPMENT = "Development"
    TESTING = "Testing"
    PRODUCTION = "Production"


# ============================================================
# EXPERIMENT INFORMATION
# ============================================================


@dataclass(slots=True)
class ExperimentInfo:
    """
    General experiment information.
    """

    name: str = DEFAULT_EXPERIMENT_NAME
    description: str = ("Bayesian Root Cause Attribution Experiment")
    version: str = DEFAULT_VERSION
    author: str = DEFAULT_AUTHOR
    experiment_id: str = "EXP001"

    created: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    status: ExperimentStatus = (
        ExperimentStatus.DEVELOPMENT
    )



# ============================================================
# FAULT CONFIGURATION
# ============================================================


@dataclass(slots=True)
class FaultConfig:
    """
    Configuration of the faults included
    in an experiment.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.faults.enabled_faults =
    # [1,2,3,4,5]
    #
    # experiment.faults.enabled_faults =
    # ["Cooling Failure"]
    #
    # --------------------------------------------------------

    enabled_faults: list = field(default_factory=list)

    # --------------------------------------------------------
    # Example
    #
    # experiment.faults.run_all_faults = True
    #
    # --------------------------------------------------------

    run_all_faults: bool = False

    # --------------------------------------------------------
    # Example
    #
    # Repeat each fault N times.
    #
    # --------------------------------------------------------

    repetitions: int = 1


# ============================================================
# WINDOW CONFIGURATION
# ============================================================


@dataclass(slots=True)
class WindowConfig:
    """
    Configuration of the anomalous evidence window.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.window.window_type =
    # WindowType.PERCENTAGE
    #
    # --------------------------------------------------------

    window_type: WindowType = (
        WindowType.PERCENTAGE
    )

    # --------------------------------------------------------
    # Example
    #
    # experiment.window.window_size = 0.20
    #
    # Uses 20% of the detected anomaly.
    #
    # --------------------------------------------------------

    window_size: float = 0.20

    # --------------------------------------------------------
    # Example
    #
    # experiment.window.fixed_samples = 100
    #
    # Used only for FIXED_SAMPLES.
    #
    # --------------------------------------------------------

    fixed_samples: int = 100


# ============================================================
# STATISTICS CONFIGURATION
# ============================================================


@dataclass(slots=True)
class StatisticsConfig:
    """
    Controls how attribution scores
    are summarised.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.statistics.summary_method =
    # SummaryStatistic.MEAN
    #
    # --------------------------------------------------------

    summary_method: SummaryStatistic = (
        SummaryStatistic.MEAN
    )

    # --------------------------------------------------------
    # Example
    #
    # experiment.statistics.normalize_scores = True
    #
    # --------------------------------------------------------

    normalize_scores: bool = False

    # --------------------------------------------------------
    # Example
    #
    # experiment.statistics.rank_method =
    # RankingMethod.DESCENDING
    #
    # --------------------------------------------------------

    rank_method: RankingMethod = (
        RankingMethod.DESCENDING
    )

# ============================================================
# BOOTSTRAP CONFIGURATION
# ============================================================


@dataclass(slots=True)
class BootstrapConfig:
    """
    Controls bootstrap resampling used for
    estimating confidence intervals and
    statistical robustness.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.bootstrap.enabled = True
    #
    # --------------------------------------------------------

    enabled: bool = False

    # --------------------------------------------------------
    # Example
    #
    # experiment.bootstrap.iterations = 1000
    #
    # --------------------------------------------------------

    iterations: int = DEFAULT_BOOTSTRAP_ITERATIONS

    # --------------------------------------------------------
    # Example
    #
    # experiment.bootstrap.confidence_level = 0.95
    #
    # --------------------------------------------------------

    confidence_level: float = DEFAULT_CONFIDENCE_LEVEL

    # --------------------------------------------------------
    # Example
    #
    # experiment.bootstrap.random_seed = 42
    #
    # --------------------------------------------------------

    random_seed: int = DEFAULT_RANDOM_SEED


# ============================================================
# EVALUATION CONFIGURATION
# ============================================================


@dataclass(slots=True)
class EvaluationConfig:
    """
    Controls how attribution performance
    is evaluated.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.top_k = 1
    #
    # --------------------------------------------------------

    top_k: int = DEFAULT_TOP_K

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.compute_accuracy = True
    #
    # --------------------------------------------------------

    compute_accuracy: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.compute_precision = True
    #
    # --------------------------------------------------------

    compute_precision: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.compute_recall = True
    #
    # --------------------------------------------------------

    compute_recall: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.compute_f1 = True
    #
    # --------------------------------------------------------

    compute_f1: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.compute_balanced_accuracy = True
    #
    # --------------------------------------------------------

    compute_balanced_accuracy: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.compute_specificity = True
    #
    # --------------------------------------------------------

    compute_specificity: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.evaluation.save_confusion_matrix = True
    #
    # --------------------------------------------------------

    save_confusion_matrix: bool = True

# ============================================================
# OUTPUT CONFIGURATION
# ============================================================


@dataclass(slots=True)
class OutputConfig:
    """
    Controls which experiment outputs
    are generated.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.output.save_excel = True
    #
    # --------------------------------------------------------

    save_excel: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.output.save_figures = True
    #
    # --------------------------------------------------------

    save_figures: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.output.save_metadata = True
    #
    # --------------------------------------------------------

    save_metadata: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.output.save_models = False
    #
    # --------------------------------------------------------

    save_models: bool = False

    # --------------------------------------------------------
    # Example
    #
    # experiment.output.overwrite_existing = False
    #
    # --------------------------------------------------------

    overwrite_existing: bool = False

    # --------------------------------------------------------
    # Example
    #
    # experiment.output.experiment_folder = "AUTO"
    #
    # AUTO creates a timestamped folder.
    #
    # --------------------------------------------------------

    experiment_folder: str = "AUTO"

# ============================================================
# RUNTIME CONFIGURATION
# ============================================================


@dataclass(slots=True)
class RuntimeConfig:
    """
    Controls execution behaviour.
    """

    # --------------------------------------------------------
    # Example
    #
    # experiment.runtime.parallel_processing = True
    #
    # --------------------------------------------------------

    parallel_processing: bool = False

    # --------------------------------------------------------
    # Example
    #
    # experiment.runtime.number_of_workers = 8
    #
    # --------------------------------------------------------

    number_of_workers: int = 1

    # --------------------------------------------------------
    # Example
    #
    # experiment.runtime.verbose = True
    #
    # --------------------------------------------------------

    verbose: bool = True

    # --------------------------------------------------------
    # Example
    #
    # experiment.runtime.save_intermediate_results = False
    #
    # --------------------------------------------------------

    save_intermediate_results: bool = False

    # --------------------------------------------------------
    # Example
    #
    # experiment.runtime.stop_on_error = True
    #
    # --------------------------------------------------------

    stop_on_error: bool = True

# ============================================================
# MASTER EXPERIMENT CONFIGURATION
# ============================================================


@dataclass(slots=True)
class ExperimentConfig:
    """
    Master experiment configuration.

    Every experiment within the framework
    receives a single ExperimentConfig object.

    Example

    experiment.info.name

    experiment.faults.enabled_faults

    experiment.window.window_size

    experiment.statistics.summary_method

    experiment.bootstrap.iterations

    experiment.evaluation.top_k

    experiment.output.save_excel

    experiment.runtime.parallel_processing
    """

    info: ExperimentInfo = field(
        default_factory=ExperimentInfo
    )

    faults: FaultConfig = field(
        default_factory=FaultConfig
    )

    window: WindowConfig = field(
        default_factory=WindowConfig
    )

    statistics: StatisticsConfig = field(
        default_factory=StatisticsConfig
    )

    bootstrap: BootstrapConfig = field(
        default_factory=BootstrapConfig
    )

    evaluation: EvaluationConfig = field(
        default_factory=EvaluationConfig
    )

    output: OutputConfig = field(
        default_factory=OutputConfig
    )

    runtime: RuntimeConfig = field(
        default_factory=RuntimeConfig
    )