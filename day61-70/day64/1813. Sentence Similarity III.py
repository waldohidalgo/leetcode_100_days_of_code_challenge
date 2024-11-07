class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        words1 = sentence1.split()
        words2 = sentence2.split()
        longest_common_prefix = []
        longest_common_suffix = []

        # Comparación de prefijos (desde el inicio)
        for i in range(min(len(words1), len(words2))):
            if words1[i] == words2[i]:
                longest_common_prefix.append(words1[i])
            else:
                break

        # Comparación de sufijos (desde el final)
        for i in range(1, min(len(words1), len(words2)) + 1):
            if words1[-i] == words2[-i]:
                longest_common_suffix.append(words1[-i])
            else:
                break

        total_common_words = len(longest_common_prefix) + len(longest_common_suffix)
        # caso 1: superposicion de prefijos y sufijos
        if total_common_words > min(len(words1), len(words2)):
            return True
        # caso 2: no existe superposicion de prefijos y sufijos y se cubren todas las palabras de la frase de largo menor
        if total_common_words == min(len(words1), len(words2)):
            return True
        # caso 3: no existe superposicion de prefijos y sufijos y no se cubren todas las palabras de la frase de largo menor
        return False
    
sol=Solution()
# ejemplo de caso 2
# sentence1 = "My name is Haley"
# sentence2 = "My Haley"

# ejemplo de caso 3
# sentence1 = "of"
# sentence2 = "A lot of words"

# ejemplo de caso 2
# sentence1 = "Eating right now"
# sentence2 = "Eating"

# sentence1 ="Luky"
# sentence2 ="Lucccky"
# sentence1 = "Are You Okay"
# sentence2 = "are you okay"

# ejemplo de caso 1
sentence1="A A AAa"
sentence2="A A AAa"
print(sol.areSentencesSimilar(sentence1,sentence2))


