def replace_selected_chars(sentence, chars_to_replace):
    """
    Replaces specified characters in the sentence with '$'.

    Parameters:
    - sentence (str): The input sentence.
    - chars_to_replace (str): A string containing characters to be replaced.

    Returns:
    - str: The modified sentence with selected characters replaced by '$'.
    """
    translation_table = str.maketrans({char: '$' for char in chars_to_replace})

    return sentence.translate(translation_table)

sentence = input("Enter a sentence: ")
chars_to_replace = input("Enter characters to replace with '$': ")

modified_sentence = replace_selected_chars(sentence, chars_to_replace)
print("Modified sentence:", modified_sentence)
