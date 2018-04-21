import testserver
exercise_id = "median"

test = testserver.get_testdata(exercise_id)

test_id = test['session']
signals = test['signals']
results = []

# TODO Process every signal in 'signals' array and save the result in the 'results' array
for signal in signals:
    # signal is a dictionary with the following structure
    # # 'id' -> unique numeric identifier for the specific signal
    # # 'values' -> array of real numbers
    number_of_values = len(signal["values"])
    sorted_values = sorted(signal["values"])

    if number_of_values % 2:  # ungrade
        index_of_median = (number_of_values + 1)/2
        index_of_median -= 1
        median = sorted_values[int(index_of_median)]
    else:  # grade
        index_of_median_lower = number_of_values / 2
        index_of_median_lower -= 1
        index_of_median_upper = number_of_values / 2

        median = 0.5 * (sorted_values[int(index_of_median_lower)] + sorted_values[int(index_of_median_upper)])


    # result is a dictionary with the following structure
    # # 'id' -> unique numeric identifier for the corresponding signal
    # # 'median' -> median of the signal
    result = {"id":signal["id"], "median":median}
    results.append(result)

result_data = {'session': test_id,
               'results': results}
response = testserver.send_result(exercise_id, result_data)

# you can check the result on the dashboard-website or in the response data
print("Auswertung")
for c in response['classification']:
    print("Klasse: "+ str(c['class']) +" | Wahrscheinlichkeit: "+ str(c['probability'])) 
