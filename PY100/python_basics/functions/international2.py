def local_greet(locale):

    # Identify the language
    def extract_language(locale):
        language = locale[0:2]
        return language

    # Identify the region
    def extract_region(locale):
        region = locale.split('_')[1].split('.')[0]
        return region

    language = extract_language(locale)
    region = extract_region(locale)

    # Identify the greeting
    def greeting(language, region):
        match language:
            case 'en':
                match region:
                    case 'GB':
                        return 'Top of the morning!'
                    case 'AU':
                        return "G'day mate!"
                    case 'US':
                        return "What's up?"
                    case _:
                        return 'Hello'
            case 'fr':
                return 'Bonjour!'
            case 'pt':
                return 'Olá!'
            case 'de':
                return 'Hallo!'
            case 'se':
                return 'Hej!'
            case 'saf':
                return 'Haai!'
    
    your_greeting = greeting(language, region)

    return your_greeting

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!