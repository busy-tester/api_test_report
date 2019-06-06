# A='kd345l3kl5n6l7ml6km8766m78ml56m11'
# print(len(A))
import json

b='{"productClass":"1","productName":"666","placeOrigin":"","featurePoint":"[]","plantGrowthPeriod":"","plantHarvestTime":"","plantCrop":"","animalLactation":"","animalIsHerbivorous":"","animalPurpose":"","animalScope":"","animalYield":"","aquaticCultureType":"","aquaticCulturePeriod":"","executiveStandard":""}'
print(type(b))
c=json.loads(b)
print(type(c))