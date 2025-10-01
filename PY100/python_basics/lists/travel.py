def contains(city, city_list):
    if city_list.count(city) > 0:
        return True
    else:
        return False

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

# Even Better version

# def contains(city, city_list):
#    return city in city_list