# pdfmd

Convert PDF files to Markdown using [pymupdf4llm](https://github.com/pymupdf/RAG).

## Installation

```bash
# Install from PyPI
pip install pdfmd

# Or as a uv tool
uv tool install pdfmd
```

For development:

```bash
git clone https://github.com/3n3a/pdfmd.git
cd pdfmd
uv sync
```

## Usage

```bash
pdfmd input.pdf                          # writes input.md
pdfmd input.pdf -o output.md             # explicit output path
pdfmd input.pdf -o -                     # stdout
pdfmd input.pdf -p "1,3,5-8"            # specific pages (1-indexed)
pdfmd input.pdf --images --dpi 200       # extract images
```

Run `pdfmd --help` for all options.

## Build & Publish

```bash
uv build      # creates dist/*.whl and dist/*.tar.gz
uv publish    # publish to PyPI
```
