```
 █████╗ ██╗   ██╗██████╗  █████╗ 
██╔══██╗██║   ██║██╔══██╗██╔══██╗
███████║██║   ██║██████╔╝███████║
██╔══██║██║   ██║██╔══██╗██╔══██║
██║  ██║╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝


██╗    ██╗██╗  ██╗███████╗██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗    ███████╗
██║    ██║██║  ██║██╔════╝██╔══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║    ╚══███╔╝
██║ █╗ ██║███████║█████╗  ██████╔╝█████╗      ██║  ███╗█████╗  ██╔██╗ ██║      ███╔╝ 
██║███╗██║██╔══██║██╔══╝  ██╔══██╗██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║     ███╔╝  
╚███╔███╔╝██║  ██║███████╗██║  ██║███████╗    ╚██████╔╝███████╗██║ ╚████║    ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝

███╗   ███╗███████╗███████╗████████╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
████╗ ████║██╔════╝██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██╔████╔██║█████╗  █████╗     ██║   ███████╗    ██║     ██║   ██║██║  ██║█████╗  
██║╚██╔╝██║██╔══╝  ██╔══╝     ██║   ╚════██║    ██║     ██║   ██║██║  ██║██╔══╝  
██║ ╚═╝ ██║███████╗███████╗   ██║   ███████║    ╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
```

# AURA Programming Language

**AURA** is a Gen Z-inspired esoteric programming language that combines modern internet culture with programming concepts. Every keyword is designed to reflect contemporary slang and expressions, making coding both fun and expressive.

## Features

- **Gen Z Syntax**: Keywords like `rizz`, `slay`, `bet`, `no-cap`, `vibes` and more
- **Mathematical Operations**: Comprehensive math functions including square root, random numbers, and basic arithmetic
- **Array Support**: Create and manipulate arrays with `squad` commands
- **Functions**: Define and call custom functions with `bet` and `no-cap`
- **Control Flow**: Loops, conditionals, and control structures
- **Special Commands**: Built-in commands for motivation, compliments, and aesthetic output
- **Web Editor**: Modern web interface with syntax highlighting and live examples
- **Debug Mode**: Enhanced error reporting and execution tracking
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation and Setup

### Requirements
- Python 3.7 or higher
- Flask (for web editor functionality)

### Installation
```bash
# Clone or download the project
cd aura-esolang

# Install dependencies (optional, for web editor)
pip install flask

# Verify installation
python aura.py --version
```

### Running AURA Programs

#### Command Line Interface
```bash
# Run an AURA program
python aura.py example.aura

# Run with debug mode for detailed output
python aura.py example.aura --debug

# Show version information
python aura.py --version
```

#### Web Editor
```bash
# Start the web server
python aura_web.py

# Open your browser to http://localhost:5000
```

## Language Reference

### Variables and Assignment
```aura
aura x = 10          # Declare and initialize variable
gyatt y = 20         # Assign value to variable
maincharacter x      # Protect variable from deletion
```

### Output Commands
```aura
rizz "Hello World!"      # Basic output
slay "Hot content!"      # Output with [SLAY] prefix
periodt "Statement!"     # Output with [PERIODT] prefix
vibes "Good energy!"     # Output with [VIBES] prefix
```

### Input
```aura
vibe name               # Get user input and store in variable
```

### Mathematical Operations
```aura
slay a b        # Addition (a + b)
cap a b         # Subtraction (a - b)
drip a b        # Multiplication (a * b)
sus a b         # Division (a / b)
mod a b         # Modulo (a % b)
power a b       # Power (a ^ b)
sqrt n          # Square root
abs n           # Absolute value
random a b      # Random number between a and b
min a b         # Minimum of two values
max a b         # Maximum of two values
```

### Comparison Operators
```aura
flex a b        # Equal (a == b)
shade a b       # Not equal (a != b)
bigger a b      # Greater than (a > b)
smaller a b     # Less than (a < b)
bigflex a b     # Greater or equal (a >= b)
smallflex a b   # Less or equal (a <= b)
```

### Logical Operators
```aura
and a b         # Logical AND
or a b          # Logical OR
not a           # Logical NOT
lit             # True (1)
cap             # False (0)
```

