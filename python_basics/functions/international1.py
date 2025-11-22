def greeting(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'se':
            return 'Hej!'
        case 'saf':
            return 'Haai!'

your_greeting = greeting(input('Select a language code: '))

print(your_greeting)