# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pdf2md is a Python CLI tool that converts PDF files to Markdown using `pymupdf4llm`. Packaged with `hatchling`, managed with `uv`.

## Development

```bash
uv sync                     # install dependencies
uv run pdf2md --help         # run the CLI
uv run python -m pdf2md      # alternative invocation
uv build                     # build distributable
uv publish                   # publish to PyPI
```

## Architecture

src layout package (`src/pdf2md/`):
- `cli.py` — CLI entry point using argparse; `parse_pages()` converts 1-indexed page specs to 0-indexed lists, `main()` delegates to `pymupdf4llm.to_markdown()`
- `__main__.py` — enables `python -m pdf2md`
- `__init__.py` — version string

Console script entry point: `pdf2md = "pdf2md.cli:main"` (defined in `pyproject.toml`).
