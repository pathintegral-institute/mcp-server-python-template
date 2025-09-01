# Repository Guidelines

## Project Structure & Module Organization
- `src/mcp_server/server.py`: FastMCP server entrypoint. Add tools with `@mcp.tool()` and return `mcp.types` (e.g., `TextContent`, `ImageContent`).
- `src/mcp_server/__init__.py`: Package initialization, exports main function.
- `pyproject.toml`: Project metadata, runtime dependencies (Python 3.12+, `mcp`), and script configuration with src layout.
- Static assets: Place images and other files in the package directory (e.g., `src/mcp_server/lily.jpeg`).
- Growth pattern: Add tools to separate modules within `src/mcp_server/` and import them into `server.py`.

## Build, Test, and Development Commands
- Install (preferred): `uv sync` — installs dependencies from `pyproject.toml`/`uv.lock` into a local environment.
- Install for development: `uv pip install -e .` — installs the package in development mode with script access.
- Run via script: `uv run mcp-server` — starts the MCP server using the configured script entry point.
- Run directly: `uv run python src/mcp_server/server.py` — alternative direct execution.
- Run (HTTP): uncomment `mcp.run(transport="streamable-http")` in `server.py` and run the same command.
- Alternative (pip): create and activate a venv, then `pip install mcp` and run the server.

## Coding Style & Naming Conventions
- Python: 4‑space indentation, PEP 8, type hints required for tool signatures.
- Tool names: use clear, verb‑based names (`get_`, `list_`, `add_`). Keep tools idempotent and side‑effect‑aware.
- Docstrings: one‑line summary + short params/returns note; keep descriptions user‑facing.
- Import organization: standard libraries first, then `mcp` imports, then local imports.
- For binary data (images): use `base64` encoding and proper `mimeType` in `ImageContent`.

## Testing Guidelines
- Framework: `pytest` (not yet included). Place tests under `tests/` as `test_*.py`.
- Run tests: `uv run pytest -q` (after adding `pytest`).
- Aim for small, fast unit tests per tool, including error paths and type checks.

## Commit & Pull Request Guidelines
- Commits: imperative mood, concise scope; Conventional Commits encouraged (e.g., `feat: add add()` tool`).
- PRs: include summary, linked issues, testing steps, and screenshots/logs when behavior changes. Note any transport/default behavior changes.

## Security & Configuration Tips
- Do not commit secrets or `.venv/`. Use environment variables for tokens/keys.
- Keep dependencies pinned via `uv.lock`. Maintain Python version per `.python-version` and `requires-python`.
- Validate tool inputs and return helpful error messages; avoid leaking sensitive data in outputs.

## Package Configuration Notes
- Uses src layout with `src/mcp_server/` package structure for better organization.
- Script entry point configured in `pyproject.toml` as `mcp-server = "mcp_server.server:main"`.
- Development installation via `uv pip install -e .` enables the `uv run mcp-server` command.
- Package discovery configured with `[tool.setuptools.packages.find]` for proper src layout support.

