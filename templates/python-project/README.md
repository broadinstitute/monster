# Example Python Project

This folder contains the standard configuration we use for Python projects:

* Config for a pre-commit hook to automatically lint Python code
* A Github action to run the following checks:
	* Require that type hints are present and that all types used are compatible
	* Require that there are no linting errors
	* Run the test suite and ensure that it passes
* Configuration for Poetry, our package/env system, including all necessary dependencies for the above.
* A basic `.gitignore` to avoid checking in caches or lockfiles.
* Some toy Python code to exercise these tools and demonstrate patterns like folder structure or type hints.


## Installation

To use this template for a repository that chiefly contains Python code, you can copy the entire directory to the root of your repository and use the `validate-python.yaml` workflow in `.github/workflows/` (deleting the other file).

If your Python code lives in a subdirectory of a non-Python repository:
* Copy everything but the `.github` folder to that directory
* Copy `.github` to the repository root
* Use `validate-python-subdirectory.yaml` instead of `validate-python.yaml`, updating `my-subdirectory` to whatever directory contains your Python code.
