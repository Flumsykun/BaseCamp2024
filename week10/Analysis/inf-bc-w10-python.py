# Read the body of load_data(self). Try to guess how the data columns are structured.
# Reading the method load_data(self) we may understand the structure of the data columns
# and data types, but still we don't know the meaning of data values. This is something
# we can extract from the method construct_temprature_list(self). Read this method carefully
# and try to explain what will be result of this method?
# Manually write some lines within a text file and try to run the code using your own data values.
# Does it print what you expect?



class TemperatureDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.temperature_data = []

    # Method to open the file and load lines as an attribute
    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = [line.strip().split() for line in file]
                # Attempt to convert each value, and handle any value errors
                self.temperature_data = []
                for d in data:
                    try:
                        # Convert first 3 elements to integers and the last element (temperature) to float
                        self.temperature_data.append(list(map(int, d[:-1])) + [float(d[-1])])
                    except ValueError as e:
                        print(f"Error processing line '{' '.join(d)}': {e}")
                        continue  # Skip this line if it causes an error
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
        except IOError as e:
            print(f"Error: There was an issue reading the file {self.file_path}: {e}")

    # Method to perform the analysis and construct the list
    def construct_temperature_list(self):
        temperature_list = []
        for data in self.temperature_data:
            try:
                month, day, year, temperature = data
                if year not in [item[0] for item in temperature_list]:
                    temperature_list.append((year, {}))
                if month not in temperature_list[-1][1]:
                    temperature_list[-1][1][month] = 0.0
                temperature_list[-1][1][month] = max(temperature, temperature_list[-1][1][month])
            except ValueError:
                print(f"Error: Malformed data entry {data}. Skipping this entry.")
                continue
        return temperature_list

def main():
    file_path = './temps.txt'
    analyzer = TemperatureDataAnalyzer(file_path)
    analyzer.load_data()
    if analyzer.temperature_data:  # Check if data was loaded successfully
        temperature_list = analyzer.construct_temperature_list()
        print(temperature_list)
    else:
        print("No valid data was loaded.")

if __name__ == '__main__':
    main()
