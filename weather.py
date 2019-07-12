import pyowm

city = input("Please enter a city")
#country = input("please enter a country")

apiKey = '1ae2401ff4ef1dd27589ae76741ad9b2'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place('city,country')
w= observation.get_weather()


print("This shows the weater of ",city)
print("*************************************************")
print("The wind is: ", w.get_wind())
print("The humidity is: ", w.get_humidity())
print("The cloud is: ", w.get_clouds())
print("The rain is: ", w.get_rain())
print("The snow is: ", w.get_snow())
print("The pressure is: ", w.get_pressure())
print("The temperature is: ", w.get_temperature())
#print("The temperature is: ", w.get_temperature(unit='fahrenheit'))
