"""
MCP server entrypoint for PyPI Info Tool.
"""

from mcp.server.fastmcp import FastMCP
from get_pypi_info import get_pypi_package_info

mcp = FastMCP("PyPI Info Tool")

@mcp.tool()
def pypi_info(package_name: str):
    """
    MCP tool to fetch PyPI package information for a given package name.
    """
    return get_pypi_package_info(package_name)

if __name__ == "__main__":
    mcp.run(transport="sse")
