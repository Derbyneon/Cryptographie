# Introduction aux Chiffrements Classiques

Les chiffrements classiques sont les premières méthodes de cryptographie développées dans l'histoire. Ils se divisent principalement en deux catégories :

- **Chiffrements par substitution** : chaque lettre est remplacée par une autre.
- **Chiffrements par transposition** : l'ordre des lettres est modifié.

## Le Chiffrement de César

Le chiffrement de César, nommé d'après Jules César, est l'un des plus simples et des plus anciens. Son principe est :

- Chaque lettre est décalée d'un nombre fixe de positions dans l'alphabet.
- Par exemple, avec un décalage de 3 : `A → D`, `B → E`, etc.
- Le déchiffrement s'effectue en appliquant le décalage inverse.

### Implémentation

Dans notre implémentation, nous avons les fonctions suivantes :

- **`caesar_encrypt()`** : prend un texte et un décalage en paramètres. Elle normalise le texte (minuscules, sans espaces) et pour chaque lettre, elle calcule sa nouvelle position dans l'alphabet.
- **`caesar_decrypt()`** : fait l'opération inverse du chiffrement de César.
- **`caesar_crack()`** : teste tous les décalages possibles (1-26) pour tenter de casser le chiffrement.

## Le Chiffrement de Vigenère

Le chiffrement de Vigenère est une amélioration du César, développée au XVIe siècle. Il utilise une clé (mot ou phrase) et chaque lettre de la clé détermine le décalage à appliquer. Si le message est plus long que la clé, celle-ci est répétée.

### Implémentation

Notre implémentation comprend :

- **`vigenere_encrypt()`** : utilise la position de chaque lettre de la clé comme décalage. La clé est répétée grâce à l'opération modulo sur sa longueur.
- **`vigenere_decrypt()`** : applique le processus inverse du chiffrement de Vigenère.

## Sécurité et Limitations

Ces chiffrements sont aujourd'hui considérés comme non sécurisés car :

- Le chiffrement de César peut être cassé en testant les 26 possibilités.
- Le Vigenère peut être cassé par analyse de fréquence.
- Ils sont vulnérables à l'analyse statistique des langues.

Cependant, ces chiffrements restent importants car :

- Ils introduisent des concepts fondamentaux de la cryptographie.
- Ils ont influencé le développement des chiffrements modernes.
- Les principes de substitution et transposition sont toujours utilisés dans des algorithmes modernes comme **AES**.



---

# Le Concept du One-Time Pad (OTP)

Le One-Time Pad est un système de chiffrement qui offre une sécurité parfaite au sens de Shannon. Ses caractéristiques principales sont :

- **Une clé totalement aléatoire**.
- **Une clé aussi longue que le message**.
- **Une clé utilisée une seule fois**.
- **Une clé gardée absolument secrète**.

## Sécurité Parfaite

La sécurité parfaite selon Shannon signifie que :

- Le texte chiffré ne révèle aucune information sur le texte clair.
- Tous les textes clairs possibles sont équiprobables pour un texte chiffré donné.
- Même avec une puissance de calcul infinie, le système est incassable.

## Implémentation du Code

Notre implémentation propose deux types de chiffrement :

### a) Pour le texte :

- **`text_to_numbers()`** : convertit le texte en nombres (positions dans l'alphabet).
- **`generate_key()`** : crée une clé aléatoire de la longueur nécessaire.
- **`encrypt_text()`** : chiffre le texte par addition modulo 26.
- **`decrypt_text()`** : déchiffre le texte par soustraction modulo 26.

### b) Pour les images :

- **`generate_key_image()`** : crée une clé de la taille de l'image.
- **`encrypt_image()`** : chiffre l'image par XOR bit à bit.
- **`decrypt_image()`** : déchiffre l'image par XOR bit à bit.

## Particularités de l'Implémentation

### Pour le texte :

- Utilisation de l'alphabet (26 lettres).
- Opérations modulo 26 pour rester dans l'alphabet.
- Conversion texte ↔ nombres pour faciliter les opérations.

### Pour les images :

- Utilisation du **XOR** (opération réversible).
- Travail sur les **bytes** (valeurs 0-255).
- Support des **images couleur** (3 canaux RGB).

## Limites et Considérations Pratiques

Bien que théoriquement parfait, l'OTP présente des limitations pratiques :

- Nécessite une clé aussi longue que le message.
- La distribution sécurisée des clés est complexe.
- Le stockage des clés est problématique.
- La synchronisation des clés entre émetteur et récepteur est délicate.

## Usage Historique et Moderne

Le One-Time Pad a été utilisé pour :

- **Communications militaires durant la WWII**.
- **Ligne rouge** entre USA et URSS.
- **Communications diplomatiques** de haut niveau.

Aujourd'hui, son usage est limité aux communications ultra-sensibles en raison de ses contraintes pratiques.


