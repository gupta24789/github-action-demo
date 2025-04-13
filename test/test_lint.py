from subprocess import run, PIPE


def test_flake8():
    """Test that Python code follows PEP 8 style guide using flake8."""
    result = run(
        ['python', '-m', 'flake8',
         '--max-line-length=100',
         '--exclude=.git,__pycache__,venv'],
        stdout=PIPE,
        stderr=PIPE,
        text=True
    )

    assert result.returncode == 0, f"Code style issues found:\n{result.stdout}"
