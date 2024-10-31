# FASTQ to FASTA Converter

Ce script Python permet de convertir des fichiers au format FASTQ en fichiers FASTA, en séparant également les scores de qualité dans un fichier dédié.

## Prérequis

- Python 3.9
- Modules intégrés : `argparse`, `os`, `sys`

## Installation

Téléchargez le script dans le dossier de votre choix.

## Utilisation

Exécutez le script depuis le terminal avec les options disponibles :

```bash
python main.py -n "Toto_R1.fastq" -of " my_output.fasta" -oq "my_qual.qual" 

