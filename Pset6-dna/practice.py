import csv
from sys import argv


def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Usage: dna.py databases/large.csv sequences/5.txt")
        exit(1)

    # TODO: Read database file into a variable
    STR = []
    with open(argv[1], 'r') as f:
        db = list(csv.reader(f))
        # create list without name column
        for j in db:
           STR.append(j[1:])
        # list of check subesequences
        subsequences = STR[0]

    # TODO: Read DNA sequence file into a variable
    with open(argv[2], 'r') as f:
        dna = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    # store in results dictionary
    result = {}
    # iterate over STR[0]
    for i in subsequences:
        result[i] = longest_match(dna, i)
    print(db)
    # TODO: Check database for matching profiles
    
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
