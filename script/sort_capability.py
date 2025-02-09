"""Script to sort the capability constants."""

import pyperclip

from pysmartthings.models import Capability


def main() -> int:
    """Run the script."""
    capabilities = {}
    dot_capabilities = {}
    for capability in Capability:
        if "." in capability.value:
            category = capability.value.split(".")[0]
            if category not in dot_capabilities:
                dot_capabilities[category] = {}
            dot_capabilities[category][capability.value] = capability
        else:
            capabilities[capability.value] = capability
    capabilities = dict(sorted(capabilities.items()))
    result = "class Capability(StrEnum):"
    result += '\n    """Capability model."""\n\n'
    for name, capability in capabilities.items():
        result += f'    {capability.name} = "{name}"\n'
    for category_capabilities in dot_capabilities.values():
        result += "\n"
        capabilities = dict(sorted(category_capabilities.items()))
        for name, capability in capabilities.items():
            result += f'    {capability.name} = "{name}"\n'
    print(result)
    pyperclip.copy(result)
    return 0


if __name__ == "__main__":
    main()
