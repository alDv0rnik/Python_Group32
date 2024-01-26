class Material:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    @property
    def density(self):
        return self.__density

    @property
    def name(self):
        return self.__name

    def get_material(self):
        return f"{self.name};{self.density}"


class Subject:
    def __init__(self, name, material: Material, volume):
        self.__name = name
        self.__material = material
        self.__volume = volume

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material: Material):
        self.__material = material

    def __get_mass(self):
        return self.__volume * self.material.density

    def get_subject(self):
        return f"{self.__name};{self.material.name};{self.material.density};{self.__volume};{self.__get_mass()}"


if __name__ == '__main__':
    steel = Material("steel",7850.0)
    copper = Material("copper", 8500.0)
    wire = Subject("wire", steel, 0.03)
    print(wire.get_subject())
    wire.material = copper
    print(wire.get_subject())