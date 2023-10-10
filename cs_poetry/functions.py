def nearest_value(values: set[int], one: int) -> int:
    closest_value = None
    min_distance = float('inf')

    for value in values:
        distance = abs(value - one)
        if distance < min_distance or (distance == min_distance and value < closest_value):
            closest_value = value
            min_distance = distance

    return closest_value

def first_word(text: str) -> str:
    # Diviser la chaîne de caractères en utilisant l'espace comme séparateur
    words = text.split()
    
    # Le premier mot est le premier élément de la liste 'words'
    if words:
        return words[0]
    
    # Si la liste 'words' est vide retourner une chaîne vide
    return ""

def split_pairs(text: str):
    if len(text) % 2 == 1:
        # If it's odd, add an underscore to make it even
        text += "_"
    
    # Generator to yield pairs
    for i in range(0, len(text), 2):
        yield text[i:i+2]

def correct_sentence(text: str) -> str:
    # Check if the sentence starts with a capital letter
    if not text[0].isupper():
        text = text[0].upper() + text[1:]
    
    # Check if the sentence ends with a period
    if not text.endswith('.'):
        text += '.'

    return text

def beginning_zeros(a: str) -> int:
    count = 0
    for digit in a:
        if digit == '0':
            count += 1
        else:
            break
    return count

def between_markers(text: str, start: str, end: str) -> str:
    # Find the position of the initial marker
    start_index = text.find(start)
    
    # Find the position of the final marker
    end_index = text.rfind(end)
    
    # Check if both markers exist in the string
    if start_index != -1 and end_index != -1:
        # Extract the substring between the markers
        return text[start_index + 1:end_index]
    
    # If either marker is not found, return an empty string
    return ""


def checkio(data: list[int]):
    element_count = {}
    
    non_unique_elements = []
    
    for element in data:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    for element in data:
        if element_count[element] > 1:
            non_unique_elements.append(element)
    
    return non_unique_elements

def backward_string_by_word(text: str) -> str:
    # Split the input string into words using spaces as a delimiter
    words = text.split(' ')
    
    # Reverse each word and store them in a list
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back together with spaces between them
    reversed_text = ' '.join(reversed_words)
    
    return reversed_text
