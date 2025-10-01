def extract_region(locale_name):
    return locale_name.split('_')[1].split('.')[0]

print(extract_region('en_US.UTF-8'))      
print(extract_region('en_GB.UTF-8'))      
print(extract_region('ko_KR.UTF-16')) 