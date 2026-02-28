# pysmartthings Examples

This directory contains practical examples demonstrating how to use the pysmartthings library.

## Prerequisites

1. **Python 3.12+** - This library uses modern async/await syntax
2. **SmartThings Account** - You need a Samsung SmartThings account
3. **Personal Access Token** - Required for API authentication

## Getting Your SmartThings API Token

1. Go to the [SmartThings Personal Access Tokens](https://account.smartthings.com/tokens) page
2. Click "Generate new token"
3. Give it a name (e.g., "pysmartthings development")
4. Select the required scopes:
   - `r:devices:*` - Read device information
   - `x:devices:*` - Execute device commands
   - `r:locations:*` - Read location information
   - `r:scenes:*` - Read scenes
   - `x:scenes:*` - Execute scenes
   - `r:rooms:*` - Read rooms
   - Additional scopes as needed for your use case
5. Click "Generate token"
6. **Copy the token immediately** - you won't be able to see it again!

## Installation

```bash
# Install pysmartthings
pip install pysmartthings

# Or with poetry
poetry add pysmartthings
```

## Running the Examples

Each example is a standalone Python script. You'll need to replace `YOUR_TOKEN_HERE` with your actual SmartThings Personal Access Token.

### Quick Start

```bash
# Basic usage - list devices and get device details
python examples/basic_usage.py

# Control devices - switches, dimmers, lights, thermostats
python examples/control_devices.py

# Scenes - list and execute scenes
python examples/scenes.py

# Lock codes - manage smart lock codes (requires lock device)
python examples/lock_codes.py

# Event subscription - real-time device events via SSE
python examples/event_subscription.py

# Async patterns - concurrent operations and error handling
python examples/async_patterns.py
```

## Examples Overview

### 1. basic_usage.py
**What it demonstrates:**
- Creating and authenticating a SmartThings client
- Listing all devices
- Getting detailed device information
- Checking device status
- Listing locations and rooms

**Use this when:** You're getting started with the library

### 2. control_devices.py
**What it demonstrates:**
- Controlling switches (on/off)
- Dimming lights (0-100%)
- Setting color lights (RGB)
- Controlling thermostats (temperature, mode)
- Checking capabilities before executing commands

**Use this when:** You need to control your SmartThings devices

### 3. scenes.py
**What it demonstrates:**
- Listing available scenes
- Filtering scenes by location
- Executing scenes
- Error handling for scene operations

**Use this when:** You want to trigger SmartThings scenes/automations

### 4. lock_codes.py
**What it demonstrates:**
- Checking if a device supports lock codes
- Setting lock codes (PIN codes)
- Deleting lock codes
- Locking and unlocking doors
- Managing multiple codes

**Use this when:** You have smart locks and need to manage access codes

### 5. event_subscription.py
**What it demonstrates:**
- Subscribing to real-time device events
- Handling device state changes
- Processing health events
- Managing subscriptions lifecycle
- Event filtering and processing

**Use this when:** You need real-time notifications of device changes

### 6. async_patterns.py
**What it demonstrates:**
- Running multiple operations concurrently
- Proper session management
- Error handling with specific exceptions
- Retry logic for transient failures
- Timeout handling
- Best practices for async/await

**Use this when:** You're building production applications

## Common Patterns

### Session Management

```python
from aiohttp import ClientSession
from pysmartthings import SmartThings

# Recommended: Manage session yourself for multiple clients
async with ClientSession() as session:
    api = SmartThings(session=session)
    api.authenticate("YOUR_TOKEN_HERE")
    # Use api...

# Alternative: Let SmartThings manage the session
api = SmartThings()
api.authenticate("YOUR_TOKEN_HERE")
# Session created automatically on first request
```

### Error Handling

```python
from pysmartthings import (
    SmartThingsAuthenticationFailedError,
    SmartThingsNotFoundError,
    SmartThingsConnectionError,
)

try:
    device = await api.get_device(device_id)
except SmartThingsAuthenticationFailedError:
    print("Token expired or invalid")
except SmartThingsNotFoundError:
    print(f"Device {device_id} not found")
except SmartThingsConnectionError as err:
    print(f"Network error: {err}")
```

### Checking Capabilities

```python
from pysmartthings import Capability

# Check if device supports a capability before using it
if Capability.SWITCH in device.capabilities:
    await api.execute_device_command(
        device.device_id,
        Capability.SWITCH,
        Command.ON
    )
```

## Environment Variables (Optional)

For security, you can store your token in an environment variable:

```bash
export SMARTTHINGS_TOKEN="your-token-here"
```

Then in your code:

```python
import os
token = os.getenv("SMARTTHINGS_TOKEN")
api.authenticate(token)
```

## Troubleshooting

### "Authentication Failed" Error
- Verify your token is correct and hasn't expired
- Check that you've granted the necessary scopes
- Tokens can be revoked - you may need to generate a new one

### "Not Found" Error
- Check that the device/scene/location ID is correct
- Ensure the resource exists in your SmartThings account
- Some devices may not be accessible via the cloud API

### "Connection Error"
- Verify your internet connection
- Check if the SmartThings API is operational
- Review rate limits (429 errors)

### "Command Error"
- Verify the device supports the capability
- Check command arguments match the capability requirements
- Some devices require specific component names

## Additional Resources

- [SmartThings API Documentation](https://developer.smartthings.com/docs)
- [SmartThings Capabilities Reference](https://developer.smartthings.com/docs/devices/capabilities/capabilities-reference)
- [pysmartthings GitHub](https://github.com/pySmartThings/pysmartthings)
- [Technical Documentation](../CLAUDE.md) - For contributors and advanced usage

## Contributing

Found a bug in an example or want to add a new one? See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

These examples are provided under the Apache 2.0 license, same as the main library.
