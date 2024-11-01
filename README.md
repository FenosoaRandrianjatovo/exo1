# FASTQ to FASTA Converter

Ce script Python permet de convertir des fichiers au format FASTQ en fichiers FASTA, en séparant également les scores de qualité dans un fichier dédié.

## Prérequis

- Python 3.9
- Modules intégrés : `argparse`, `os`, `sys`

## Installation

Téléchargez le script dans le dossier de votre choix.
```bash
git clone https://github.com/FenosoaRandrianjatovo/exo1.git
```

## Utilisation

Exécutez le script depuis le terminal avec les options disponibles :

```bash
python main_convertir.py -n "Toto_R1.fastq" -of " my_output.fasta" -oq "my_qual.qual" 

