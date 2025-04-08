# Wizlights MCP Server

## Overview

A Model Context Protocol (MCP) server that enables large language models (LLMs) to control [WizConnected](https://www.wizconnected.com/) smart lights. 

## Prerequisites

- [uv package manager](https://docs.astral.sh/uv/)

**Note**: To run the MCP development server, you also need [Node.js](https://nodejs.org/en).

## Usage

### Installing on Claude Desktop

To use this MCP server with Claude Desktop, install it by running
```bash
mcp install wizlights_mcp_server/server.py
```

### Development Mode

```bash
mcp dev server.py

# Mount local code
mcp dev server.py --with-editable .
```

## Acknowledgements

This package relies heavily on the [pywizlight](https://github.com/sbidy/pywizlight) package to communicate with the WiZ devices.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.