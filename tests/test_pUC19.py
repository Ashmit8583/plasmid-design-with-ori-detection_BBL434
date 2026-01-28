import subprocess

def test_ecori_removed():
    subprocess.run([
        "python",
        "plasmid_builder.py",
        "tests/pUC19.fa",
        "tests/Design_pUC19.txt",
        "markers.tab",
        "Output.fa"
    ], check=True)

    with open("Output.fa") as f:
        assert "GAATTC" not in f.read()
