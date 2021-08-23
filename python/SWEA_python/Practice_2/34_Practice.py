beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

print(beer)

for key, value in beer.items():
    beer[key] = value * 1.05

print(beer)