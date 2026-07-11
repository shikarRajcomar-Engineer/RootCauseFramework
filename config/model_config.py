"""
====================================================================
Root Cause Attribution Framework
====================================================================

File:
    model_config.py

Description:
    Central model configuration for the Root Cause Attribution
    Framework.

This module defines HOW machine learning models are configured.

It intentionally DOES NOT contain

    • Model implementation
    • Model training
    • Dataset loading
    • Bayesian inference

Those are handled by their own modules.

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

DEFAULT_MODEL_NAME = "Unnamed Model"
DEFAULT_AUTHOR = "Rajcomar"
DEFAULT_VERSION = "1.0"
DEFAULT_RANDOM_SEED = 42
DEFAULT_LEARNING_RATE = 0.001
DEFAULT_BATCH_SIZE = 32
DEFAULT_EPOCHS = 100

# ============================================================
# ENUMS
# ============================================================


class ModelType(Enum):
    """
    Supported model types.
    """

    AUTOENCODER = "Autoencoder"
    VARIATIONAL_AUTOENCODER = "Variational Autoencoder"
    SPARSE_AUTOENCODER = "Sparse Autoencoder"
    DENOISING_AUTOENCODER = "Denoising Autoencoder"
    LSTM_AUTOENCODER = "LSTM Autoencoder"
    PCA = "Principal Component Analysis"
    ISOLATION_FOREST = "Isolation Forest"
    ONE_CLASS_SVM = "One-Class SVM"
    CUSTOM = "Custom"


class ActivationFunction(Enum):
    """
    Activation functions.
    """

    RELU = "relu"
    SIGMOID = "sigmoid"
    TANH = "tanh"
    LINEAR = "linear"
    ELU = "elu"
    GELU = "gelu"
    SELU = "selu"


class OptimizerType(Enum):
    """
    Optimizers.
    """

    ADAM = "Adam"
    SGD = "SGD"
    RMSPROP = "RMSprop"
    ADAMW = "AdamW"

class LossFunction(Enum):
    """
    Loss functions.
    """

    MSE = "Mean Squared Error"
    MAE = "Mean Absolute Error"
    HUBER = "Huber"
    BINARY_CROSSENTROPY = "Binary Crossentropy"
    CUSTOM = "Custom"

# ============================================================
# MODEL INFORMATION
# ============================================================


@dataclass(slots=True)
class ModelInfo:
    """
    General information about a model.
    """

    name: str = DEFAULT_MODEL_NAME
    description: str = ""
    version: str = DEFAULT_VERSION
    author: str = DEFAULT_AUTHOR
    model_id: str = "MODEL001"
    created: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    model_type: ModelType = (ModelType.AUTOENCODER)


# ============================================================
# MODEL ARCHITECTURE
# ============================================================


@dataclass(slots=True)
class ArchitectureConfig:
    """
    Model architecture configuration.

    model.architecture.input_dimension = 7

    model.architecture.hidden_layers =[64,32,16]

    model.architecture.latent_dimension = 8

    model.architecture.activation =ActivationFunction.RELU

    model.architecture.output_activation =ActivationFunction.LINEAR

    model.architecture.use_bias = True

    """


    input_dimension: int = 0
    hidden_layers: list[int] = field(default_factory=list)
    latent_dimension: int = 8
    activation: ActivationFunction = (ActivationFunction.RELU)
    output_activation: ActivationFunction = (ActivationFunction.LINEAR)
    use_bias: bool = True


    # ============================================================
# TRAINING CONFIGURATION
# ============================================================


@dataclass(slots=True)
class TrainingConfig:
    """
    Training configuration.

    Example
    -------

    model.training.train_model = True

    model.training.epochs = 200

    model.training.batch_size = 64

    model.training.shuffle = True

    model.training.validation_split = 0.20

    model.training.random_seed = 42

    model.training.verbose = 1

    """

    train_model: bool = True
    epochs: int = DEFAULT_EPOCHS
    batch_size: int = DEFAULT_BATCH_SIZE
    shuffle: bool = True
    validation_split: float = 0.20
    random_seed: int = DEFAULT_RANDOM_SEED
    verbose: int = 1

    # ============================================================
# OPTIMIZER CONFIGURATION
# ============================================================


@dataclass(slots=True)
class OptimizerConfig:
    """
    Optimizer configuration.

    Example
    -------

    model.optimizer.optimizer = OptimizerType.ADAM

    model.optimizer.learning_rate = 0.001

    model.optimizer.beta1 = 0.9

    model.optimizer.beta2 = 0.999

    model.optimizer.epsilon = 1e-7

    """

    optimizer: OptimizerType = OptimizerType.ADAM
    learning_rate: float = DEFAULT_LEARNING_RATE
    beta1: float = 0.9
    beta2: float = 0.999
    epsilon: float = 1e-7

# ============================================================
# LOSS CONFIGURATION
# ============================================================


@dataclass(slots=True)
class LossConfig:
    """
    Loss configuration.

    Example
    -------

    model.loss.loss_function = LossFunction.MSE

    model.loss.reduction = "sum_over_batch_size"

    """

    loss_function: LossFunction = LossFunction.MSE
    reduction: str = "sum_over_batch_size"

# ============================================================
# REGULARIZATION CONFIGURATION
# ============================================================


@dataclass(slots=True)
class RegularizationConfig:
    """
    Regularization configuration.

    Example
    -------

    model.regularization.use_dropout = True

    model.regularization.dropout_rate = 0.30

    model.regularization.use_batch_normalization = True

    model.regularization.l1 = 0.0

    model.regularization.l2 = 0.0001

    """

    use_dropout: bool = False
    dropout_rate: float = 0.30
    use_batch_normalization: bool = False
    l1: float = 0.0
    l2: float = 0.0

# ============================================================
# EARLY STOPPING CONFIGURATION
# ============================================================


@dataclass(slots=True)
class EarlyStoppingConfig:
    """
    Early stopping configuration.

    Example
    -------

    model.early_stopping.enabled = True

    model.early_stopping.monitor = "val_loss"

    model.early_stopping.patience = 20

    model.early_stopping.restore_best_weights = True

    """

    enabled: bool = True
    monitor: str = "val_loss"
    patience: int = 20
    min_delta: float = 0.0
    restore_best_weights: bool = True

# ============================================================
# CHECKPOINT CONFIGURATION
# ============================================================


@dataclass(slots=True)
class CheckpointConfig:
    """
    Model checkpoint configuration.

    Example
    -------

    model.checkpoint.enabled = True

    model.checkpoint.monitor = "val_loss"

    model.checkpoint.save_best_only = True

    model.checkpoint.save_weights_only = False

    """

    enabled: bool = True
    monitor: str = "val_loss"
    save_best_only: bool = True
    save_weights_only: bool = False
    mode: str = "min"

# ============================================================
# MODEL STORAGE CONFIGURATION
# ============================================================
@dataclass(slots=True)
class ModelStorageConfig:
    """
    Model storage configuration.

    Example
    -------

    model.storage.use_saved_model = True

    model.storage.auto_load_if_exists = True

    model.storage.save_model = True

    model.storage.save_scaler = True

    model.storage.save_history = True

    model.storage.save_configuration = True

    model.storage.model_directory = "models"

    model.storage.model_name = "MainAutoencoder"

    model.storage.model_version = "v1"

    """

    use_saved_model: bool = False
    auto_load_if_exists: bool = True
    save_model: bool = True
    save_scaler: bool = True
    save_history: bool = True
    save_training_curves: bool = True
    save_configuration: bool = True
    save_optimizer_state: bool = False
    model_directory: str = "models"
    model_name: str = "UnnamedModel"
    model_version: str = "v1"
    overwrite_existing: bool = False
    export_tensorflow: bool = True
    export_onnx: bool = False


# ============================================================
# HYPERPARAMETER CONFIGURATION
# ============================================================
@dataclass(slots=True)
class HyperparameterConfig:
    """
    Hyperparameter search configuration.

    Example
    -------

    model.hyperparameters.enabled = True
    model.hyperparameters.search_method = "GridSearch"
    model.hyperparameters.learning_rates = [0.01,0.001,0.0001]
    model.hyperparameters.batch_sizes = [32,64,128]
    model.hyperparameters.latent_dimensions = [4,8,16]
    model.hyperparameters.hidden_layer_options = [
        [64,32],
        [128,64,32]
    ]

    model.hyperparameters.dropout_rates = [0.0,0.2,0.3]
    model.hyperparameters.optimizers = [
        OptimizerType.ADAM,
        OptimizerType.RMSPROP
    ]

    """

    enabled: bool = False
    search_method: str = "Manual"
    max_trials: int = 50
    random_seed: int = DEFAULT_RANDOM_SEED
    learning_rates: list[float] = field(
        default_factory=lambda: [0.001]
    )
    batch_sizes: list[int] = field(
        default_factory=lambda: [32]
    )
    epochs: list[int] = field(
        default_factory=lambda: [100]
    )
    latent_dimensions: list[int] = field(
        default_factory=lambda: [8]
    )
    hidden_layer_options: list[list[int]] = field(
        default_factory=lambda: [[64, 32]]
    )
    dropout_rates: list[float] = field(
        default_factory=lambda: [0.0]
    )
    optimizers: list[OptimizerType] = field(
        default_factory=lambda: [OptimizerType.ADAM]
    )
    activations: list[ActivationFunction] = field(
        default_factory=lambda: [ActivationFunction.RELU]
    )

# ============================================================
# PREDICTION CONFIGURATION
# ============================================================


@dataclass(slots=True)
class PredictionConfig:
    """
    Prediction configuration.

    Example
    -------

    model.prediction.batch_size = 512

    model.prediction.return_reconstruction = True

    model.prediction.return_latent_vector = False

    model.prediction.verbose = 0

    """

    batch_size: int = 512

    return_reconstruction: bool = True

    return_latent_vector: bool = False

    verbose: int = 0

# ============================================================
# MASTER MODEL CONFIGURATION
# ============================================================


@dataclass(slots=True)
class ModelConfig:
    """
    Master model configuration.

    Example
    -------

    model.info.name

    model.architecture.hidden_layers

    model.training.epochs

    model.storage.model_directory

    """

    info: ModelInfo = field(default_factory=ModelInfo)

    architecture: ArchitectureConfig = field(default_factory=ArchitectureConfig)

    training: TrainingConfig = field(default_factory=TrainingConfig)

    optimizer: OptimizerConfig = field(default_factory=OptimizerConfig)

    loss: LossConfig = field(default_factory=LossConfig)

    regularization: RegularizationConfig = field(default_factory=RegularizationConfig)

    early_stopping: EarlyStoppingConfig = field(default_factory=EarlyStoppingConfig)

    checkpoint: CheckpointConfig = field(default_factory=CheckpointConfig)

    storage: ModelStorageConfig = field(default_factory=ModelStorageConfig)

    prediction: PredictionConfig = field(default_factory=PredictionConfig)

    hyperparameters: HyperparameterConfig = field(default_factory=HyperparameterConfig)

# ============================================================
# CONFIGURATION ERROR
# ============================================================


class ModelConfigurationError(Exception):
    """
    Raised when the model configuration is invalid.
    """
    pass

# ============================================================
# MODEL CONFIGURATION MANAGER
# ============================================================

import json
import hashlib
from dataclasses import asdict


class ModelConfigurationManager:
    """
    Utility class for validating, exporting and
    summarising model configurations.
    """

    def __init__(self, config: ModelConfig):
        self.config = config

    # ========================================================
    # VALIDATION
    # ========================================================

    def validate(self) -> None:
        """
        Validate the configuration.

        NOTE
        ----
        This validates ONLY configuration values.

        Runtime validation (input dimensions, datasets,
        model files, etc.) is performed later by the
        training and inference pipelines.
        """

        if self.config.training.epochs <= 0:
            raise ModelConfigurationError(
                "Training epochs must be greater than zero."
            )

        if self.config.training.batch_size <= 0:
            raise ModelConfigurationError(
                "Batch size must be greater than zero."
            )

        if not 0.0 <= self.config.training.validation_split <= 1.0:
            raise ModelConfigurationError(
                "Validation split must be between 0 and 1."
            )

        if self.config.optimizer.learning_rate <= 0:
            raise ModelConfigurationError(
                "Learning rate must be greater than zero."
            )

        if not 0.0 <= self.config.regularization.dropout_rate <= 1.0:
            raise ModelConfigurationError(
                "Dropout rate must be between 0 and 1."
            )

        if self.config.early_stopping.patience < 0:
            raise ModelConfigurationError(
                "Early stopping patience cannot be negative."
            )

    # ========================================================
    # EXPORT
    # ========================================================

    def to_dictionary(self) -> dict:
        """
        Convert the configuration to a dictionary.
        """

        return self._convert(asdict(self.config))

    def save_json(self, filename: str | Path) -> None:
        """
        Save the configuration as a JSON file.
        """

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                self.to_dictionary(),
                file,
                indent=4
            )

    # ========================================================
    # HASHING
    # ========================================================

    def configuration_hash(self) -> str:
        """
        Generate a unique SHA256 hash for the
        current configuration.
        """

        configuration = json.dumps(
            self.to_dictionary(),
            sort_keys=True
        )

        return hashlib.sha256(
            configuration.encode("utf-8")
        ).hexdigest()

    # ========================================================
    # INTERNAL UTILITIES
    # ========================================================

    @staticmethod
    def _convert(item):
        """
        Convert enums into strings so the configuration
        can be exported to JSON.
        """

        if isinstance(item, Enum):
            return item.name

        if isinstance(item, dict):
            return {
                key: ModelConfigurationManager._convert(value)
                for key, value in item.items()
            }

        if isinstance(item, list):
            return [
                ModelConfigurationManager._convert(value)
                for value in item
            ]

        return item

    # ========================================================
    # SUMMARY
    # ========================================================

    def summary(self) -> None:
        """
        Print a summary of the model configuration.
        """

        print("=" * 70)
        print(self.config.info.name)
        print("=" * 70)

        print(f"Model Type         : {self.config.info.model_type.name}")
        print(f"Model ID           : {self.config.info.model_id}")
        print(f"Model Version      : {self.config.storage.model_version}")

        print()

        print(f"Input Dimension    : {self.config.architecture.input_dimension}")
        print(f"Hidden Layers      : {self.config.architecture.hidden_layers}")
        print(f"Latent Dimension   : {self.config.architecture.latent_dimension}")

        print()

        print(f"Epochs             : {self.config.training.epochs}")
        print(f"Batch Size         : {self.config.training.batch_size}")
        print(f"Learning Rate      : {self.config.optimizer.learning_rate}")
        print(f"Optimizer          : {self.config.optimizer.optimizer.name}")
        print(f"Loss Function      : {self.config.loss.loss_function.name}")

        print()

        print(f"Train Model        : {self.config.training.train_model}")
        print(f"Use Saved Model    : {self.config.storage.use_saved_model}")
        print(f"Auto Load Model    : {self.config.storage.auto_load_if_exists}")

        print()

        print(f"Model Directory    : {self.config.storage.model_directory}")
        print(f"Model Name         : {self.config.storage.model_name}")

        print("=" * 70)

# ============================================================
# DEFAULT MODEL CONFIGURATION
# ============================================================

model = ModelConfig()

configuration_manager = ModelConfigurationManager(model)

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    configuration_manager.validate()

    configuration_manager.summary()

    configuration_manager.save_json(
        "model_configuration.json"
    )

    print()

    print("Configuration Hash")

    print(configuration_manager.configuration_hash())