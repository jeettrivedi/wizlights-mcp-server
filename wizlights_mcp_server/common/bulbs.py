from pywizlight import wizlight

from .validators import is_valid_ip_address


async def get_bulb_state(ip: str) -> dict:
    """
    Get the state of a specific WiZ smart bulb.

    Retrieves the current state of a WiZ smart bulb using its IP address.

    Args:
        ip (str): The IP address of the WiZ smart bulb.

    Returns:
        dict: A dictionary containing the current state of the bulb, including:
            - state (bool): The on/off state of the bulb.
            - source (str): The source of the current state.
            - mac (str): The MAC address of the bulb.
            - power (int): The power consumption of the bulb.
            - warm_white (int): The warm white value of the bulb.
            - white_range (tuple): The white range of the bulb.
            - extended_white_range (tuple): The extended white range of the bulb.
            - speed (int): The speed of the current effect.
            - get_ratio (float): The ratio of the current effect.
            - scene_id (int): The ID of the current scene.
            - scene (str): The name of the current scene.
            - cold_white (int): The cold white value of the bulb.
            - rgb (tuple): The RGB color values of the bulb.
            - rgbw (tuple): The RGBW color values of the bulb.
            - rgbww (tuple): The RGBWW color values of the bulb.
            - brightness (int): The brightness level of the bulb.
            - color_temp (int): The color temperature of the bulb.

    Raises:
        ValueError: If the IP address is invalid.
    """
    if not is_valid_ip_address(ip):
        raise ValueError("Invalid IP address")

    bulb = wizlight(ip)
    state = await bulb.updateState()

    return {
        "state": state.get_state(),
        "source": state.get_source(),
        "mac": state.get_mac(),
        "power": state.get_power(),
        "warm_white": state.get_warm_white(),
        "white_range": state.get_white_range(),
        "extended_white_range": state.get_extended_white_range(),
        "speed": state.get_speed(),
        "get_ratio": state.get_ratio(),
        "scene_id": state.get_scene_id(),
        "scene": state.get_scene(),
        "cold_white": state.get_cold_white(),
        "rgb": state.get_rgb(),
        "rgbw": state.get_rgbw(),
        "rgbww": state.get_rgbww(),
        "brightness": state.get_brightness(),
        "color_temp": state.get_colortemp(),
    }
