input_file = "notes.txt"
output_file = "clean_notes.txt"

try:
    with open(input_file, "r") as source, open(output_file, "w") as target:
        for line in source:
            if line.startswith("IMPORTANT") or line.startswith("TODO"):
                target.write(line)
    print("Clean notes have been successfully saved!")
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found. Please make sure it exists.")