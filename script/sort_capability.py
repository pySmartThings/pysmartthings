"""Script to sort the capability constants."""

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
    print("class Capability(StrEnum):")
    print('    """Capability model."""')
    print()
    for name, capability in capabilities.items():
        print(f'    {capability.name} = "{name}"')
    for category_capabilities in dot_capabilities.values():
        print()
        capabilities = dict(sorted(category_capabilities.items()))
        for name, capability in capabilities.items():
            print(f'    {capability.name} = "{name}"')
    return 0


if __name__ == "__main__":
    main()
