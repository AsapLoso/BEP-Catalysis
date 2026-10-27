# BEP-Catalysis Codespace

Create a Codespace from the branch containing this configuration. The container installs Python 3.12, JupyterLab, and the VS Code Python, Jupyter, Pylance and Codex extensions. After creation, `uv sync --locked --project notebooks/v3` installs the V3 environment from its existing lock file. Select the `notebooks/v3/.venv` Python interpreter or kernel if VS Code does not select it automatically. Sign in to Codex in the extension when prompted.

Open the Codespace in VS Code desktop using the GitHub Codespaces extension. Work in the remote window so that the editor, notebook kernel, and Codex can work with the same remote files. Save editor changes before expecting another process to read them.

A Codespace is a separate Git checkout. OneDrive does not automatically mirror it to a local synced folder. Use reviewed commits and Git synchronization to transfer work, and inspect both checkouts for uncommitted, untracked, ignored or unpublished files before changing either. Files outside the repository are not automatically available in the Codespace.

The V3 lock file covers the dependencies declared in `notebooks/v3/pyproject.toml`; it does not establish that every other notebook or external data source is available. Verify the selected notebook and its inputs before running scientific work.
