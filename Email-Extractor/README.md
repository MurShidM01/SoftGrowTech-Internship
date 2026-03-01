# Email Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-1f6feb?style=for-the-badge&logo=python&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-Enabled-0ea5e9?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ea043?style=for-the-badge)

A Python utility that scans a text file and extracts email addresses into a clean output list. Built to practice file I/O, regex parsing, and structured outputs.

**Highlights**

- Reads input from a plain text file
- Extracts emails via a regex pattern
- Writes results to a single file, one email per line
- Creates the output directory automatically

**Tech**

- Python 3.8+

**Input and Output**

- Input file: `input/input_text.txt`
- Output file: `output/email.txt`

**Run**

1. Add or edit text in `input/input_text.txt`.
2. Run the script:

```bash
python email_extractor.py
```

**Notes**

- If the input file is missing, the script prints an error message and exits.
- The output directory is created automatically.

**Project Structure**

- `email_extractor.py` - Main extraction script
- `input/` - Folder for input text
- `output/` - Folder for extracted emails
