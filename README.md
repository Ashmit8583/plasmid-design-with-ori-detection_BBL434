This coding assignmnet designs a plasmid that works in an unknown organism by first
detecting the organism-specific origin of replication using GC skew analysis.

The detected ORI is used as the replication backbone, ensuring host compatibility.
Replication genes are added by default as required by the referenced paper.

The plasmid is modified using a user-provided Design.txt file and selectable
markers are incorporated from markers.tab. Missing markers are handled safely.

Testing is performed using pUC19.fa and Design_pUC19.txt, confirming removal
of the EcoRI restriction site from the final plasmid.
