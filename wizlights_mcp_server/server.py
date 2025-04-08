import logging
from mcp.server.fastmcp import FastMCP

from wizlights_mcp_server.resources.bulbs import register_bulb_resources
from wizlights_mcp_server.resources.scenes import register_scene_resources
from wizlights_mcp_server.tools.bulbs import register_bulb_tools

log = logging.getLogger(__name__)

# Create an MCP server
log.info("Creating MCP server...")
mcp = FastMCP("WizLights")

# Register resources
log.info("Registering resources...")
register_bulb_resources(mcp)
register_scene_resources(mcp)

# Register tools
log.info("Registering tools...")
register_bulb_tools(mcp)

log.info("WizLights MCP server started.")

