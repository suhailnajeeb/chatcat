from pathlib import Path
from typing import Iterable, List, Optional, Union

# Mapping from file extension to language for markdown code fences
EXT_LANG_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".dart": "dart",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".h": "c",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".md": "markdown",
    ".sh": "bash",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".toml": "toml",
    ".txt": "text",
    # Add more as needed
}

def iter_files(base: Union[str, Path], globs: Optional[List[str]] = None, file_list: Optional[List[Union[str, Path]]] = None) -> Iterable[Path]:
    """
    Iterate over files to include in the dump.
    If file_list is provided, yield those files.
    Otherwise, use globs or default to ["**/*"] to include all files.
    """
    base = Path(base)
    if file_list:
        for f in file_list:
            yield base / Path(f)
    else:
        patterns = globs or ["**/*"]
        for pattern in patterns:
            for path in base.glob(pattern):
                if path.is_file():
                    yield path
    # TODO: Add .gitignore support

def dump_file(path: Union[str, Path], markdown: bool = False) -> str:
    """
    Return a string containing the file’s relative path, then its contents.
    If markdown=True, wrap contents in a language-marked code fence.
    """
    path = Path(path)
    rel_path = str(path)
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        content = f"<Error reading file: {e}>"
    if markdown:
        ext = path.suffix.lower()
        lang = EXT_LANG_MAP.get(ext, "")
        return f"### {rel_path}\n\n```{lang}\n{content}\n```\n"
    else:
        return f"# {rel_path}\n\n{content}\n"
