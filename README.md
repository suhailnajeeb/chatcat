# chatcat

A CLI tool to dump codebase files into LLM/chat-friendly text or markdown format.

## Features
- Select files by glob or file list
- Output as plain text or markdown code fences
- CLI powered by Click
- Modular and extensible core

## Installation

From the project root:

```sh
pip install -e chatcat --break-system-packages
```

## Usage

Basic usage:

```sh
chatcat . --out dump.md --only "*.py" --markdown
```

### Options
- `directory` (argument): Path to the base directory (default: `.`)
- `--only` or `-o`: Multiple glob patterns to select files (e.g., `--only "*.py" --only "*.md"`)
- `--file-list` or `-f`: Path to a text file listing files to dump, one per line
- `--out` or `-O`: Write output to the given file (if not provided, prints to stdout)
- `--markdown/--no-markdown`: Option to wrap contents in markdown code fences (default: True)

### Example

```sh
chatcat src --out code_dump.md --only "*.py" --only "*.md" --markdown
```

## Development

- All source code is in `chatcat/src/chatcat`.
- Run tests with:
  ```sh
  pytest tests/
  ```

## License
See LICENSE.
