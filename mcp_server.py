from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

# Initialize MCP with a name
mcp = FastMCP("Job Recommender")

# Define the LinkedIn tool
@mcp.tool()
async def fetchlinkedin(listofkey: list[str]) -> list[str]:
    return fetch_linkedin_jobs(listofkey)

# Define the Naukri tool
@mcp.tool()
async def fetchnaukri(listofkey: list[str]) -> list[str]:
    return fetch_naukri_jobs(listofkey)

# Run MCP server with HTTP transport
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8501)
