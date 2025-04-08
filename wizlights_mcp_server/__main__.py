from wizlights_mcp_server.server import mcp

def main():
    """
    Entry point for the wizlights-mcp-server script.
    """
    mcp.run(
        transport="stdio"
    )