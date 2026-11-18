from mcp.server import MCPServer
from typing import Dict, Any
import os

mcp = MCPServer("SampleServer", version="1.0.0")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.resource("docs://readme", mime_type="text/markdown")
def readme() -> str:
    """How to use this server"""

    return "# Bookshop\n\nSearch the catalog with the search_books tool"


@mcp.resource("catalog://category_count", mime_type="application/json")
def catalog_stats() -> Dict[str, any]:
    """Provides the count for every category of books available"""
    return {
        "horror": 25,
        "thriller": 30,
        "self-motivation": 15
    }


@mcp.resource("user://{profile}/library")
def get_user_profile(profile: str) -> str:
    """Based on the user profile, certain number of books can be issued"""

    if profile == 'admin':
        max_books_issued = 5
    elif profile == 'student':
        max_books_issued = 3
    else:
        max_books_issued = 1

    return f"With profile as {profile}, you can issue a max of {max_books_issued} number of books"


@mcp.resource("config://user")
def get_user_role() -> Any:
    """User Roles"""

    return ['admin', 'super-user', 'intern', 'employee']


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT")),
    )
