"""Sort the Command enum."""

import pyperclip
from pysmartthings.models import Command


def main() -> int:
    """Run the script."""
    commands = {attr.name: attr for attr in Command}
    commands = dict(sorted(commands.items()))
    result = "class Command(StrEnum):"
    result += '\n    """Command model."""\n\n'
    for name, command in commands.items():
        result += f'    {name} = "{command.value}"\n'
    pyperclip.copy(result)
    print(result)
    return 0


if __name__ == "__main__":
    main()
