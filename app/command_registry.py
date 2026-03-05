from commands.log_work import log_work

COMMANDS = {
    "log_work": log_work,
}

def execute_command(intent):
    command_name = intent.get("intent")

    if command_name not in COMMANDS:
        return "Command not allowed."

    return COMMANDS[command_name](**intent)
