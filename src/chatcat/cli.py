import click
from pathlib import Path
from .core import iter_files, dump_file

@click.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, dir_okay=True), default=".")
@click.option("--only", "-o", multiple=True, help="Glob pattern(s) to select files.")
@click.option("--file-list", "-f", type=click.Path(exists=True, dir_okay=False), help="Path to a text file listing files to dump, one per line.")
@click.option("--out", "-O", type=click.Path(dir_okay=False), help="Write output to the given file.")
@click.option("--markdown/--no-markdown", default=True, help="Wrap contents in markdown code fences.")
def main(directory, only, file_list, out, markdown):
    """Dump codebase files into LLM/chat-friendly text or markdown format."""
    base = Path(directory)
    files = None
    if file_list:
        with open(file_list, "r", encoding="utf-8", errors="ignore") as f:
            files = [line.strip() for line in f if line.strip()]
    output = []
    for path in iter_files(base, globs=list(only) if only else None, file_list=files):
        output.append(dump_file(path, markdown=markdown))
    result = "\n".join(output)
    if out:
        with open(out, "w", encoding="utf-8", errors="ignore") as f:
            f.write(result)
    else:
        click.echo(result)

if __name__ == "__main__":
    main()
