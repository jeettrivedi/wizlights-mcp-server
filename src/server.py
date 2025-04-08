from mcp.server.fastmcp import FastMCP

from resources.bulbs import register_bulb_resources
from resources.scenes import register_scene_resources
from tools.bulbs import register_bulb_tools

# Create an MCP server
mcp = FastMCP("WizLights")

# Register resources
register_bulb_resources(mcp)
register_scene_resources(mcp)

# Register tools
register_bulb_tools(mcp)
