import numpy as np
from PIL import Image
import os

class OneTimePad:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
    def generate_key(self, length: int) -> list:
        """Génère une clé aléatoire de la longueur spécifiée"""
        return [np.random.randint(0, 26) for _ in range(length)]
    
    def generate_key_image(self, width: int, height: int, channels: int = 3) -> np.ndarray:
        """Génère une clé aléatoire pour une image"""
        return np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
    
    def text_to_numbers(self, text: str) -> list:
        """Convertit le texte en nombres (positions dans l'alphabet)"""
        text = text.lower().replace(' ', '')
        return [self.alphabet.index(char) for char in text if char in self.alphabet]
    
    def numbers_to_text(self, numbers: list) -> str:
        """Convertit les nombres en texte"""
        return ''.join(self.alphabet[n % 26] for n in numbers)
    
    def encrypt_text(self, plaintext: str, key: list = None) -> tuple:
        """
        Chiffre un texte avec un One-Time Pad
        Retourne le texte chiffré et la clé utilisée
        """
        numbers = self.text_to_numbers(plaintext)
        if key is None:
            key = self.generate_key(len(numbers))
        
        # Chiffrement par addition modulo 26
        ciphertext_numbers = [(n + k) % 26 for n, k in zip(numbers, key)]
        return self.numbers_to_text(ciphertext_numbers), key
    
    def decrypt_text(self, ciphertext: str, key: list) -> str:
        """Déchiffre un texte avec un One-Time Pad"""
        numbers = self.text_to_numbers(ciphertext)
        
        # Déchiffrement par soustraction modulo 26
        plaintext_numbers = [(n - k) % 26 for n, k in zip(numbers, key)]
        return self.numbers_to_text(plaintext_numbers)
    
    def encrypt_image(self, image_path: str, output_path: str = None) -> tuple:
        """
        Chiffre une image avec un One-Time Pad
        Retourne le chemin de l'image chiffrée et la clé
        """
        # Charger l'image
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Générer une clé de la même taille que l'image
        key = self.generate_key_image(img_array.shape[1], img_array.shape[0], 
                                    img_array.shape[2] if len(img_array.shape) > 2 else 1)
        
        # Chiffrement par XOR
        encrypted_array = np.bitwise_xor(img_array, key)
        
        # Sauvegarder l'image chiffrée
        if output_path is None:
            base, ext = os.path.splitext(image_path)
            output_path = f"{base}_encrypted{ext}"
            
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(output_path)
        
        return output_path, key
    
    def decrypt_image(self, encrypted_image_path: str, key: np.ndarray, output_path: str = None) -> str:
        """Déchiffre une image avec un One-Time Pad"""
        # Charger l'image chiffrée
        img = Image.open(encrypted_image_path)
        img_array = np.array(img)
        
        # Déchiffrement par XOR
        decrypted_array = np.bitwise_xor(img_array, key)
        
        # Sauvegarder l'image déchiffrée
        if output_path is None:
            base, ext = os.path.splitext(encrypted_image_path)
            output_path = f"{base}_decrypted{ext}"
            
        decrypted_image = Image.fromarray(decrypted_array)
        decrypted_image.save(output_path)
        
        return output_path

# Test de la classe OneTimePad
if __name__ == "__main__":
    otp = OneTimePad()
    
    # Test avec du texte
    message = "secretmessage"
    encrypted, key = otp.encrypt_text(message)
    decrypted = otp.decrypt_text(encrypted, key)
    
    print(f"Message original: {message}")
    print(f"Message chiffré: {encrypted}")
    print(f"Message déchiffré: {decrypted}")
    
    # Test avec une image
    # Assurez-vous d'avoir une image test.jpg dans le répertoire
    try:
        encrypted_path, img_key = otp.encrypt_image("test.jpg")
        decrypted_path = otp.decrypt_image(encrypted_path, img_key)
        print(f"\nImage chiffrée sauvegardée: {encrypted_path}")
        print(f"Image déchiffrée sauvegardée: {decrypted_path}")
    except FileNotFoundError:
        print("\nPas d'image test.jpg trouvée pour le test")