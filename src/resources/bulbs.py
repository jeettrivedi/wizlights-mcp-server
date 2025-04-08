from mcp.server.fastmcp import FastMCP
from pywizlight import discovery
from pywizlight.scenes import SCENES

from common.bulbs import get_bulb_state
from common.validators import is_valid_ip_address


def register_bulb_resources(mcp: FastMCP) -> None:
    """Register bulb resources with the MCP server."""

    @mcp.resource(
        "bulbs://{broadcast_space}",
        name="get_bulbs",
        description="Get all available bulbs in the broadcast space",
    )
    async def get_bulbs(broadcast_space: str) -> list[dict]:
        """
        Asynchronously retrieves a list of smart bulbs within the specified broadcast space.
        Args:
            broadcast_space (str): The IP address or broadcast space to search for smart bulbs.
                Must be a valid string representing the network space.
        Returns:
            list[dict]: A list of dictionaries, where each dictionary contains the following keys:
                - "ip" (str): The IP address of the bulb.
                - "mac" (str): The MAC address of the bulb.
            If the broadcast_space is invalid, returns a dictionary with an "error" key and a descriptive message.
        """
        if not is_valid_ip_address(broadcast_space):
            return {
                "error": "Invalid broadcast space. Please provide a valid IP address."
            }
        bulbs = await discovery.discover_lights(broadcast_space)
        return [{"ip": bulb.ip, "mac": bulb.mac} for bulb in bulbs]

    @mcp.resource(
        "bulbs://{ip}/state",
        name="get_bulb_state",
        description="Get a specific bulb's state",
    )
    async def get_state(ip: str) -> dict:
        return await get_bulb_state(ip)

    @mcp.resource(
        "bulbs://{ip}/scene",
        name="get_bulb_scene",
        description="Get a specific bulb's scene",
    )
    async def get_scene(ip: str) -> dict:
        """
        Retrieve the current scene of a smart bulb.
        Args:
            ip (str): The IP address of the smart bulb.
        Returns:
            dict: A dictionary containing the current scene of the smart bulb.
                If the IP address is invalid or the bulb is not found, returns an error message.
        """
        try:
            state = await get_bulb_state(ip)
        except ValueError:
            return {"error": "Invalid IP address or bulb not found."}

        return (
            SCENES.get(state.get("scene_id"))
            if state
            else {"error": "Bulb was either not found or is not connected."}
        )
