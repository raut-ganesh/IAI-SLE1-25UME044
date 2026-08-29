# AI-Based Smart Home Agent

def smart_home_agent(temperature, light, motion):
    print("\nSmart Home Agent")
    print("----------------")

    print("Temperature:", temperature, "C")
    print("Light Level:", light)
    print("Motion:", motion)

    # Temperature decision
    if temperature > 28:
        print("Action: Turn ON AC")
    else:
        print("Action: Keep AC OFF")

    # Light decision
    if light == "Dark" and motion == "Detected":
        print("Action: Turn ON Lights")
    else:
        print("Action: Turn OFF Lights")

    # Security decision
    if motion == "Detected":
        print("Action: Monitor Room")
    else:
        print("Action: Security Mode ON")


# Sample environment
temperature = 30
light = "Dark"
motion = "Detected"

# Run the smart home agent
smart_home_agent(temperature, light, motion)
