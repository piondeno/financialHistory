import subprocess
import sys
import tempfile
from pathlib import Path

import verify_chapter as vc

SCRIPT = Path(__file__).resolve().parent / "verify_chapter.py"

SECTIONS = ["本章摘要", "歷史背景", "投機的興起", "頂點與轉折", "崩潰與危機",
            "後續與制度變革", "深度分析", "評判與評斷", "關鍵數據表"]


def heading_block(names=None):
    names = names or SECTIONS
    return "\n\n".join(f"## {i}. {n}" for i, n in enumerate(names, 1))


def run_cli(*paths):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, paths)],
        capture_output=True, text=True)


def test_count_chars_ignores_whitespace():
    assert vc.count_chars("ab cd\nef\tgh\n") == 8


def test_count_chars_counts_cjk_punct_digits():
    assert vc.count_chars("金融，投機。123abc") == 12


def test_missing_sections_complete():
    assert vc.missing_sections(heading_block()) == []


def test_missing_sections_finds_one():
    names = [n for n in SECTIONS if n != "深度分析"]
    assert vc.missing_sections(heading_block(names)) == ["深度分析"]


def test_chain_ok():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d)
        (p / "ch01-1837-1847-a.md").write_text("x")
        (p / "ch02-1847-1857-b.md").write_text("x")
        assert vc.check_chain(p) == []


def test_chain_broken():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d)
        (p / "ch01-1837-1847-a.md").write_text("x")
        (p / "ch02-1850-1857-b.md").write_text("x")
        errs = vc.check_chain(p)
        assert any("ch01" in e and "ch02" in e for e in errs)


def test_chain_chapter_number_gap():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d)
        (p / "ch01-1837-1847-a.md").write_text("x")
        (p / "ch03-1847-1857-b.md").write_text("x")
        errs = vc.check_chain(p)
        assert any("ch02" in e and "ch03" in e for e in errs)


def test_chain_first_must_start_1837():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d)
        (p / "ch01-1840-1847-a.md").write_text("x")
        assert any("1837" in e for e in vc.check_chain(p))


def test_chain_last_must_end_2026():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d)
        (p / "ch20-2022-2025-a.md").write_text("x")
        assert any("2026" in e for e in vc.check_chain(p))


def test_cli_pass(tmp_path):
    ch = tmp_path / "chapters"
    ch.mkdir()
    f = ch / "ch01-1837-1847-測試.md"
    f.write_text(f"# 第一章 測試（1837–1847）\n\n{heading_block()}\n\n{'測' * 20001}\n",
                 encoding="utf-8")
    r = run_cli(f)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "PASS" in r.stdout


def test_cli_too_short_fails(tmp_path):
    ch = tmp_path / "chapters"
    ch.mkdir()
    f = ch / "ch01-1837-1847-測試.md"
    f.write_text(f"# 第一章 測試（1837–1847）\n\n{heading_block()}\n\n太短\n",
                 encoding="utf-8")
    r = run_cli(f)
    assert r.returncode == 1
    assert "FAIL" in r.stdout


def test_cli_missing_section_fails(tmp_path):
    ch = tmp_path / "chapters"
    ch.mkdir()
    f = ch / "ch01-1837-1847-測試.md"
    names = [n for n in SECTIONS if n != "崩潰與危機"]
    f.write_text(f"# 第一章 測試（1837–1847）\n\n{heading_block(names)}\n\n{'測' * 20001}\n",
                 encoding="utf-8")
    r = run_cli(f)
    assert r.returncode == 1
    assert "崩潰與危機" in r.stdout


def test_cli_no_args_exit_2():
    r = run_cli()
    assert r.returncode == 2


def test_cli_nonexistent_file_exit_1():
    r = run_cli("/nonexistent-verify-chapter-test.md")
    assert r.returncode == 1
    assert "檔案不存在" in r.stdout
