# Barcode and QR Code Generator

A tool to generate datasets of QR codes, EAN13 barcodes, and DataMatrix codes with random content and optional visual effects like noise, blur, and dust. Supports CLI and direct Python usage.

---
![image](https://github.com/user-attachments/assets/3c729553-a37d-4012-a551-be74defc4b76) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
![image](https://github.com/user-attachments/assets/cd63c194-d163-4d34-aca8-8f8ab9340f90) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
![image](https://github.com/user-attachments/assets/089676dd-c9c4-4615-844f-e9678c044487)





## Quick Start

### Run Directly via Python
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python3 main.py --hash_length 16 --dir_name "my_codes" --file_format "png" --files_count 5 --code_type "qr"
   ```
### Use as a CLI Tool
1. Install via install.sh:
   ```bash
   python3 main.py --hash_length 16 --dir_name "my_codes" --file_format "png" --files_count 5 --code_type "qr"
   ```
2. Generate codes with the c-gen command:
   ```bash
   c-gen --hash_length 16 --dir_name "my_codes" --file_format "png" --files_count 5 --code_type "ean13"
   ```

### Parametrs
| Parameter         | Description                                            | Default       |
|-------------------|--------------------------------------------------------|---------------|
| `--hash_length`   | Length of the random hash (only for QR/DataMatrix).    | `16`          |
| `--dir_name`      | Directory to save the generated files.                 | `"qr_codes"`  |
| `--file_format`   | Output file format (`jpeg`, `png`).                    | `"jpeg"`      |
| `--files_count`   | Number of files to generate.                           | `3`           |
| `--code_type`     | Type of code (`qr`, `ean13`, `datamatrix`).            | `"qr"`        |


### Project structure
```bash
├── effect_generators.py        # Functions for visual effects
├── code_generators.py          # Barcode/QR code generation
├── dataset_generator.py        # Random data generation
├── main.py                     # CLI implementation
├── install.sh                  # Installer script
```
