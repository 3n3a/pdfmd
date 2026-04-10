# pdf2md

Convert PDF files to Markdown using [pymupdf4llm](https://github.com/pymupdf/RAG).

## Installation

```bash
# With uv
uv sync

# Or with pip
pip install .
```

## Usage

```bash
pdf2md input.pdf                          # writes input.md
pdf2md input.pdf -o output.md             # explicit output path
pdf2md input.pdf -o -                     # stdout
pdf2md input.pdf -p "1,3,5-8"            # specific pages (1-indexed)
pdf2md input.pdf --images --dpi 200       # extract images
```

Run `pdf2md --help` for all options.

## Build & Publish

```bash
uv build      # creates dist/*.whl and dist/*.tar.gz
uv publish    # publish to PyPI
```