### Arrays (Squad Operations)
```aura
squad numbers = [1, 2, 3, 4, 5]    # Create array
squadget numbers 0                  # Get element at index
squadset numbers 0 10               # Set element at index
squadpush numbers 6                 # Add element to end
squadpop numbers                    # Remove last element
squadlen numbers                    # Get array length
```

### Control Flow

#### Loops
```aura
# Basic loop with counter
loop 5
  rizz "Hello!"
  rizz loopindex    # Built-in loop counter (0-based)
endloop

# While loop
aura x = 0
whileloop smaller x 5
  rizz x
  rizzup x
endwhileloop
```

#### Conditionals
```aura
# If statement
betif bigger x 10
  rizz "x is big!"
nobet

# If not statement
susif flex x 0
  rizz "x is not zero!"
nosus
```

### Functions
```aura
# Define function
bet greet(name, age)
  slay "Hello!"
  rizz name
  rizz age
no-cap

# Call function
bet greet("Alice", 25)
```

### Variable Operations
```aura
rizzup x            # Increment variable (x++)
gyattdown x         # Decrement variable (x--)
ghost x             # Delete variable
vibecheck           # Show all variables
```

### Special Commands
```aura
compliment          # Display random compliment
motivation          # Display motivational quote
aesthetic           # Display aesthetic message
help                # Show help information
exit                # Quit program
```

## Example Programs

### Hello World
```aura
slay "Hello World!"
periodt "Welcome to AURA!"
motivation
exit
```

### Variables and Math
```aura
aura x = 10
aura y = 5
maincharacter x

slay "Math Operations:"
rizz slay x y    # Addition: 15
rizz cap x y     # Subtraction: 5
rizz drip x y    # Multiplication: 50
rizz sus x y     # Division: 2

vibecheck
exit
```

### Arrays and Loops
```aura
squad numbers = [1, 2, 3, 4, 5]
slay "Array contents:"
rizz numbers

slay "Processing elements:"
loop 5
  rizz "Index"
  rizz loopindex
  rizz ":"
  rizz squadget numbers loopindex
endloop

exit
```

### Functions
```aura
bet greet(name)
  slay "Hello there,"
  rizz name
  periodt "Welcome to AURA!"
no-cap

bet calculate(a, b)
  aura result = slay a b
  rizz "Result:"
  rizz result
no-cap

# Function calls
bet greet("AURA User")
bet calculate(10, 5)
exit
```

### Conditionals and Logic
```aura
aura age = 18
aura name = "Alex"

slay "Age verification:"
betif bigflex age 18
  periodt "Access granted!"
nobet

susif smaller age 13
  slay "Too young for this content"
nosus

vibecheck
exit
```

### Complete Example
```aura
# Complete AURA program demonstration
slay "Welcome to AURA Programming Language"

# Variable declarations
aura username = "CodeMaster"
aura score = 0
maincharacter username

# Array operations
squad achievements = ["First Program", "Loop Master", "Function Creator"]
slay "Current achievements:"
rizz achievements

# Mathematical operations
aura points = random 50 100
aura bonus = drip points 2
gyatt score = slay score points bonus

# Conditional logic
betif bigger score 200
  slay "High score achieved!"
  compliment
nobet

# Function definition
bet displayStats(user, points)
  slay "Player Stats:"
  rizz user
  rizz points
  aesthetic
no-cap

# Function call
bet displayStats(username, score)

# Loop demonstration
slay "Countdown:"
loop 5
  aura remaining = cap 5 loopindex
  rizz remaining
endloop

slay "Program completed successfully!"
exit
```

## Web Editor

The AURA Web Editor provides a modern, interactive development environment with the following features:

### Features
- **Syntax Highlighting**: Color-coded syntax for better readability
- **Live Examples**: Pre-loaded example programs to get started quickly
- **Interactive Execution**: Run code directly in the browser
- **Error Reporting**: Clear error messages and debugging information
- **Line Numbers**: Easy navigation and reference
- **Responsive Design**: Works on desktop and mobile devices

