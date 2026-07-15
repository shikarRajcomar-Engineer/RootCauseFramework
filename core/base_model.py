"""
====================================================================

Root Cause Attribution Framework

====================================================================

File:
    base_model.py

Description:
    Abstract base class for every machine learning model
    used throughout the framework.

Every model should inherit from this class.

Author:
    Rajcomar

Version:
    3.0.0

====================================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from pathlib import Path
from datetime import datetime

import json
import pickle

import pandas as pd

from config.model_config import ModelConfig

class BaseModel(ABC):
    """
    Abstract base class for every model in the framework.

    Every model inherits

    • save()

    • load()

    • summary()

    • save_history()

    • save_metrics()

    • save_configuration()

    etc.
    """

    def __init__(
        self,
        config: ModelConfig
    ):

        self.config = config
        self.model = None
        self.scaler = None
        self.history = None
        self.training_metrics = {}
        self.metadata = {}
        self.created = datetime.now()

    @abstractmethod
    def train(
        self,
        X_train,
        X_validation=None
    ):
        """
        Train the model.
        """
        pass

    @abstractmethod
    def predict(
        self,
        X
    ):
        """
        Predict using the model.
        """
        pass

    @abstractmethod
    def save_model(
        self
    ):
        """
        Save trained model.
        """
        pass

    @abstractmethod
    def load_model(
        self
    ):
        """
        Load trained model.
        """
        pass

    def save_scaler(
        self,
        filename: Path
    ):

        with open(filename, "wb") as file:

            pickle.dump(
                self.scaler,
                file
            )

    def load_scaler(
        self,
        filename: Path
    ):

        with open(filename, "rb") as file:

            self.scaler = pickle.load(file)

    def save_history(
        self,
        filename: Path
    ):

        if self.history is None:

            return

        pd.DataFrame(
            self.history.history
        ).to_excel(
            filename,
            index=False
        )

    def save_metrics(
        self,
        filename: Path
    ):

        pd.DataFrame(
            [self.training_metrics]
        ).to_excel(
            filename,
            index=False
        )


    def save_metadata(
        self,
        filename: Path
    ):

        metadata = {

            "Model Name":
            self.config.info.name,

            "Model ID":
            self.config.info.model_id,

            "Created":
            str(self.created),

            "Framework Version":
            "3.0.0"
        }

        with open(
            filename,
            "w"
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4
            )

    def save_configuration(
        self,
        filename: Path
    ):

        from config.model_config import (
            ModelConfigurationManager
        )

        manager = ModelConfigurationManager(
            self.config
        )

        manager.save_json(
            filename
        )

    def summary(self):

        print("=" * 70)

        print(self.config.info.name)

        print("=" * 70)

        print("Model ID :", self.config.info.model_id)

        print("Type :", self.config.info.model_type.name)

        print("Version :", self.config.storage.model_version)

        print("=" * 70)

    def validate(self):

        if self.model is None:

            raise RuntimeError(
                "Model has not been created."
            )
# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("BaseModel is an abstract base class.")
    print("It cannot be executed directly.")
    print()
    print("Instantiate a derived model instead, for example:")
    print("    Autoencoder")
    print("    SensorAutoencoder")
    print("    BayesianNetwork")
    print("=" * 70)