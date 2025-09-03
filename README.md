# 📦 PyPI Info Tool - MCP Server

This project implements a **Model Context Protocol (MCP) server** using the **Python SDK**.  
It provides an MCP tool that fetches **PyPI package information** for any given package name.  
The server is lightweight and runs as a **Stream-SSE (Server-Sent Events)** service, making it easy to integrate into editors like **VS Code**.

---

## ✨ Features
- Built with **FastMCP** (Python SDK for MCP).  
- Exposes a tool `pypi_info` for retrieving package details from **PyPI**.  
- Simple and efficient **entrypoint**: `server.py`.  
- Easy to run and extend for additional tools.  

---

## 📂 Repository Structure
```
PyPI-Info-Tool/
│
├── get_pypi_info.py    # Function to fetch PyPI package details
├── pyproject.toml      # Project configuration (Poetry)
├── poetry.lock         # Dependency lock file
├── server.py           # MCP server entrypoint
└── serve/              # (Optional) Additional scripts or configs
```

---

## ⚙️ How It Works
1. **Server Setup**  
   - Uses `FastMCP` to initialize the MCP server with the name **"PyPI Info Tool"**.  

2. **Tool Definition**  
   - Defines a tool `pypi_info(package_name: str)` decorated with `@mcp.tool()`.  
   - This tool calls the helper function `get_pypi_package_info` to retrieve package metadata from PyPI.  

3. **Execution**  
   - The server runs via:
     ```bash
     python server.py
     ```
   - Communication happens over **SSE transport**.  

---

## 🚀 Example Usage
Call the tool inside MCP-enabled environments (e.g., VS Code with Copilot MCP):  
```python
pypi_info("requests")
```
✅ Returns detailed information about the **requests** package from PyPI.  

---

## 🛠️ Tech Stack
- **Python**  
- **FastMCP (MCP SDK)**  **Python sdk** link: https://github.com/modelcontextprotocol/python-sdk
- **PyPI API**  

---

## 📄 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.  
