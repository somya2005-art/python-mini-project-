class DNA:
    def _init_(self, sequence):
        """Initialize the DNA object with a sequence."""
        self.sequence = sequence.upper()  # Ensure the sequence is in uppercase

    def _repr_(self):
        """Return a string representation of the DNA object."""
        return 'DNA(sequence="' + self.sequence + '")'

    def compare(self, other_dna):
        """Compare this DNA sequence with another and return the Hamming distance."""
        if len(self.sequence) != len(other_dna.sequence):
            print("DNA sequences must be of the same length to compare.")
            return None
        
        hamming_distance = 0
        for i in range(len(self.sequence)):
            if self.sequence[i] != other_dna.sequence[i]:
                hamming_distance += 1
        
        return hamming_distance

    def transcribe(self):
        """Transcribe the DNA sequence to RNA (replace 'T' with 'U')."""
        return self.sequence.replace('T', 'U')

    def _len_(self):
        """Return the length of the DNA sequence."""
        return len(self.sequence)

    def is_valid(self):
        """Check if the DNA sequence is valid (only contains A, T, C, G)."""
        valid_bases = {'A', 'T', 'C', 'G'}
        for base in self.sequence:
            if base not in valid_bases:
                return False
        return True

# Function to take DNA sequence input from the user
def get_dna_input(prompt="Enter a DNA sequence: "):
    while True:
        dna_sequence = input(prompt).strip().upper()  # Get input and ensure it's uppercase
        is_valid = True
        for base in dna_sequence:
            if base not in {'A', 'T', 'C', 'G'}:
                is_valid = False
                break
        if is_valid:
            return dna_sequence
        else:
            print("Invalid sequence. Please enter a DNA sequence containing only A, T, C, G.")

# Main function to run the project
def main():
    # Take DNA sequences as input
    print("Enter the first DNA sequence:")
    dna1_sequence = get_dna_input()
    dna1 = DNA(dna1_sequence)

    print("Enter the second DNA sequence:")
    dna2_sequence = get_dna_input()
    dna2 = DNA(dna2_sequence)

    # Check if the sequences are of the same length
    if len(dna1) != len(dna2):
        print("DNA sequences must be of the same length to compare.")
        return

    # Compare DNA sequences (Hamming distance)
    distance = dna1.compare(dna2)
    if distance is not None:
        print("Hamming distance between the two DNA sequences: " + str(distance))

    # Transcribe the first DNA sequence to RNA
    rna = dna1.transcribe()
    print("RNA transcription of the first DNA sequence: " + rna)


if __name__ == "__main__":
    main()   