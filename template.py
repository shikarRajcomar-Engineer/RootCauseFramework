"""
Root Cause Attribution Framework V3
Project Structure Generator

Author: Rajcomar
"""

from pathlib import Path

# ==========================================================
# PROJECT NAME
# ==========================================================

PROJECT_NAME = "RootCauseFramework"

# ==========================================================
# COMPLETE PROJECT STRUCTURE
# ==========================================================

structure = {

    # Root Files
    "README.md": "",
    "requirements.txt": "",
    ".gitignore": "",
    "run.py": "",
    "train.py": "",
    "evaluate.py": "",
    "LICENSE": "",

    # ======================================================
    # CONFIG
    # ======================================================

    "config": {

        "__init__.py": "",

        "project_config.py": "",
        "dataset_config.py": "",
        "experiment_config.py": "",
        "model_config.py": "",
        "signal_config.py": "",
        "bayesian_config.py": "",
        "report_config.py": "",
        "plotting_config.py": ""

    },

    # ======================================================
    # CORE
    # ======================================================

    "core": {

        "__init__.py": "",

        "logger.py": "",
        "paths.py": "",
        "constants.py": "",
        "exceptions.py": "",
        "helpers.py": "",
        "validation.py": "",
        "environment.py": "",
        "version.py": ""

    },

    # ======================================================
    # DATASETS
    # ======================================================

    "datasets": {

        "__init__.py": "",

        "base_dataset.py": "",
        "loader.py": "",
        "preprocessing.py": "",
        "windowing.py": "",
        "cache.py": "",
        "validators.py": "",
        "normalization.py": ""

    },

    # ======================================================
    # MODELS
    # ======================================================

    "models": {

        "__init__.py": "",

        "architecture.py": "",
        "autoencoder.py": "",
        "trainer.py": "",
        "predictor.py": "",
        "reconstruction.py": "",
        "model_loader.py": "",
        "losses.py": "",
        "metrics.py": ""

    },

    # ======================================================
    # SIGNALS
    # ======================================================

    "signals": {

        "__init__.py": "",

        "magnitude.py": "",
        "disruption.py": "",
        "consistency.py": "",
        "temporal.py": "",
        "fusion.py": "",
        "normalization.py": ""

    },

    # ======================================================
    # BAYESIAN
    # ======================================================

    "bayesian": {

        "__init__.py": "",

        "priors.py": "",
        "likelihoods.py": "",
        "posterior.py": "",
        "gaussian.py": "",
        "entropy.py": "",
        "ranking.py": "",
        "calibration.py": ""

    },

    # ======================================================
    # EXPERIMENTS
    # ======================================================

    "experiments": {

        "__init__.py": "",

        "experiment_manager.py": "",

        "baseline.py": "",

        "signal_ablation.py": "",

        "window_ablation.py": "",

        "summary_ablation.py": "",

        "prior_ablation.py": "",

        "shrinkage_ablation.py": "",

        "fusion_ablation.py": "",

        "factorial.py": ""

    },

    # ======================================================
    # EVALUATION
    # ======================================================

    "evaluation": {

        "__init__.py": "",

        "accuracy.py": "",
        "topk.py": "",
        "confusion_matrix.py": "",
        "classification_report.py": "",
        "bootstrap.py": "",
        "confidence_intervals.py": "",
        "wilcoxon.py": "",
        "mcnemar.py": "",
        "effect_size.py": "",
        "ranking_metrics.py": ""

    },

    # ======================================================
    # REPORTING
    # ======================================================

    "reporting": {

        "__init__.py": "",

        "excel_report.py": "",
        "latex_report.py": "",
        "metadata.py": "",
        "manifest.py": "",
        "summary.py": ""

    },

    # ======================================================
    # VISUALIZATION
    # ======================================================

    "visualization": {

        "__init__.py": "",

        "barplots.py": "",
        "boxplots.py": "",
        "heatmaps.py": "",
        "radar.py": "",
        "roc.py": "",
        "calibration.py": "",
        "sensor_plots.py": "",
        "posterior_plots.py": ""

    },

    # ======================================================
    # UTILS
    # ======================================================

    "utils": {

        "__init__.py": "",

        "file_utils.py": "",
        "math_utils.py": "",
        "statistics.py": "",
        "timer.py": "",
        "seed.py": ""

    },

    # ======================================================
    # TESTS
    # ======================================================

    "tests": {

        "__init__.py": "",

        "test_signals.py": "",
        "test_bayesian.py": "",
        "test_dataset.py": "",
        "test_models.py": ""

    },

    # ======================================================
    # DATA
    # ======================================================

    "data": {

        "raw": {},

        "processed": {},

        "cache": {}

    },

    # ======================================================
    # OUTPUTS
    # ======================================================

    "outputs": {

        "Excel": {},
        "Figures": {},
        "Latex": {},
        "Metadata": {},
        "Logs": {}

    },

    # ======================================================
    # LOGS
    # ======================================================

    "logs": {

    }

}


# ==========================================================
# CREATE FUNCTION
# ==========================================================

def create_structure(base_path, structure):

    for name, content in structure.items():

        path = base_path / name

        if isinstance(content, dict):

            path.mkdir(parents=True, exist_ok=True)

            create_structure(path, content)

        else:

            path.parent.mkdir(parents=True, exist_ok=True)

            path.touch(exist_ok=True)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    project_root = Path(PROJECT_NAME)

    project_root.mkdir(exist_ok=True)

    create_structure(project_root, structure)

    print("=" * 60)
    print(" Root Cause Attribution Framework Created Successfully")
    print("=" * 60)
    print(f"Location : {project_root.resolve()}")
    print("=" * 60)