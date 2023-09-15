import subprocess

input_file = "2_intro_to_flask/readme.md"
output_file = "README.docx"


subprocess.run(["pandoc", input_file, "-o", output_file])
print(f"Successfully converted {input_file} to {output_file}.")
