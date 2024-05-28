class Building:
    def __init__(self, numberOfFoors):
        self.numberOfFoors = numberOfFoors

    def __str__(self, buildingType):
        self.buildingType = buildingType

    def __eg__(self, other):
        return self.numberOfFoors == other.buildingType


numberOfFoors = 25
buildingType = 'build'


print(numberOfFoors)
print(buildingType)
print(numberOfFoors==buildingType)
