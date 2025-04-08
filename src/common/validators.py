def is_valid_ip_address(ip: str) -> bool:
    """
    Validate the given IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    if not ip or not ip.replace(".", "").isdigit():
        return False
    parts = ip.split(".")
    return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
