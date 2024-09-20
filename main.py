#### Fonction secondaire
'''
Fonction Palyndromes
'''

def ispalindrome(s):
    '''
    Determine si 's' est une palindrome ou non.

    Args:
        s : chaine de caracteres
    Returns:
        ispalyndrome(s) : 's est un palyndrome' / 's n'est pas un palyndrome'
    '''
    if len(s)<=1:
        return(s, 'est un palyndrome')
    for i in range (len(s)//2):
        if s[i]!=s[-(i+1)]:
            return (s,"n'est pas un palyndrome")
    return (s,'est un palyndrome')
    # votre code ici
#### Fonction principale


def main():
    '''
    Détermine si la fonction ispalyndrome() fonctionne bien pour les mots suivants :
    "radar", 
    "kayak", 
    "level", 
    "rotor", 
    "civique", 
    "deifie".
    '''
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
    print()


if __name__ == "__main__":
    main()
