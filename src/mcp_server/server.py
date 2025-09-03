"""
Your MCP server
"""
import os
import base64
import logging
from pathlib import Path
from typing import List

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, ImageContent

# Set up logging (this just prints messages to your terminal for debugging)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create the MCP server object
mcp = FastMCP(
    host="127.0.0.1", port="8081",
    # `host` and `port` will not work for stdio transport
    # set the `host` as `0.0.0.0` if you want to expose this server
)

# Here’s where you define your tools (functions the AI can use)
@mcp.tool()
def add(a: int, b: int) -> TextContent:
    """Add two numbers.

    Args:
        a: the first integer to be added
        b: the second integer to be added
    
    Return:
        The sum of the two integers, as a string."""
    return TextContent(type="text", text=str(a + b))

# The return format should be one of the types defined in mcp.types. The commonly used ones include TextContent, ImageContent, BlobResourceContents.
# In the case of a string, you can also directly use `return str(a + b)` which is equivalent to `return TextContent(type="text", text=str(a + b))`

@mcp.tool()
def get_name_and_image_of_flower() -> List[TextContent | ImageContent]:
    """Get the name and image of flower

    Return:
        Name of flower and its image"""

    current_dir = Path()
    image_path = current_dir / "src/mcp_server/lily.jpeg"

    with open(image_path, "rb") as f:
        image_base64_str = base64.b64encode(f.read()).decode("utf-8")

    return [
        TextContent(text="Lily", type="text"),
        ImageContent(data=image_base64_str, mimeType="image/png", type="image"),
    ]


# This is the main entry point for your server
def main():
    logger.info('Starting your-new-server')
    mcp.run(transport="stdio")
    # mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()

