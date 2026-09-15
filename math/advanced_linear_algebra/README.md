# Advanced Linear Algebra

This project builds on basic matrix operations and implements core concepts
from linear algebra using Python lists and NumPy where required.

## Learning Objectives

At the end of this project, you should be able to explain and implement:

- The determinant of a square matrix.
- The minor matrix of a square matrix.
- The cofactor matrix and cofactor signs.
- The adjugate matrix as the transpose of the cofactor matrix.
- The inverse of a matrix using its determinant and adjugate.
- The relationship between a zero determinant and a non-invertible matrix.
- How eigenvalues can be used to classify the definiteness of a matrix.
- Input validation for square matrices and appropriate error handling.

## Tasks

| File | Function | Purpose |
| --- | --- | --- |
| `0-determinant.py` | `determinant` | Calculates the determinant of a matrix. |
| `1-minor.py` | `minor` | Calculates the minor matrix. |
| `2-cofactor.py` | `cofactor` | Calculates the cofactor matrix. |
| `3-adjugate.py` | `adjugate` | Calculates the adjugate matrix. |
| `4-inverse.py` | `inverse` | Calculates the inverse when it exists. |
| `5-definiteness.py` | `definiteness` | Classifies a matrix using its eigenvalues. |

## Requirements

- Use Python 3.
- Every script must begin with `#!/usr/bin/env python3`.
- Every script must be executable and end with a newline.
- All modules and functions must have documentation.
- Follow `pycodestyle` conventions.
- Do not import modules unless the task requires it. NumPy is used by
  `5-definiteness.py`.

## Running the Scripts

From this directory, run a script with:

```bash
./0-determinant.py
```

The functions are designed to be imported and tested with matrices represented
as lists of lists, except `definiteness`, which expects a NumPy array.
