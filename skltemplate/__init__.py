# Authors: scikit-learn-contrib developers
# License: BSD 3 clause

from ._template import (
    TemplateClassifier,
    TemplateEstimator,
    TemplateTransformer,
    and_this_function,
)
from ._version import __version__
from .utils import discrovery

__all__ = [
    "TemplateEstimator",
    "TemplateClassifier",
    "TemplateTransformer",
    "and_this_function",
    "discrovery",
    "__version__",
]
