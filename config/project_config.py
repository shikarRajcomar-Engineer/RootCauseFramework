"""
====================================================================
Root Cause Attribution Framework
====================================================================

File:
    project_config.py

Description:
    Central project configuration for the Root Cause Attribution
    Framework.

This module contains ONLY project-level configuration.

It intentionally DOES NOT contain

    • Experiment configuration
    • Dataset configuration
    • Model configuration
    • Bayesian configuration

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
from pathlib import Path
from enum import Enum
from typing import Dict, List
import platform
import sys
import logging

# ============================================================
# FRAMEWORK CONSTANTS
# ============================================================

FRAMEWORK_NAME = "Root Cause Attribution Framework"
FRAMEWORK_VERSION = "3.0.0"
FRAMEWORK_STAGE = "Alpha"
DEFAULT_AUTHOR = "Rajcomar"
DEFAULT_ENCODING = "utf-8"
DEFAULT_RANDOM_SEED = 42

# ============================================================
# ENUMS
# ============================================================

class Device(Enum):
    """Supported execution devices."""

    CPU = "CPU"
    GPU = "GPU"
    AUTO = "AUTO"


class LoggingLevel(Enum):
    """Logging levels."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


# ============================================================
# PROJECT INFORMATION
# ============================================================


@dataclass(slots=True)
class ProjectInfo:
    """
    General framework information.
    """

    name: str = FRAMEWORK_NAME
    version: str = FRAMEWORK_VERSION
    stage: str = FRAMEWORK_STAGE
    author: str = DEFAULT_AUTHOR
    description: str = (
        "A modular research framework for Bayesian "
        "root cause attribution using autoencoders."
    )


# ============================================================
# SYSTEM INFORMATION
# ============================================================


@dataclass(slots=True)
class SystemInfo:
    """
    Information about the current machine.
    """

    python_version: str = sys.version.split()[0]
    operating_system: str = platform.system()
    os_version: str = platform.release()
    machine: str = platform.machine()
    processor: str = platform.processor()


# ============================================================
# DIRECTORY CONFIGURATION
# ============================================================


@dataclass(slots=True)
class DirectoryConfig:
    """
    All framework directories.

    Every other module should obtain directories
    from this object.
    """

    root: Path = Path.cwd()

    config: Path = field(init=False)

    core: Path = field(init=False)

    datasets: Path = field(init=False)

    models: Path = field(init=False)

    signals: Path = field(init=False)

    bayesian: Path = field(init=False)

    experiments: Path = field(init=False)

    evaluation: Path = field(init=False)

    reporting: Path = field(init=False)

    visualization: Path = field(init=False)

    utils: Path = field(init=False)

    tests: Path = field(init=False)

    data: Path = field(init=False)

    raw_data: Path = field(init=False)

    processed_data: Path = field(init=False)

    cache: Path = field(init=False)

    outputs: Path = field(init=False)

    excel: Path = field(init=False)

    figures: Path = field(init=False)

    latex: Path = field(init=False)

    metadata: Path = field(init=False)

    logs: Path = field(init=False)

    def __post_init__(self):

        self.config = self.root / "config"

        self.core = self.root / "core"

        self.datasets = self.root / "datasets"

        self.models = self.root / "models"

        self.signals = self.root / "signals"

        self.bayesian = self.root / "bayesian"

        self.experiments = self.root / "experiments"

        self.evaluation = self.root / "evaluation"

        self.reporting = self.root / "reporting"

        self.visualization = self.root / "visualization"

        self.utils = self.root / "utils"

        self.tests = self.root / "tests"

        self.data = self.root / "data"

        self.raw_data = self.data / "raw"

        self.processed_data = self.data / "processed"

        self.cache = self.data / "cache"

        self.outputs = self.root / "outputs"

        self.excel = self.outputs / "Excel"

        self.figures = self.outputs / "Figures"

        self.latex = self.outputs / "Latex"

        self.metadata = self.outputs / "Metadata"

        self.logs = self.root / "logs"


# ============================================================
# LOGGING CONFIGURATION
# ============================================================


@dataclass(slots=True)
class LoggingConfig:
    """
    Framework logging settings.
    """

    level: LoggingLevel = LoggingLevel.INFO

    console_logging: bool = True

    file_logging: bool = True

    log_filename: str = "framework.log"

    log_format: str = (
        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(message)s"
    )


# ============================================================
# EXECUTION CONFIGURATION
# ============================================================


@dataclass(slots=True)
class ExecutionConfig:
    """
    Execution settings.
    """

    random_seed: int = DEFAULT_RANDOM_SEED

    device: Device = Device.AUTO

    debug_mode: bool = False

    deterministic: bool = True


# ============================================================
# MASTER CONFIGURATION OBJECT
# ============================================================


@dataclass(slots=True)
class ProjectConfig:
    """
    Master configuration object.

    Every module in the framework will receive
    ONE ProjectConfig object.

    Example

    config.project.name

    config.paths.outputs

    config.execution.random_seed
    """

    project: ProjectInfo = field(default_factory=ProjectInfo)

    system: SystemInfo = field(default_factory=SystemInfo)

    paths: DirectoryConfig = field(default_factory=DirectoryConfig)

    logging: LoggingConfig = field(default_factory=LoggingConfig)

    execution: ExecutionConfig = field(default_factory=ExecutionConfig)