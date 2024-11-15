'''
You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern. 

We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring. 
– Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
– “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
– “010” doesn’t match source[1..3] = "maz" 
– “010” matches source[2..4] = "azi" 
– “010” doesn’t match source[3..5] = "zin" 
– “010” doesn’t match source[4..6] = "ing"

So, there are 2 matches. For a visual demonstration, see the example video. 

For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
– There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

Guaranteed constraints:
1 ≤ source.length ≤ 103
1 ≤ pattern.length ≤ 103
This is a pattern-matching question where instances of a pattern need to be found inside of a larger array. It has the advantage of testing several fundamental programming skills at once: traversing multiple arrays with nested loops, working with subarrays, and performing basic collections/string operations.

Note that the guaranteed constraints in this question indicate that the candidate shouldn’t worry about optimizing their solution.
'''

pattern = ''    # 0s and 1s; 0s for vowels a e i o u y, 1s for consonants
source = ''     # lowercase letters except y

# Function that solves the problem.
def pattern_match(input_pattern, input_source):
    '''
    This function checks how many times a given pattern of vowels and consonants
    (input_pattern) appears in a source string (input_source)

    - input_pattern: 0s and 1s; 0s for vowels a e i o u y, 1s for consonants
    - input_source: lowercase letters except y

    For each position in source, the function checks if a substring matches the pattern
    If all characters match the pattern, result_count is incremented

    The function then prints the final count of matches
    '''

    # Declarar variables
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result_count = 0

    # Obtener largo de pattern
    # Recorrer source y comparar largo_pattern letras desde el indice
    # Si alguna no funciona, break. Si se llega al final correctamente, count + 1
    # Recorrer hasta largo source - largo pattern
    
    # Recorrer source
    for i in range(len(input_source) - len(input_pattern)):

        # Esta variable auxiliar va contando si el patron se recorre completo
        aux = 0

        # Recorrer patron
        for j in range(len(input_pattern)):

            # Comparar con vocales
            # Si cumple, aumentar variable auxiliar
            if input_pattern[j] == '0':
                if input_source[i + j] in vowels:
                    aux = aux + 1
            
            # Comparar con consonantes
            # Si cumple, aumentar variable auxiliar
            if input_pattern[j] == '1':
                if input_source[i + j] not in vowels:
                    aux = aux + 1

            # Si se recorrio todo el patron, aumentar variable final result_count
            if j == (len(input_pattern) - 1):
                if aux == len(input_pattern):
                    result_count = result_count + 1
    
    # Imprimir resultados
    print(result_count)

# Ejemplo de uso
pattern = '101'
source = 'otorrinolaringologo'
pattern_match(pattern, source)