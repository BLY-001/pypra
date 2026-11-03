# Challenge #3
# Create a Python script that removes all empty lines including those that contain only spaces from a file.
# Click to download a sample text file.

with open("chll2.txt", 'r') as f:
    content = [line.strip() for line in f if line.strip()]