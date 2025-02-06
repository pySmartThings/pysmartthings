#!/usr/bin/env python3
"""Generate capability constants."""

import re
import sys

from pysmartthings.capability import CAPABILITIES


def main():
    """Run the script."""
    capabilities = CAPABILITIES.copy()
    capabilities.sort()
    for c in capabilities:
        print('{} = "{}"'.format(re.sub(r"([A-Z])", r"_\1", c).lower(), c))


if __name__ == "__main__":
    sys.exit(main())
