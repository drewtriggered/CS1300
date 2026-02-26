# Ask the user for input
temp = float(input("Enter the current temperature (°F): "))
raining_input = input("Is it raining? (yes/no): ").strip().lower()

# Convert rain input to Boolean
raining = raining_input == "yes"

# Temperature advisory system
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    if raining:
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif 60 <= temp <= 85:
    if raining:
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif 32 <= temp <= 59:
    print("It's cold — bundle up!")

else:  # temp < 32
    print("FREEZE WARNING: Roads may be icy!")