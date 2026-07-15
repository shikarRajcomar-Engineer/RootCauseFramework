"""
====================================================================

Root Cause Attribution Framework

====================================================================

File:
    autoencoder.py

Description:
    TensorFlow implementation of a configurable Autoencoder.

    This class inherits from BaseModel and implements all
    functionality required to build, train, evaluate,
    save and load an autoencoder.

Author:
    Rajcomar

Framework Version:
    3.0.0

Python:
    3.10+

====================================================================
"""


from __future__ import annotations

from pathlib import Path

import tensorflow as tf

from tensorflow.keras import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense

from core.base_model import BaseModel
from config.model_config import ModelConfig


class Autoencoder(BaseModel):
    """
    Configurable TensorFlow Autoencoder.

    This implementation supports

        • Dynamic architectures
        • Any number of hidden layers
        • Latent feature extraction
        • Reconstruction
        • Model persistence
        • Training history
        • Future explainability methods

    Example
    --------

    autoencoder = Autoencoder(model_config)
    autoencoder.build_model()
    autoencoder.compile_model()
    autoencoder.train(X_train)
    predictions = autoencoder.predict(X_test)

    """


    def __init__(
        self,
        config: ModelConfig
    ):

        super().__init__(config)
        self.encoder = None
        self.decoder = None
        self.model = None

    def build_encoder(self):
        """
        Build encoder network.
        """

        architecture = self.config.architecture

        inputs = Input(
            shape=(architecture.input_dimension,),
            name="EncoderInput"
        )

        x = inputs

        for units in architecture.hidden_layers:

            x = Dense(
                units=units,
                activation=architecture.activation.value,
                use_bias=architecture.use_bias
            )(x)

        latent = Dense(
            units=architecture.latent_dimension,
            activation=architecture.activation.value,
            name="LatentSpace"
        )(x)

        self.encoder = Model(
            inputs,
            latent,
            name="Encoder"
        )

    def build_decoder(self):
        """
        Build decoder network.
        """

        architecture = self.config.architecture

        inputs = Input(
            shape=(architecture.latent_dimension,),
            name="DecoderInput"
        )

        x = inputs

        for units in reversed(
            architecture.hidden_layers
        ):

            x = Dense(
                units=units,
                activation=architecture.activation.value,
                use_bias=architecture.use_bias
            )(x)

        outputs = Dense(
            units=architecture.input_dimension,
            activation=architecture.output_activation.value,
            name="DecoderOutput"
        )(x)

        self.decoder = Model(
            inputs,
            outputs,
            name="Decoder"
        )

    def build_model(self):
        """
        Build the complete Autoencoder.
        """

        self.build_encoder()

        self.build_decoder()

        autoencoder_input = Input(
            shape=(
                self.config.architecture.input_dimension,
            ),
            name="AutoencoderInput"
        )

        encoded = self.encoder(
            autoencoder_input
        )

        reconstructed = self.decoder(
            encoded
        )

        self.model = Model(
            autoencoder_input,
            reconstructed,
            name=self.config.info.name
        )

    def summary(self):
        """
        Print model summary.
        """

        super().summary()

        self.model.summary()

    def validate(self):

        super().validate()

        if self.encoder is None:

            raise RuntimeError(
                "Encoder has not been built."
            )

        if self.decoder is None:

            raise RuntimeError(
                "Decoder has not been built."
            )
        
if __name__ == "__main__":

    from config.model_config import model_config

    autoencoder = Autoencoder(model_config)

    autoencoder.build_model()

    autoencoder.summary()