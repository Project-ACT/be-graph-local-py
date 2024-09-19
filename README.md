# be-graph-local-py

Creation and editing of local graph files for publication and automated discovery.

## Getting Started

1. Install required packages with Poetry.
2. Run `python main.py -f "tests/data/doap.rdf"` to run the program on an example file.

## Poetry Installation

To install Poetry, follow these steps:

1. Open your terminal or command prompt.
2. Run the following command to install Poetry:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    If you don't have `curl` installed, you can also use `wget`:

    ```bash
    wget -O - https://install.python-poetry.org | python3 -
    ```

3. Once the installation is complete, you can verify it by running:

    ```bash
    poetry --version
    ```

    This should display the version number of Poetry installed on your system.

Congratulations! You have successfully installed Poetry. You can now use it to manage your Python dependencies and projects.

For more information on how to use Poetry, refer to the [official documentation](https://python-poetry.org/docs/).

## Tests

Run `pytest` to run all the tests in the `tests/` directory.
