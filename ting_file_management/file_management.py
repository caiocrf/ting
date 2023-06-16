import sys
import os


def txt_importer(path_file):
    file_extension = os.path.splitext(path_file)[1]

    if not os.path.exists(path_file):
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []

    if file_extension != ".txt":
        sys.stderr.write("Formato inválido\n")
        return []

    with open(path_file, "r") as file:
        lines = file.read().split("\n")

    return lines
