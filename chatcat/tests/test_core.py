import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from chatcat.core import iter_files, dump_file

def test_iter_files_with_file_list(tmp_path):
    f1 = tmp_path / "a.py"
    f2 = tmp_path / "b.txt"
    f1.write_text("print('hi')")
    f2.write_text("hello")
    files = list(iter_files(tmp_path, file_list=["a.py", "b.txt"]))
    assert set(f.name for f in files) == {"a.py", "b.txt"}

def test_iter_files_with_globs(tmp_path):
    (tmp_path / "foo.py").write_text("print('foo')")
    (tmp_path / "bar.md").write_text("# bar")
    files = list(iter_files(tmp_path, globs=["*.py", "*.md"]))
    assert set(f.suffix for f in files) == {".py", ".md"}

def test_dump_file_plain(tmp_path):
    f = tmp_path / "x.py"
    f.write_text("print('x')")
    out = dump_file(f, markdown=False)
    assert f"# {f}" in out
    assert "print('x')" in out

def test_dump_file_markdown(tmp_path):
    f = tmp_path / "y.py"
    f.write_text("print('y')")
    out = dump_file(f, markdown=True)
    assert f"```python" in out
    assert "print('y')" in out
