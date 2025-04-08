from mcp.server.fastmcp import FastMCP
from pywizlight.scenes import SCENES


def register_scene_resources(mcp: FastMCP) -> None:
    """Register scene resources to the MCP server."""

    @mcp.resource(
        "scenes://",
        name="get_scenes",
        description="Get all available scenes",
    )
    async def get_scenes() -> list:
        """Get all available scenes"""
        return list(SCENES.values())
    