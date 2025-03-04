from lang import TERRAIN_LIST

class Terrain:
    def __init__(self, name, image, rarity, route):
        self.name = name
        self.image = image
        self.rarity = rarity
        self.route = route

    def __str__(self):
        return f"Terrain(name={self.name}, rarity={self.rarity}, route={self.route})"

    def apply_terrain(self):
        # Lógica para aplicar el terreno
        
        print(f"Applying terrain: {self.name}")
        return f"Terrain {self.name} applied from {self.route}"

    def __repr__(self):
        return f"Terrain(name={self.name}, image={self.image}, rarity={self.rarity}, route={self.route})"


# Función para instanciar terrenos a partir del diccionario TERRAIN_LIST
def instantiate_terrains(language):
    terrains = []
    for key, value in TERRAIN_LIST[language].items():
        terrain = Terrain(value["name"], value["image"], value["rarity"], value["route"])
        terrains.append(terrain)
    return terrains