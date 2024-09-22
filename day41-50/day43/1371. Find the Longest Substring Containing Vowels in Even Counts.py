class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        bitmask = 0

        first_occurrence = {0: -1}
        max_length = 0
        
        for i, char in enumerate(s):
            if char in vowels:
                bitmask ^= (1 << vowels[char])
            
            if bitmask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                first_occurrence[bitmask] = i
        
        return max_length
sol=Solution()
s = "bcbcbc"

print(sol.findTheLongestSubstring(s))


# se almacenan en una bitmask las posiciones de las vocales y si ha aparecido entonces se activa el bit correspondiente, si vuelve la misma vocal se desactiva el bit correspondiente. Esto genera que cada vez que se repita una bitmask significa que las vocales han aparecido un numero par de veces para aquellas distintas del bitmask correspondiente. Almacenando el indice para los bitmask que no han sido considerados en un diccionario entonces se puede saber la longitud de la cadena de caracteres en la cual las vocales aparecen un numero par de veces.