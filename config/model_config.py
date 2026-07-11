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
# PREDICTION CONFIGURATION
# ============================================================


@dataclass(slots=True)
class PredictionConfig:
    """
    Prediction configuration.

    Example
    -------

    model.prediction.batch_size = 512

    model.prediction.return_latent_vector = False

    model.prediction.return_reconstruction = True

    """

    batch_size: int = 512
    return_latent_vector: bool = False
    return_reconstruction: bool = True
    verbose: int = 0