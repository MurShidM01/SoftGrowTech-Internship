import os
import re

input_file = "input/input_text.txt"
output_file = "output/email.txt"

if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    print("Email addresses extracted and saved to", output_file)
else:
<<<<<<< HEAD
    print("Input file not found.")
=======
    print("Input file not found.")
>>>>>>> 7582939aad547ee92a626311dea219072e5ed2c8