### Usage
1. Start the web server: `python aura_web.py`
2. Open your browser to `http://localhost:5000`
3. Choose from example programs or write your own code
4. Click "Execute Code" to run your program
5. View results in the output panel

### Available Examples
- **Hello World**: Basic AURA greeting and output
- **Variables Demo**: Working with variables and assignments
- **Math Operations**: Mathematical functions and calculations
- **Squad Operations**: Array creation and manipulation

## Error Handling

AURA uses a consistent error reporting system with "skill issue" messages:

```
skill issue: undefined variable: x
skill issue: can't sus by zero
skill issue: expected =
skill issue: array numbers not found
```

### Debug Mode
Enable debug mode for detailed execution information:
```bash
python aura.py example.aura --debug
```

Debug mode provides:
- Line-by-line execution tracking
- Variable state information
- Enhanced error context
- Execution statistics

## File Structure

```
aura-esolang/
├── aura.py              # Main interpreter
├── aura_web.py          # Web server and API
├── web_editor.html      # Web interface
├── example.aura         # Example program
├── example_clean.aura   # Clean example
├── test_suite.aura      # Test cases
├── simple_test.aura     # Simple test
├── demo.aura            # Demo program
├── launcher.bat         # Windows launcher
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
└── LICENSE              # License file
```

## API Reference

The web server provides REST API endpoints:

### POST /run_aura
Execute AURA code
```json
{
  "code": "slay \"Hello World!\"\nexit"
}
```

Response:
```json
{
  "output": "AURA Execution Results:\n[SLAY] Hello World!\naura out! Thanks for vibing with us!"
}
```

### GET /stats
Get execution statistics
```json
{
  "total_runs": 42,
  "successful_runs": 40,
  "failed_runs": 2,
  "success_rate": "95.2%",
  "runtime": "1234.5s",
  "server_status": "running"
}
```

### GET /help
Get command reference
```json
{
  "variables": {
    "aura var = value": "Declare a variable",
    "gyatt var = value": "Assign to a variable"
  },
  "output": {
    "rizz value": "Basic output",
    "slay value": "Output with [SLAY] prefix"
  }
}
```

### GET /health
Health check endpoint
```json
{
  "status": "healthy",
  "timestamp": "2025-07-11T10:30:00",
  "version": "AURA v2.0"
}
```

## Development and Contributing

### Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd aura-esolang

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python aura.py test_suite.aura
```

### Project Structure
The codebase is organized as follows:
- `aura.py`: Core interpreter with lexer, parser, and runtime
- `aura_web.py`: Flask web server and API endpoints
- `web_editor.html`: Frontend web interface
- `*.aura`: Example programs and test cases

### Contributing Guidelines
Contributions are welcome! Here's how to contribute:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes**: Add new features, fix bugs, or improve documentation
4. **Test thoroughly**: Ensure all existing tests pass and add new tests
5. **Submit a pull request**: Describe your changes and their benefits

### Adding New Features
When adding new AURA commands:
1. Add the command to the `exec_line` method in `aura.py`
2. Add expression support to `eval_expr` if needed
3. Update the help system and documentation
4. Add test cases to verify functionality
5. Update the web editor examples if relevant

## Troubleshooting

### Common Issues

**Command not found errors**
- Ensure you're using Python 3.7+
- Check that all required files are in the same directory
- Verify the command spelling matches AURA syntax

**Web editor not loading**
- Confirm Flask is installed: `pip install flask`
- Check that port 5000 is available
- Ensure `aura_web.py` and `web_editor.html` are in the same directory

**Skill issue messages**
- Enable debug mode for detailed error information
- Check variable names and syntax
- Verify that arrays are properly initialized before use

**Performance issues**
- Avoid infinite loops in `whileloop` constructs
- Use reasonable array sizes for better performance
- Consider using debug mode only when needed

### Getting Help
- Check the built-in help: Add `help` to your AURA program
- Review example programs in the repository
- Enable debug mode for detailed execution information
- Check the web editor for interactive examples

## License

MIT License

Copyright (c) 2025 AURA Development Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**AURA Programming Language** - Where Gen Z meets code. No cap, this language is absolutely iconic!