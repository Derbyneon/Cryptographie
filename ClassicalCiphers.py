class ClassicalCiphers:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
    def caesar_encrypt(self, text: str, shift: int) -> str:
        """Chiffrement de César"""
        result = ''
        # Normalisation du décalage pour rester dans l'alphabet
        shift = shift % 26
        # Conversion en minuscules et suppression des espaces
        text = text.lower().replace(' ', '')
        
        for char in text:
            if char in self.alphabet:
                # Trouve la position de la lettre dans l'alphabet
                position = self.alphabet.find(char)
                # Applique le décalage
                new_position = (position + shift) % 26
                # Ajoute la nouvelle lettre au résultat
                result += self.alphabet[new_position]
            else:
                result += char
                
        return result
    
    def caesar_decrypt(self, text: str, shift: int) -> str:
        """Déchiffrement de César"""
        # Le déchiffrement est un chiffrement avec un décalage opposé
        return self.caesar_encrypt(text, -shift)
    
    def caesar_crack(self, text: str) -> list:
        """Tentative de cassage du chiffrement de César"""
        all_possibilities = []
        # Essaie tous les décalages possibles
        for shift in range(26):
            decrypted = self.caesar_decrypt(text, shift)
            all_possibilities.append((shift, decrypted))
        return all_possibilities
    
    def vigenere_encrypt(self, text: str, key: str) -> str:
        """Chiffrement de Vigenère"""
        result = ''
        # Préparation du texte et de la clé
        text = text.lower().replace(' ', '')
        key = key.lower().replace(' ', '')
        key_length = len(key)
        
        for i, char in enumerate(text):
            if char in self.alphabet:
                # Calcul du décalage basé sur la lettre de la clé
                key_char = key[i % key_length]
                shift = self.alphabet.find(key_char)
                # Position de la lettre actuelle
                text_char_pos = self.alphabet.find(char)
                # Nouvelle position après application du décalage
                new_position = (text_char_pos + shift) % 26
                result += self.alphabet[new_position]
            else:
                result += char
                
        return result
    
    def vigenere_decrypt(self, text: str, key: str) -> str:
        """Déchiffrement de Vigenère"""
        result = ''
        # Préparation du texte et de la clé
        text = text.lower().replace(' ', '')
        key = key.lower().replace(' ', '')
        key_length = len(key)
        
        for i, char in enumerate(text):
            if char in self.alphabet:
                # Calcul du décalage inverse basé sur la lettre de la clé
                key_char = key[i % key_length]
                shift = self.alphabet.find(key_char)
                # Position de la lettre actuelle
                text_char_pos = self.alphabet.find(char)
                # Nouvelle position après application du décalage inverse
                new_position = (text_char_pos - shift) % 26
                result += self.alphabet[new_position]
            else:
                result += char
                
        return result

# Test des chiffrements
if __name__ == "__main__":
    cipher = ClassicalCiphers()
    
    # Test du chiffrement de César
    message = "meetmeatdawn"
    shift = 3
    encrypted = cipher.caesar_encrypt(message, shift)
    decrypted = cipher.caesar_decrypt(encrypted, shift)
    
    print(f"Message original: {message}")
    print(f"Message chiffré (César): {encrypted}")
    print(f"Message déchiffré: {decrypted}")
    
    # Test du chiffrement de Vigenère
    key = "lemon"
    vig_encrypted = cipher.vigenere_encrypt(message, key)
    vig_decrypted = cipher.vigenere_decrypt(vig_encrypted, key)
    
    print(f"\nMessage chiffré (Vigenère): {vig_encrypted}")
    print(f"Message déchiffré: {vig_decrypted}")