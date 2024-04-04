# Open the original text file in read mode
with open('original.txt', 'r') as text_file:
    # Read the string from the file
    my_string = text_file.read()
    a = 0
    extracted_text = []

    while a < 5:
        try:
            # Extract the text from the string
            extracted_text1 = my_string[my_string.find("Q"+str(a)):my_string.find(":", my_string.find("Q"+str(a))) + 1]
            extracted_text2 = my_string[my_string.find("(1)"):my_string.find("(2)", my_string.find("(1)"))]
            extracted_text3 = my_string[my_string.find("(2)"):my_string.find("(3)", my_string.find("(2)"))]
            extracted_text4 = my_string[my_string.find("(3)"):my_string.find("(4)", my_string.find("(3)"))]
            extracted_text5 = my_string[my_string.find("(4)"):my_string.find("Ans.", my_string.find("(4)"))]
            extracted_text6 = my_string[my_string.find("Ans.("):my_string.find(")", my_string.find("Ans.("))]

            extracted_text.append( extracted_text1+","+extracted_text2+","+extracted_text3+","+extracted_text4+","+extracted_text5+","+extracted_text6)
            a += 1
        except ValueError:
            print(f"Error extracting text at index {a}. Skipping to next iteration.")
            a += 1
            continue

# Open the new text file in write mode
with open('new.txt', 'w') as new_file:
    # Write the extracted text to the new file
    for text in extracted_text:
        new_file.write(text)

# Open the original text file in write mode
with open('original_modified.txt', 'w') as modified_file:
    # Write the remaining text to the original_modified file
    modified_file.write(my_string[:my_string.find("Q")])

# Remove the extracted text from the original file
with open('original.txt', 'w') as original_file:
    original_file.write('')
    
# Open the original_modified file in read mode
with open('original_modified.txt', 'r') as modified_file:
    # Read the remaining text from the file
    remaining_text = modified_file.read()

# Overwrite the contents of original.txt with the contents of original_modified.txt
with open('original.txt', 'w') as original_file:
    original_file.write(remaining_text)