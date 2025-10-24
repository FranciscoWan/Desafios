palavra = input("Digite a palavra secreta: ").lower()
tentativas = 6 # Cabeça, corpo, 2 braços, 2 pernas
letras_acertadas = ['_'] * len(palavra)
letras_erradas = []
print("\n" * 50)  # Limpa a tela para esconder a palavra secreta
print("Bem-vindo ao Jogo da Forca!")
while tentativas > 0 and '_' in letras_acertadas:
    print("\nPalavra: " + ' '.join(letras_acertadas))
    print(f"Tentativas restantes: {tentativas}")
    print("Letras erradas: " + ', '.join(letras_erradas))
    palpite = input("Digite uma letra: ").lower()
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue
    if palpite in letras_acertadas or palpite in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue
    if palpite in palavra:
        for i, letra in enumerate(palavra):
            if letra == palpite:
                letras_acertadas[i] = palpite
        print("Boa! Você acertou uma letra.")
        if '_' not in letras_acertadas:
            print(f"\nParabéns! Você ganhou! A palavra era: {palavra}")
            break
    else:
        letras_erradas.append(palpite)
        tentativas -= 1
        print("Letra errada.")