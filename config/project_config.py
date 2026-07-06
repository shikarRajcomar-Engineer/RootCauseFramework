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
from typing import Any
import platform
import sys
import logging
from datetime import datetime
from dataclasses import fields
import json
import hashlib
from dataclasses import asdict


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
    framework_id: str = "RCAF"
    author: str = DEFAULT_AUTHOR
    created: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    description: str = (
        "A modular research framework for Bayesian "
        "root cause attribution using autoencoders."
    )


# ============================================================
# SYSTEM INFORMATION
# ============================================================


@dataclass(slots=True)
class EnvironmentInfo:
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
class PathConfig:
    """
    All framework directories.
    Every other module should obtain directories
    from this object.
    """

    root: Path = field(default_factory=lambda: Path(__file__).resolve().parent.parent)

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

    environment: EnvironmentInfo = field(default_factory=EnvironmentInfo)
    
    paths: PathConfig = field(default_factory=PathConfig)

    logging: LoggingConfig = field(default_factory=LoggingConfig)

    execution: ExecutionConfig = field(default_factory=ExecutionConfig)


# ============================================================
# CONFIGURATION UTILITIES
# ============================================================


class ProjectConfigurationError(Exception):
    """Raised when the project configuration is invalid."""
    pass


# ============================================================
# PROJECT CONFIG METHODS
# ============================================================

class ConfigurationManager:
    """
    Utility class for managing the framework configuration.
    """

    def __init__(self, config: ProjectConfig):

        self.config = config

    # --------------------------------------------------------
    def create_directories(self) -> None:
        """
        Create every framework directory.
        """

        for field in fields(self.config.paths):

            value = getattr(self.config.paths, field.name)

            if isinstance(value, Path):

                value.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------------

    def validate(self) -> None:
        """
        Validate the configuration.
        """

        if self.config.execution.random_seed < 0:

            raise ProjectConfigurationError(
                "Random seed must be positive."
            )

        if not self.config.project.name:

            raise ProjectConfigurationError(
                "Project name cannot be empty."
            )

        if not self.config.project.version:

            raise ProjectConfigurationError(
                "Project version cannot be empty."
            )

    # --------------------------------------------------------

    def to_dictionary(self) -> dict:
        """
        Convert configuration to dictionary.
        """

        dictionary = asdict(self.config)

        return self._convert_paths(dictionary)

    # --------------------------------------------------------

    def save_json(self, filename: Path) -> None:
        """
        Save configuration to JSON.
        """

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                self.to_dictionary(),
                file,
                indent=4
            )

    # --------------------------------------------------------

    def configuration_hash(self) -> str:
        """
        Create a unique hash of the configuration.
        """

        data = json.dumps(
            self.to_dictionary(),
            sort_keys=True
        )

        return hashlib.sha256(
            data.encode("utf-8")
        ).hexdigest()

    # --------------------------------------------------------

    @staticmethod
    def _convert_paths(item):

        if isinstance(item, Path):

            return str(item)

        if isinstance(item, dict):

            return {
                key: ConfigurationManager._convert_paths(value)
                for key, value in item.items()
            }

        if isinstance(item, list):

            return [
                ConfigurationManager._convert_paths(value)
                for value in item
            ]

        if isinstance(item, Enum):

            return item.name

        return item

    # --------------------------------------------------------

    def summary(self) -> None:
        """
        Print a summary of the framework configuration.
        """

        print("=" * 70)

        print(self.config.project.name)

        print("=" * 70)

        print(f"Version        : {self.config.project.version}")
        print(f"Author         : {self.config.project.author}")
        print(f"Stage          : {self.config.project.stage}")

        print()

        print("Python         :", self.config.environment.python_version)
        print("Operating Sys  :", self.config.environment.operating_system)
        print("Machine        :", self.config.environment.machine)

        print()

        print("Project Root   :", self.config.paths.root)

        print("Output Folder  :", self.config.paths.outputs)

        print("Logs Folder    :", self.config.paths.logs)

        print()

        print("Device         :", self.config.execution.device.name)

        print("Random Seed    :", self.config.execution.random_seed)

        print("=" * 70)


# ============================================================
# DEFAULT CONFIGURATION
# ============================================================

project_config = ProjectConfig()

configuration_manager = ConfigurationManager(project_config)


if __name__ == "__main__":

    configuration_manager.create_directories()

    configuration_manager.validate()

    configuration_manager.summary()

    configuration_manager.save_json(
        project_config.paths.outputs / "project_configuration.json"
    )

    print()
    print("Configuration Hash")
    print(configuration_manager.configuration_hash())