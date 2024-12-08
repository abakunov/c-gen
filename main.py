#!/usr/bin/env python3

import argparse
import os
from effect_generators import apply_random_effects
from code_generators import generate_QR, generate_EAN13, generate_DataMatrix
from dataset_generator import generate_random_hash, generate_codes


def main():
    """CLI for generating a dataset of codes."""
    parser = argparse.ArgumentParser(description="Generate a dataset of codes with effects.")
    parser.add_argument("--hash_length", type=int, default=16, help="Length of the random hash (default: 16).")
    parser.add_argument("--dir_name", type=str, default="qr_codes", help="Directory name for saving files.")
    parser.add_argument("--file_format", type=str, default="jpeg", help="File format (jpeg, png).")
    parser.add_argument("--files_count", type=int, default=3, help="Number of files to generate.")
    parser.add_argument("--code_type", type=str, default="qr", choices=["qr", "ean13", "datamatrix"],
                        help="Type of code (qr, ean13, datamatrix).")

    args = parser.parse_args()

    generate_codes(
        hash_length=args.hash_length,
        dir_name=args.dir_name,
        file_format=args.file_format,
        files_count=args.files_count,
        code_type=args.code_type
    )


if __name__ == "__main__":
    main()
