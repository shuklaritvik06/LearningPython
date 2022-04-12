sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result_list = sentence.split()
result = {key: len(key) for key in result_list}
print(result)
