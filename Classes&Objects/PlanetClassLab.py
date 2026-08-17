class Planet:
    def __init__(self, name, planet_type, star):
        if not all(isinstance(x, str) for x in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")

        if name == "":
            raise ValueError("name must be a non-empty string")
        if planet_type == "":
            raise ValueError("planet_type must be a non-empty string")
        if star == "":
            raise ValueError("star must be a non-empty string")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"



planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Mars", "Terrestrial", "Sun")
planet_3 = Planet("Jupiter", "Gas Giant", "Sun")

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

print(planet_1)
print(planet_2)
print(planet_3)
