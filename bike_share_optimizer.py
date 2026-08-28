"""Backward-compatible entry point for the packaged project."""

from bike_share_optimizer import BikeShareOptimizer
from bike_share_optimizer.demo import build_demo_data, main

__all__ = ["BikeShareOptimizer", "build_demo_data"]


if __name__ == "__main__":
    main()
