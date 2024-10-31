# Importation des modules nécessaires
import sys
import os
import argparse

# Ouverture du fichier FASTQ en mode lecture
def main(name, out_fasta, out_fasta_qual, folder_path):
    
    try:
        # exist_ok=True pour eviter l'erreur si le  folder existe
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder_path}' created successfully or already exists.")
    except OSError as e:
        print(f"Error creating folder '{folder_path}': {e}")
    try:
        fastq_in = open(name, "r")
    except IOError:
        sys.exit("Could not open input file!")

    # Ouverture des fichiers de sortie FASTA pour l'ADN et pour les scores de qualité
    try:
        # fasta_out = open(folder_path/out_fasta, "w")
        fasta_out = open(os.path.join(folder_path, out_fasta), "w")
        fasta_qual = open(os.path.join(folder_path,out_fasta_qual), "w")
    except IOError:
        sys.exit("Could not open output file!")

    # Dictionnaire de correspondance pour les scores de qualité
    quality_mapping = {
    '!': '0', '"': '1', '#': '2', '$': '3', '%': '4', '&': '5', "'": '6', '(': '7', ')': '8', '*': '9',
    '+': '10', ',': '11', '-': '12', '.': '13', '/': '14', '0': '15', '1': '16', '2': '17', '3': '18',
    '4': '19', '5': '20', '6': '21', '7': '22', '8': '23', '9': '24', ':': '25', ';': '26', '<': '27',
    '=': '28', '>': '29', '?': '30', '@': '31', 'A': '32', 'B': '33', 'C': '34', 'D': '35', 'E': '36',
    'F': '37', 'G': '38', 'H': '39', 'I': '40', 'J': '41'
    }

    # Lecture du fichier FASTQ ligne par ligne
    for line in fastq_in:
        line = line.strip()
          # Supprime le caractère de fin de ligne

        # Vérifie si la ligne commence par "@", indiquant un identifiant de séquence
        if line.startswith("@"):
            # Remplace le "@" par ">" pour correspondre au format FASTA
            fasta_out.write(">" + line[1:] + "\n")
            fasta_qual.write(">" + line[1:] + "\n")

            # Lecture de la séquence d'ADN sur la ligne suivante
            sequence = fastq_in.readline().strip()
            fasta_out.write(sequence + "\n")  # Écriture de la séquence dans le fichier FASTA

            # Ignore la ligne "+" suivante (l. 3) dans le fichier FASTQ
            fastq_in.readline()

            # Lecture de la ligne de scores de qualité (l. 4)
            quality_line = fastq_in.readline().strip()

            # Conversion des caractères de qualité en scores numériques
            quality_scores = [quality_mapping[char] for char in quality_line]
            
            # Écriture des scores de qualité convertis dans le fichier de sortie
            fasta_qual.write(" ".join(quality_scores) + "\n")

    # Fermeture des fichiers d'entrée et de sortie
    fastq_in.close()
    fasta_out.close()
    fasta_qual.close()

    # Affichage d'un message de confirmation
    print("Conversion to FASTA format completed successfully.")



if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Convert FASTQ to FASTA format.")
    parser.add_argument("-n", "--name", type=str, default="Toto_R1.fastq", help="Input FASTQ file name")
    parser.add_argument("-of", "--out_fasta", type=str, default="fasta_convertie.fasta", help="Output FASTA file name")
    parser.add_argument("-oq", "--out_fasta_qual", type=str, default="fast_qual_convertie.qual", help="Output FASTA quality scores file")
    parser.add_argument("-fp", "--folder_path", type=str, default="Folder_output", help="Output folder path")

   

    # Parse arguments
    args = parser.parse_args()
    
    # Call the main function with parsed arguments
    main(args.name, args.out_fasta, args.out_fasta_qual, args.folder_path)


