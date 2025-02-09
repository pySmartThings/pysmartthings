"""Sort the Attribute enum."""

import pyperclip

from pysmartthings.models import Attribute


def main() -> int:
    """Run the script."""
    attributes = {attr.name: attr for attr in Attribute}
    attributes = dict(sorted(attributes.items()))
    result = "class Attribute(StrEnum):"
    result += '\n    """Attribute model."""\n\n'
    for name, attribute in attributes.items():
        result += f'    {name} = "{attribute.value}"\n'
    pyperclip.copy(result)
    print(result)
    return 0


if __name__ == "__main__":
    main()
