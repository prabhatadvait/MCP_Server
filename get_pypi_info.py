"""
MCP tool to fetch PyPI package information using FastMCP.
"""

import requests
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PyPI Info Tool")

PYPI_API_URL = "https://pypi.org/pypi/{package}/json"

@mcp.tool()
def get_pypi_package_info(package_name: str) -> Dict[str, Any]:
    """
    Fetches package information from the PyPI API for the given package name.
    Returns a dictionary with maintainers, versions, extra info, and description.
    """
    url = PYPI_API_URL.format(package=package_name)
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Package '{package_name}' not found on PyPI.")
    data = response.json()
    info = data.get("info", {})
    releases = data.get("releases", {})

    maintainers = []
    if info.get("maintainer"):
        maintainers.append(info["maintainer"])
    if info.get("author") and info["author"] not in maintainers:
        maintainers.append(info["author"])

    result = {
        "name": info.get("name"),
        "summary": info.get("summary"),
        "description": info.get("description"),
        "maintainers": maintainers,
        "author_email": info.get("author_email"),
        "license": info.get("license"),
        "home_page": info.get("home_page"),
        "project_url": info.get("project_url"),
        "package_url": info.get("package_url"),
        "docs_url": info.get("docs_url"),
        "versions": list(releases.keys()),
        "requires_python": info.get("requires_python"),
        "keywords": info.get("keywords"),
        "classifiers": info.get("classifiers"),
    }
    return result

if __name__ == "__main__":
    mcp.run()
