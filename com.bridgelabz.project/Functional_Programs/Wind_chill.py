import math


t=float(input("Enter the temperture(in F):"))
v=float(input("Enter the wind_speed (in miles/hour):"))

if (abs(t) > 50 or v < 3 or v > 120):
    print("You.. have entered invalid credencials.. note: |t| < 50 and v > 3 and v < 120...")


else:
    wind_chill=35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

    print(f"Temperature:{t}°F")
    print(f"Wind_Speed:{v}mph")
    print(f"The chillness wind for given value:{wind_chill}°F")
