# Write some code to remove 'fossil' from the list, 
# then add 'geothermal' to the end of the list.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.append('geothermal')
energy.remove('fossil')

print(energy)
