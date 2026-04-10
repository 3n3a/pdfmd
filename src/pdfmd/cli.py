"""pdf2md - Convert PDF files to Markdown using pymupdf4llm."""

import argparse
import sys
from pathlib import Path

import pymupdf4llm


def parse_pages(spec: str) -> list[int]:
    """Parse a page spec like '1,3,5-8' into a 0-indexed list."""
    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            pages.update(range(int(start) - 1, int(end)))
        else:
            pages.add(int(part) - 1)
    return sorted(pages)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Convert a PDF to Markdown.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("input", type=Path, help="input PDF file")
    ap.add_argument(
        "-o", "--output", type=Path,
        help="output .md file (default: input with .md extension, '-' for stdout)",
    )
    ap.add_argument(
        "-p", "--pages", type=str,
        help="pages to extract, e.g. '1,3,5-8' (1-indexed). default: all",
    )
    ap.add_argument(
        "--images", action="store_true",
        help="extract embedded images alongside the markdown",
    )
    ap.add_argument(
        "--image-dir", type=Path, default=Path("images"),
        help="directory for extracted images",
    )
    ap.add_argument(
        "--image-format", default="png", choices=["png", "jpg"],
        help="image format",
    )
    ap.add_argument(
        "--dpi", type=int, default=150,
        help="DPI for rendered/extracted images",
    )
    ap.add_argument(
        "--table-strategy", default="lines", choices=["lines", "lines_strict"],
        help="table detection strategy",
    )
    ap.add_argument(
        "-q", "--quiet", action="store_true",
        help="suppress progress output",
    )
    args = ap.parse_args()

    if not args.input.is_file():
        sys.exit(f"error: {args.input} not found")

    kwargs = {
        "table_strategy": args.table_strategy,
        "dpi": args.dpi,
        "show_progress": not args.quiet,
    }
    if args.pages:
        try:
            kwargs["pages"] = parse_pages(args.pages)
        except ValueError:
            sys.exit(f"error: invalid page spec: {args.pages!r}")
    if args.images:
        args.image_dir.mkdir(parents=True, exist_ok=True)
        kwargs["write_images"] = True
        kwargs["image_path"] = str(args.image_dir)
        kwargs["image_format"] = args.image_format

    try:
        md = pymupdf4llm.to_markdown(str(args.input), **kwargs)
    except Exception as e:
        sys.exit(f"error: conversion failed: {e}")

    if args.output and str(args.output) == "-":
        sys.stdout.write(md)
    else:
        out = args.output or args.input.with_suffix(".md")
        out.write_text(md, encoding="utf-8")
        if not args.quiet:
            print(f"wrote {out} ({len(md):,} chars)", file=sys.stderr)

    return 0
