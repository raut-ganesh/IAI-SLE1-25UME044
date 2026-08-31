# AI-Based Smart Home Agent

def create_smart_home_agent():

    print("=" * 60)
    print("🏠 AI Smart Home Agent Initialized")
    print("Type 'exit' or 'quit' to end the session.")
    print("=" * 60 + "\n")

    while True:
        try:
            # Take temperature input
            temperature_input = input("\n🌡️ Temperature (C): ").strip()

            if not temperature_input:
                continue

            if temperature_input.lower() in ["exit", "quit"]:
                print("Exiting session. Goodbye!")
                break

            temperature = float(temperature_input)

            # Take light input
            light = input("💡 Light Level (Bright/Dark): ").strip()

            if not light:
                continue

            if light.lower() in ["exit", "quit"]:
                print("Exiting session. Goodbye!")
                break

            # Take motion input
            motion = input("🚶 Motion (Detected/Not Detected): ").strip()

            if not motion:
                continue

            if motion.lower() in ["exit", "quit"]:
                print("Exiting session. Goodbye!")
                break

            print("\n🤖 Agent is analyzing the environment...\n")

            # Display environment
            print("Smart Home Agent")
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

        except ValueError:
            print("\n❌ Error: Please enter a valid temperature.")

        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break

        except Exception as e:
            print(f"\n❌ Error encountered: {e}")


if __name__ == "__main__":
    create_smart_home_agent()
