class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit
        self.length_in_meters = self.convert_to_meters()

    def convert_to_meters(self):
        if self.unit == "inches":
            return self.length * 0.0254
        elif self.unit == "feet":
            return self.length * 0.3048
        elif self.unit == "yards":
            return self.length * 0.9144
        elif self.unit == "miles":
            return self.length * 1609.344
        elif self.unit == "millimeters":
            return self.length / 1000
        elif self.unit == "centimeters":
            return self.length / 100
        elif self.unit == "meters":
            return self.length
        elif self.unit == "kilometers":
            return self.length * 1000
        else:
            raise ValueError("Unknown unit")

    def inches(self):
        return round(self.length_in_meters / 0.0254, 5)

    def feet(self):
        return round(self.length_in_meters / 0.3048, 5)

    def yards(self):
        return round(self.length_in_meters / 0.9144, 5)

    def miles(self):
        return round(self.length_in_meters / 1609.344, 5)

    def kilometers(self):
        return round(self.length_in_meters / 1000, 5)

    def meters(self):
        return round(self.length_in_meters, 5)

    def centimeters(self):
        return round(self.length_in_meters * 100, 5)

    def millimeters(self):
        return round(self.length_in_meters * 1000, 5)

    def __str__(self):
        return f"<{self.__class__.__name__} object at {hex(id(self))}>"

    def __repr__(self):
        return f"Converter({self.length}, '{self.unit}')"


if __name__ == "__main__":
    length = float(input("Enter a length: "))
    unit = input("Enter the unit (inches, feet, yards, miles, centimeters, meters, kilometers): ")
    converter = Converter(length, unit)
    print(f"{length} {unit} = {converter.inches()} inches")
    print(f"{length} {unit} = {converter.feet()} feet")
    print(f"{length} {unit} = {converter.yards()} yards")
    print(f"{length} {unit} = {converter.miles()} miles")
    print(f"{length} {unit} = {converter.millimeters()} millimeters")
    print(f"{length} {unit} = {converter.centimeters()} centimeters")
    print(f"{length} {unit} = {converter.meters()} meters")
    print(f"{length} {unit} = {converter.kilometers()} kilometers")
