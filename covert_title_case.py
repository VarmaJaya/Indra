# def format_name(f_name, l_name):
#     """Take first name and last name then format it to title case string and return the title case new name"""
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# # new_name = format_name("INDRA", "KIran")
# # print(new_name)
# new_name = format_name(f_name="indra", l_name="varma")
# print(new_name)
def transformSentence(sentence):
    words = sentence.split()
    transformed_words = []

    for word in words:
        transformed_word = word[0]  # Keep the first letter unchanged

        for i in range(1, len(word)):
            prev_char = word[i - 1]
            current_char = word[i]

            if prev_char.lower() < current_char.lower():
                transformed_word += current_char.upper()
            elif prev_char.lower() > current_char.lower():
                transformed_word += current_char.lower()
            else:
                transformed_word += current_char

        transformed_words.append(transformed_word)

    return ' '.join(transformed_words)

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()