from pywizlight import PilotBuilder, wizlight
from pywizlight.scenes import get_id_from_scene_name

from wizlights_mcp_server.common.bulbs import get_bulb_state
from wizlights_mcp_server.common.validators import is_valid_ip_address
from wizlights_mcp_server.models.state import StateModel


def register_bulb_tools(mcp):
    @mcp.tool("bulb://{ip}/set_state", description="Set a specific bulb's state")
    async def set_light_state(ip: str, state: dict) -> dict:
        """Set a specific bulb's state"""

        if not is_valid_ip_address(ip):
            return {"error": "Invalid IP address. Please provide a valid IP address."}

        bulb = wizlight(ip)

        try:
            StateModel(**state)
        except Exception as e:
            return {"error": f"Invalid state structure: {str(e)}"}

        # Extract fields from the parsed request
        rgb = state.get("rgb")
        rgbw = state.get("rgbw")
        rgbww = state.get("rgbww")
        brightness = state.get("brightness")
        colortemp = state.get("colortemp")
        warm_white = state.get("warm_white")
        cold_white = state.get("cold_white")
        speed = state.get("speed")
        scene = state.get("scene")
        hucolor = state.get("hucolor")
        ratio = state.get("ratio")
        power = state.get("state", "true").lower() == "true"

        # Build the PilotBuilder with the provided fields
        pilot_builder = PilotBuilder(
            rgb=rgb,
            rgbw=rgbw,
            rgbww=rgbww,
            brightness=brightness,
            colortemp=colortemp,
            warm_white=warm_white,
            cold_white=cold_white,
            speed=speed,
            scene=scene,
            hucolor=hucolor,
            ratio=ratio,
            state=power,
        )
        await bulb.turn_on(pilot_builder)
        return await get_bulb_state(ip)

    @mcp.tool(
        "bulb://{ip}/toggle",
        description="Toggle a specific bulb's state",
    )
    async def toggle_light(ip: str) -> dict:
        """Toggle a specific bulb's state

        Args:
            ip (str): The IP address of the bulb.

        Returns:
            dict: The updated state of the bulb.
        """

        if not is_valid_ip_address(ip):
            return {"error": "Invalid IP address. Please provide a valid IP address."}

        bulb = wizlight(ip)
        state = await bulb.updateState()
        current_state = state.get_state()

        await bulb.turn_on(
            PilotBuilder(
                state=not current_state,
            )
        )

        return await get_bulb_state(ip)

    @mcp.tool(
        "bulb://{ip}/set_scene",
        description="Set a specific bulb's scene",
    )
    async def set_scene(ip: str, scene: str) -> dict:
        """Set a specific bulb's scene

        Args:
            ip (str): The IP address of the bulb.
            scene (str): The scene name to set.
        Returns:
            dict: The updated state of the bulb.
        """

        if not is_valid_ip_address(ip):
            return {"error": "Invalid IP address. Please provide a valid IP address."}

        if not scene:
            return {"error": "Scene name is required."}

        try:
            scene_id = get_id_from_scene_name(scene)
        except ValueError:
            return {"error": "Invalid scene name"}

        bulb = wizlight(ip)
        await bulb.turn_on(
            PilotBuilder(
                scene=scene_id,
            )
        )

        return await get_bulb_state(ip)
