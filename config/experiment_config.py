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