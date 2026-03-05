from intent_engine import parse_intent
from command_registry import execute_command

def main():
    user_input = input("HassiOS > ")
    intent = parse_intent(user_input)

    if not intent:
        print("Could not understand command.")
        return

    result = execute_command(intent)
    print(result)

if __name__ == "__main__":
    main()
