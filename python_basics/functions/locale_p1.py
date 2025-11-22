# Write a function that extracts the language code from a locale. 
# A locale is a combination of a language code, a region, 
# and usually also a character set, e.g en_US.UTF-8.

def extract_language(locale_name):
    language_code = locale_name[0:2]
    return language_code

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16')) 