GSE Data
========

The format of the JSON file is as follows

```
[
	{
		"gse": name of GSE
		"file": name of file
		"type": file type: {csv,tsv}:{lf:crlf:cr} or xlsx:sheet
		"gene": column where gene name is
		"standard": {
			"A": [columns with adults]
			"L4": [columns with L4]
			"D": [columns with dauer]
			"L3": [columns with L3]
			"L2": [columns with L2]
			"L1": [columns with L1]
			"E": [columns with embryos]
			"other": [columns with tissues, mixtures, and unknowns]
		},
		"experiment": {
			"arbitrary-tag1": [columns that group these]
			"arbitrary-tag2": [columns that group these]
		},
		"notes": [
			comments about the set
		]
	}
]
```