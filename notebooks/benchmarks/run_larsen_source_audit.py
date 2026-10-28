"""Execute the separate Larsen source-law audit notebook in place."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient


NOTEBOOK = Path(__file__).with_name("larsen_2024_source_audit.ipynb")


def main() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(NOTEBOOK.parent)}},
    )
    executed = client.execute()
    nbformat.write(executed, NOTEBOOK)
    print(f"Executed {len(executed.cells)} cells in {NOTEBOOK}")


if __name__ == "__main__":
    main()
