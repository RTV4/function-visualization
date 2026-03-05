"""
functions.py
-----------
Collection of mathematical functions for visualization.

Each function accepts x (NumPy array or scalar) and parameters that can be varied.
"""

from __future__ import annotations
import numpy as np


def linear(x: np.ndarray, a: float = 1.0, b: float = 0.0) -> np.ndarray:
    """f(x) = a*x + b"""
    return a * x + b


def quadratic(x: np.ndarray, a: float = 1.0, b: float = 0.0, c: float = 0.0) -> np.ndarray:
    """f(x) = a*x^2 + b*x + c"""
    return a * x**2 + b * x + c


def sine(x: np.ndarray, amplitude: float = 1.0, frequency: float = 1.0, phase: float = 0.0) -> np.ndarray:
    """f(x) = A * sin(freq*x + phase)"""
    return amplitude * np.sin(frequency * x + phase)


def exponential(x: np.ndarray, k: float = 1.0, base: float = np.e) -> np.ndarray:
    """f(x) = base^(k*x) ; default base = e"""
    return np.power(base, k * x)


def logistic(x: np.ndarray, L: float = 1.0, k: float = 1.0, x0: float = 0.0) -> np.ndarray:
    """f(x) = L / (1 + e^{-k(x-x0)})"""
    return L / (1.0 + np.exp(-k * (x - x0)))
