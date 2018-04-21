import testserver
exercise_id = "moving_average"

def moving_average (signal, window_size):
    # signal is an array of real numbers
    
    # TODO implement me
    
    filteredSignal = []
    return filteredSignal;


test = testserver.get_testdata(exercise_id)
sessionId = test['session']
signals = test['signals']
filteredSignals = [];

for s in signals:
    window_size = s['window']
    result = {'id': s['id'], 'values': moving_average(s['values'], window_size)}
    filteredSignals.append(result)

result_data = {'session': sessionId,
               'results': filteredSignals}
response = testserver.send_result(exercise_id, result_data)

# you can check the result on the dashboard-website or in the response data
print("Auswertung")
for c in response['classification']:
    print("Klasse: "+ str(c['class']) +" | Wahrscheinlichkeit: "+ str(c['probability']))
