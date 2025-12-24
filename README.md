# Unified Math Local MCP Server 🧮

A powerful Model Context Protocol (MCP) server that transforms AI assistants into mathematical powerhouses with 100% deterministic calculations.

## 🎯 Why This Exists

Small Large Language Models (LLMs) are excellent at generating text but struggle with precise mathematical calculations. They predict the next token, which often leads to "hallucinated" answers for complex computations. This MCP server solves that problem by giving AI assistants access to a reliable calculator that computes accurate answers instead of guessing.

**The Solution:** Instead of asking the AI to guess mathematical answers, we provide it with a Calculator (this Server) so it can compute the answer with precision.

## ✨ Features

This server provides 30+ mathematical tools across 8 categories:

### 1. **Basic Arithmetic**
- Addition, Subtraction, Multiplication, Division
- Modulo operations
- Power calculations

### 2. **Advanced Mathematics**
- Square root
- Logarithms (natural, base-10, custom base)

### 3. **Number Theory**
- Factorial
- Greatest Common Divisor (GCD)
- Least Common Multiple (LCM)

### 4. **Trigonometry**
- Sine, Cosine, Tangent
- Degree ↔ Radian conversion

### 5. **Statistics**
- Mean (average)
- Median
- Standard Deviation
- Variance

### 6. **Geometry**
- Hypotenuse calculation
- Circle area
- 2D Euclidean distance

### 7. **Advanced Distance Metrics**
- 3D Euclidean distance
- Manhattan distance (n-dimensional)
- Absolute difference

### 8. **Utilities**
- Absolute value
- Floor, Ceiling, Rounding
- Random number generation
- Mathematical constants (π, e)

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended for speed)

### Installation

```bash
# Install uv (if not already installed)
pip install uv

# Clone the repository
git clone <your-repo-url>
cd Unified-Math-Local-MCP-Server

# Install dependencies
uv add fastmcp
```

### Running the Server

```bash
# Start the server
uv run python main.py
```

## 🧪 Testing with FastMCP Inspector

Before connecting to an AI client, test your tools using the built-in Inspector:

```bash
uv run fastmcp dev main.py
```

This opens an interactive interface where you can:
- View all available tools
- Test each tool with sample inputs
- See JSON-RPC messages in real-time
- Verify outputs before production use

## 🔗 Connecting to Claude Desktop

### Automatic Installation

```bash
uv run fastmcp install claude-desktop main.py
```

### Manual Configuration

1. Find your `uv` path:
   ```bash
   which uv
   ```

2. Edit your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add the server configuration:
   ```json
   {
     "mcpServers": {
       "unified-math-server": {
         "command": "/path/to/uv",
         "args": ["run", "python", "/path/to/main.py"]
       }
     }
   }
   ```

4. Restart Claude Desktop

## 📖 Usage Examples

Once connected to Claude Desktop, you can use natural language:

**Example 1: Basic Calculation**
```
User: "Add 15, 27, and 33"
Assistant: [Calls add([15, 27, 33])]
Result: 75
```

**Example 2: Chain of Operations**
```
User: "I have a right triangle with sides 5 and 12. Calculate the hypotenuse, 
      then tell me the area of a circle with that radius."

Assistant Process:
1. Calls hypotenuse(5, 12) → 13.0
2. Calls circle_area(13.0) → 530.93
Final Answer: "The area of the circle is approximately 530.93 square units."
```

**Example 3: Statistics**
```
User: "Calculate the standard deviation of [10, 20, 30, 40, 50]"
Assistant: [Calls stdev([10, 20, 30, 40, 50])]
Result: 15.81
```

## 🏗️ Architecture & Design Philosophy

### Defensive Programming
The server includes helper functions (`_as_number`, `_as_list`) that sanitize inputs. AI models are non-deterministic and might pass strings like `" 42 "` instead of the integer `42`. This layer prevents crashes due to type errors.

### Atomic Tool Design
Instead of one monolithic `calculate()` function, we create specific tools for specific operations. This enables:
- **Chain of Thought Reasoning**: AI can break complex formulas into steps
- **Clear Error Messages**: Each tool can provide specific feedback
- **Better Discoverability**: AI can see exactly what operations are available

### Type Safety
We use Python type hints extensively. FastMCP automatically generates JSON schemas from these hints, making the code self-documenting.

## 🛠️ Technology Stack

| Technology | Purpose | Why? |
|------------|---------|------|
| **uv** | Package management | 10-100x faster than pip; instant virtual environment setup |
| **FastMCP** | MCP abstraction layer | Reduces boilerplate; FastAPI-like decorator syntax |
| **Python 3.10+** | Runtime | Native type hints; async/await support |

## 📚 Available Tools

For a complete list of tools with their signatures and descriptions, run the Inspector or check the [main.py](main.py) file. Each tool includes:
- Clear docstrings
- Type-safe parameters
- Comprehensive error handling
- Input validation

## 🔒 Security

MCP is designed with security in mind:
- **Permission-Based**: Claude Desktop asks for permission before executing tools
- **Local Execution**: All computations run on your machine
- **No Network Calls**: The server doesn't make external requests
- **Sandboxed**: FastMCP handles input validation and error isolation

## 🤝 Contributing

Contributions are welcome! To add new mathematical tools:

1. Fork the repository
2. Add your tool function with the `@mcp.tool` decorator
3. Include proper type hints and docstrings
4. Test using the FastMCP Inspector
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp) by @jlowin
- Powered by [Anthropic's Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- Package management by [uv](https://github.com/astral-sh/uv)

## 📖 Learn More

Read the full tutorial series on Medium:
- **Part 1**: Why the era of isolated AI is ending
- **Part 2**: Understanding MCP architecture
- **Part 3**: Building this Unified Math Server
- **Part 4**: Building Remote MCP servers

---

**Found this helpful?** ⭐ Star this repo and share your feedback!

**Questions?** Open an issue or reach out on [your social media/contact]
