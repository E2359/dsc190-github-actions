"""Small NumPy example used by the DSC 190 assignment."""

import numpy as np


def main() -> None:
    """Print the sum of a small NumPy array."""
    values = np.array([1, 2, 3])
    print(values.sum())


if __name__ == "__main__":
    main()
