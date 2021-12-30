import pandas

data = pandas.read_csv("weather_data.csv")

print(data.temp)

temp_list = data["temp"].to_list()

print(temp_list)
print("Average:")
# print(sum(temp_list)/len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

print(data.condition)

print(data[data.temp == data["temp"].max()])