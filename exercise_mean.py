import testserver
exercise_id = "mean"

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
    mean = sum(signal["values"]) / number_of_values

    # result is a dictionary with the following structure
    # # 'id' -> unique numeric identifier for the corresponding signal
    # # 'mean' -> arithmetic mean value of the signal
    result = {"id":signal["id"], "mean":mean}
    results.append(result)

result_data = {'session': test_id,
               'results': results}
response = testserver.send_result(exercise_id, result_data)

# you can check the result on the dashboard-website or in the response data
print("Auswertung")
for c in response['classification']:
    print("Klasse: "+ str(c['class']) +" | Wahrscheinlichkeit: "+ str(c['probability'])) 
