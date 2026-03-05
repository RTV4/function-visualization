"""
main.py
-------
Visualizes mathematical functions using NumPy + Matplotlib.

Examples:
  python main.py all
  python main.py sine
  python main.py sine --frequency 3
  python main.py sine-multiples
  python main.py quadratic --a 1 --b -2 --c -3
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import functions


IMAGES_DIR = Path(__file__).resolve().parent / "images"


def ensure_images_dir() -> None:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)


def x_values(xmin: float = -10.0, xmax: float = 10.0, points: int = 1000) -> np.ndarray:
    return np.linspace(xmin, xmax, points)


def mark_extrema(ax: plt.Axes, x: np.ndarray, y: np.ndarray, label_prefix: str = "") -> None:
    """Option C: find min/max with NumPy and mark them in the plot."""
    i_max = int(np.argmax(y))
    i_min = int(np.argmin(y))
    ax.scatter([x[i_max]], [y[i_max]], marker="o", s=40, label=f"{label_prefix}max ({x[i_max]:.2f}, {y[i_max]:.2f})")
    ax.scatter([x[i_min]], [y[i_min]], marker="o", s=40, label=f"{label_prefix}min ({x[i_min]:.2f}, {y[i_min]:.2f})")


def save_plot(fig: plt.Figure, filename: str) -> Path:
    ensure_images_dir()
    out = IMAGES_DIR / filename
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def plot_single(
    name: str,
    x: np.ndarray,
    y: np.ndarray,
    title: str,
    xlabel: str = "x",
    ylabel: str = "f(x)",
    y_label_in_legend: str = "f(x)",
    filename: str = "plot.png",
    show_extrema: bool = True,
) -> Path:
    fig, ax = plt.subplots()
    ax.plot(x, y, label=y_label_in_legend)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if show_extrema:
        mark_extrema(ax, x, y, label_prefix="")
    ax.grid(True, alpha=0.25)
    ax.legend()
    return save_plot(fig, filename)


def plot_linear(args: argparse.Namespace, x: np.ndarray) -> Path:
    y = functions.linear(x, a=args.a, b=args.b)
    return plot_single(
        "linear",
        x,
        y,
        title=f"Lineární funkce: f(x) = a·x + b (a={args.a}, b={args.b})",
        y_label_in_legend="a·x + b",
        filename="linear.png",
        show_extrema=True,
    )


def plot_quadratic(args: argparse.Namespace, x: np.ndarray) -> Path:
    y = functions.quadratic(x, a=args.a, b=args.b, c=args.c)
    return plot_single(
        "quadratic",
        x,
        y,
        title=f"Kvadratická funkce: f(x) = a·x² + b·x + c (a={args.a}, b={args.b}, c={args.c})",
        y_label_in_legend="a·x² + b·x + c",
        filename="quadratic.png",
        show_extrema=True,
    )


def plot_sine(args: argparse.Namespace, x: np.ndarray) -> Path:
    y = functions.sine(x, amplitude=args.amplitude, frequency=args.frequency, phase=args.phase)
    return plot_single(
        "sine",
        x,
        y,
        title=f"Sinus: f(x) = A·sin(freq·x + phase) (A={args.amplitude}, freq={args.frequency}, phase={args.phase})",
        y_label_in_legend="A·sin(freq·x + phase)",
        filename="sine.png",
        show_extrema=True,
    )


def plot_exponential(args: argparse.Namespace, x: np.ndarray) -> Path:
    y = functions.exponential(x, k=args.k, base=args.base)
    return plot_single(
        "exponential",
        x,
        y,
        title=f"Exponenciální: f(x) = base^(k·x) (base={args.base}, k={args.k})",
        y_label_in_legend="base^(k·x)",
        filename="exponential.png",
        show_extrema=True,
    )


def plot_logistic(args: argparse.Namespace, x: np.ndarray) -> Path:
    y = functions.logistic(x, L=args.L, k=args.k, x0=args.x0)
    return plot_single(
        "logistic",
        x,
        y,
        title=f"Logistická: f(x) = L / (1 + e^(-k(x-x0))) (L={args.L}, k={args.k}, x0={args.x0})",
        y_label_in_legend="logistic",
        filename="logistic.png",
        show_extrema=True,
    )


def plot_multiple_functions(x: np.ndarray) -> Path:
    """Combined graph with at least three functions."""
    y1 = functions.linear(x, a=1.0, b=0.0)
    y2 = functions.quadratic(x, a=0.1, b=0.0, c=0.0)
    y3 = functions.sine(x, amplitude=5.0, frequency=1.0, phase=0.0)

    fig, ax = plt.subplots()
    ax.plot(x, y1, label="linear: x")
    ax.plot(x, y2, label="quadratic: 0.1·x²")
    ax.plot(x, y3, label="sine: 5·sin(x)")
    ax.set_title("Kombinovaný graf: lineární + kvadratická + sinus")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, alpha=0.25)
    ax.legend()
    return save_plot(fig, "multiple_functions.png")


def plot_sine_multiples(x: np.ndarray) -> Path:
    """Option B: automatically plot sin(x), sin(2x), sin(3x)."""
    fig, ax = plt.subplots()
    for freq in (1, 2, 3):
        y = functions.sine(x, amplitude=1.0, frequency=float(freq), phase=0.0)
        ax.plot(x, y, label=f"sin({freq}x)")
    ax.set_title("Sinus pro různé parametry: sin(x), sin(2x), sin(3x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, alpha=0.25)
    ax.legend()
    return save_plot(fig, "sine_multiples.png")


def plot_experiment() -> tuple[Path, Path]:
    """
    Experiment (task 8):
    Change interval for exponential to show how fast it grows.
      - Standard: x in [-10, 10] (saved as exponential.png by default when using exponential)
      - Experiment: x in [-2, 2] to keep values readable
    """
    x_std = x_values(-10, 10, 1000)
    x_small = x_values(-2, 2, 1000)

    # Use a slightly larger k so the effect is visible.
    k = 1.2

    y_std = functions.exponential(x_std, k=k, base=np.e)
    y_small = functions.exponential(x_small, k=k, base=np.e)

    # Standard-range plot (can blow up quickly; still saved for comparison)
    p1 = plot_single(
        "exp_std",
        x_std,
        y_std,
        title=f"Experiment: exponenciála na intervalu [-10, 10] (k={k})",
        y_label_in_legend="e^(k·x)",
        filename="experiment_exponential_wide.png",
        show_extrema=False,
    )

    # Smaller-range plot (readable)
    p2 = plot_single(
        "exp_small",
        x_small,
        y_small,
        title=f"Experiment: exponenciála na intervalu [-2, 2] (k={k})",
        y_label_in_legend="e^(k·x)",
        filename="experiment_exponential_small.png",
        show_extrema=False,
    )

    return p1, p2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Function visualization with NumPy + Matplotlib")
    p.add_argument(
        "target",
        choices=["all", "linear", "quadratic", "sine", "exponential", "logistic", "multiple", "sine-multiples", "experiment"],
        help="What to plot",
    )
    p.add_argument("--xmin", type=float, default=-10.0, help="x minimum")
    p.add_argument("--xmax", type=float, default=10.0, help="x maximum")
    p.add_argument("--points", type=int, default=1000, help="number of x points")

    # Generic params used by multiple plots; unused ones are ignored.
    p.add_argument("--a", type=float, default=1.0, help="linear/quadratic parameter a")
    p.add_argument("--b", type=float, default=0.0, help="linear/quadratic parameter b")
    p.add_argument("--c", type=float, default=0.0, help="quadratic parameter c")

    p.add_argument("--amplitude", type=float, default=1.0, help="sine amplitude")
    p.add_argument("--frequency", type=float, default=1.0, help="sine frequency")
    p.add_argument("--phase", type=float, default=0.0, help="sine phase")

    p.add_argument("--k", type=float, default=1.0, help="exponential/logistic slope parameter k")
    p.add_argument("--base", type=float, default=float(np.e), help="exponential base (default e)")

    p.add_argument("--L", type=float, default=1.0, help="logistic upper limit L")
    p.add_argument("--x0", type=float, default=0.0, help="logistic midpoint x0")

    return p


def main() -> None:
    args = build_parser().parse_args()
    x = x_values(args.xmin, args.xmax, args.points)

    outputs: list[Path] = []

    if args.target == "linear":
        outputs.append(plot_linear(args, x))
    elif args.target == "quadratic":
        outputs.append(plot_quadratic(args, x))
    elif args.target == "sine":
        outputs.append(plot_sine(args, x))
    elif args.target == "exponential":
        outputs.append(plot_exponential(args, x))
    elif args.target == "logistic":
        outputs.append(plot_logistic(args, x))
    elif args.target == "multiple":
        outputs.append(plot_multiple_functions(x))
    elif args.target == "sine-multiples":
        outputs.append(plot_sine_multiples(x))
    elif args.target == "experiment":
        outputs.extend(plot_experiment())
    elif args.target == "all":
        outputs.append(plot_linear(args, x))
        outputs.append(plot_quadratic(args, x))
        outputs.append(plot_sine(args, x))
        outputs.append(plot_exponential(args, x))
        outputs.append(plot_logistic(args, x))
        outputs.append(plot_multiple_functions(x))
        outputs.append(plot_sine_multiples(x))
        outputs.extend(plot_experiment())

    print("Generated images:")
    for pth in outputs:
        print(f" - {pth}")


if __name__ == "__main__":
    main()
