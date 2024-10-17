temperatures = (
    ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5',
     '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
    ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7',
     '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
    ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9',
     '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
)


def analyze_temprature(temps):
    # Extract temprature lists for the years of interest
    # Convert to float for numerical comparison
    temps_1995 = set(map(float, temps[0][2]))
    temps_2010 = set(map(float, temps[1][2]))
    temps_2020 = set(map(float, temps[2][2]))

    # Question 1: Different values in both March 1995 and March 2010
    common_1995_2010 = temps_1995.intersection(temps_2010)
    answer_1 = len(common_1995_2010)

    # Question 2: Different values in both March 1995 and March 2020
    common_1995_2020 = temps_1995.intersection(temps_2020)
    answer_2 = len(common_1995_2020)

    # Question 3: Year with the highest temperature
    highest_temp_1995 = max(temps_1995)
    highest_temp_2010 = max(temps_2010)
    highest_temp_2020 = max(temps_2020)

    max_temp = max(highest_temp_1995, highest_temp_2010, highest_temp_2020)

    if max_temp == highest_temp_1995:
        answer_3 = "1995"
    elif max_temp == highest_temp_2010:
        answer_3 = "2010"
    else:
        answer_3 = "2020"

    # Question 4: Year with the warmest March (average of all temperatures)
    avg_temp_1995 = sum(temps_1995) / len(temps_1995)
    avg_temp_2010 = sum(temps_2010) / len(temps_2010)
    avg_temp_2020 = sum(temps_2020) / len(temps_2020)

    max_avg_temp = max(avg_temp_1995, avg_temp_2010, avg_temp_2020)

    if max_avg_temp == avg_temp_1995:
        answer_4 = "1995"
    elif max_avg_temp == avg_temp_2010:
        answer_4 = "2010"
    else:
        answer_4 = "2020"

    return answer_1, answer_2, answer_3, answer_4


# Execute the analysis
answers = analyze_temperatures(temperatures)

# Print results
for i, answer in enumerate(answers, start=1):
    print(f"Answer_{i}: {answer}")
