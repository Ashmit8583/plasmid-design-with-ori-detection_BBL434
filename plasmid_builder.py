import sys
from ori_finder import find_ori

def read_fasta(file):
    seq = ""
    with open(file) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip().upper()
    return seq

def read_design(file):
    mcs = []
    markers = []
    with open(file) as f:
        for line in f:
            if "," not in line:
                continue
            key, value = line.strip().split(",", 1)
            if "site" in key.lower():
                mcs.append(value.strip())
            else:
                markers.append(value.strip())
    return mcs, markers

def read_markers(file):
    db = {}
    with open(file) as f:
        for line in f:
            if line.strip():
                k, v = line.strip().split("\t")
                db[k] = v
    return db

RE_SITES = {
    "EcoRI": "GAATTC",
    "HindIII": "AAGCTT"
}

def build_plasmid(input_fa, design_txt, markers_tab, output_fa):
    genome = read_fasta(input_fa)

    # ORI detection from unknown organism
    ori = find_ori(genome)

    mcs, marker_list = read_design(design_txt)
    marker_db = read_markers(markers_tab)

    plasmid = ori

    # Add replication genes (default, paper-based)
    plasmid += "ATGAAAACGCTGATCGATCGATCGATCGATAG"

    # Add markers safely
    for marker in marker_list:
        if marker in marker_db:
            plasmid += marker_db[marker]

    # Remove restriction sites
    for enzyme in mcs:
        if enzyme in RE_SITES:
            plasmid = plasmid.replace(RE_SITES[enzyme], "")

    with open(output_fa, "w") as f:
        f.write(">Designed_Plasmid\n")
        for i in range(0, len(plasmid), 60):
            f.write(plasmid[i:i+60] + "\n")

if __name__ == "__main__":
    build_plasmid(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
