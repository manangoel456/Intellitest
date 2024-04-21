# Open the original text file in read mode
with open('original.txt', 'r') as text_file:
    # Read the string from the file
    my_string = text_file.read()
    a = 0
    extracted_text = []

    while a < 5:
        try:
            # Extract the text from the string
            extracted_text1 = my_string[my_string.find("Q"+str(a+1)):my_string.find(";", my_string.find("Q"+str(a+1))) + 1]
            extracted_text2 = my_string[my_string.find("(1)"):my_string.find("(2)", my_string.find("(1)"))]
            extracted_text3 = my_string[my_string.find("(2)"):my_string.find("(3)", my_string.find("(2)"))]
            extracted_text4 = my_string[my_string.find("(3)"):my_string.find("(4)", my_string.find("(3)"))]
            extracted_text5 = my_string[my_string.find("(4)"):my_string.find("Ans.", my_string.find("(4)"))]
            extracted_text6 = my_string[my_string.find("Ans. (")+6:my_string.find(")", my_string.find("Ans. ("))]

            extracted_text.append( extracted_text1+","+extracted_text2+","+extracted_text3+","+extracted_text4+","+extracted_text5+","+extracted_text6+"\n")
            a += 1

            part_to_remove = extracted_text1
            index = my_string.find(part_to_remove)  # Find the index of the part you want to remove
            if index != -1:
                my_string = my_string[:index] + my_string[index + len(part_to_remove):]

            part_to_remove = extracted_text2
            index = my_string.find(part_to_remove)  # Find the index of the part you want to remove
            if index != -1:
                my_string = my_string[:index] + my_string[index + len(part_to_remove):]

            part_to_remove = extracted_text3
            index = my_string.find(part_to_remove)  # Find the index of the part you want to remove
            if index != -1:
                my_string = my_string[:index] + my_string[index + len(part_to_remove):]
            part_to_remove = extracted_text4
            index = my_string.find(part_to_remove)  # Find the index of the part you want to remove
            if index != -1:
                my_string = my_string[:index] + my_string[index + len(part_to_remove):]
            part_to_remove = extracted_text5
            index = my_string.find(part_to_remove)  # Find the index of the part you want to remove
            if index != -1:
                my_string = my_string[:index] + my_string[index + len(part_to_remove):]
            part_to_remove = extracted_text6
            index = my_string.find(part_to_remove)  # Find the index of the part you want to remove
            if index != -1:
                my_string = my_string[:index] + my_string[index + len(part_to_remove):]

        except ValueError:
            print(f"Error extracting text at index {a}. Skipping to next iteration.")
            a += 1
            continue

# Open the new text file in write mode
with open('new.txt', 'w') as new_file:
    # Write the extracted text to the new file
    for text in extracted_text:
        new_file.write(text)





