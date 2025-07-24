# AURA Esolang Summary

## Overview

AURA is a Gen Z-inspired esoteric programming language where every keyword reflects internet culture and slang. The language combines humor with genuine programming functionality, making it both entertaining and capable of real computation.

## Core Features

### Variable Operations
- **aura var = value** - Variable declaration
- **gyatt var = value** - Variable assignment  
- **vibe var** - Get user input
- **ghost var** - Delete variable
**rizzup var** - Increment variable
- **gyattdown var** - Decrement variable
- **maincharacter var** - Set variable as main character (cannot be deleted)

### Enhanced Output Commands
- **slay "text"** - Output with [SLAY] prefix
- **periodt "text"** - Output with [PERIODT] prefix
- **vibes "text"** - Output with [VIBES] prefix

### Mathematical Operations
- **slay a b** - Addition (a + b)
- **cap a b** - Subtraction (a - b)
- **drip a b** - Multiplication (a * b)
- **sus a b** - Division (a / b)
- **mod a b** - Modulo (a % b)
- **power a b** - Exponentiation (a ^ b)

### Advanced Math Functions
- **sqrt n** - Square root
- **abs n** - Absolute value
- **floor n** - Floor function
- **ceil n** - Ceiling function
- **round n** - Round to nearest integer
- **sin n** - Sine function
- **cos n** - Cosine function
- **tan n** - Tangent function
- **log n** - Natural logarithm
- **random min max** - Random integer between min and max
- **min a b** - Minimum of two values
- **max a b** - Maximum of two values

### Comparison Operations
- **flex a b** - Equality (a == b)
- **shade a b** - Inequality (a != b)
- **bigger a b** - Greater than (a > b)
- **smaller a b** - Less than (a < b)
- **bigflex a b** - Greater than or equal (a >= b)
- **smallflex a b** - Less than or equal (a <= b)

### Logical Operations
- **and a b** - Logical AND
- **or a b** - Logical OR
- **not a** - Logical NOT
- **lit** - Boolean true (1)
- **false** - Boolean false (0)

### String Operations
- **length str** - Get string length
- **concat str1 str2** - Concatenate strings
- **upper str** - Convert to uppercase
- **lower str** - Convert to lowercase

### Array Operations
- **squad arr = [1, 2, 3]** - Create array
- **squadpush arr value** - Add element to array
- **squadpop arr** - Remove last element
- **squadget arr index** - Get element at index
- **squadset arr index value** - Set element at index
- **squadlen arr** - Get array length

### Control Flow

#### Conditionals
- **betif condition** ... **nobet** - If statement
- **susif condition** ... **nosus** - If not statement

#### Loops
- **loop count** ... **endloop** - Fixed iteration loop
- **whileloop condition** ... **endwhileloop** - While loop
- **loopindex** - Built-in counter variable in loops

#### Functions
- **bet funcname (params)** ... **no-cap** - Function definition
- **bet funcname (args)** - Function call

### Special Operations
- **ratio a b** - Division with meme output if b > a
- **simp var value** - Set variable to value if current value is lower
- **clout var** - Double the variable value
- **cancel var** - Set variable to zero
- **manifest var value** - Create variable only if it doesn't exist
- **vibeflip var** - Negate variable value
- **glowup var** - Square the variable value
- **spill var** - Print and delete variable
- **trend var** - Display variable with random trending phrase

### Date and Time Functions
- **time** - Current Unix timestamp
- **year** - Current year
- **month** - Current month
- **day** - Current day
- **hour** - Current hour
- **minute** - Current minute
- **second** - Current second

### Utility Commands
- **dripcheck var** - Check if variable is truthy
- **vibecheck** - Display all variables and arrays
- **compliment** - Display random compliment
- **motivation** - Display motivational quote
- **aesthetic** - Display aesthetic phrase
- **debug** - Toggle debug mode
- **save filename** - Save program state to JSON
- **load filename** - Load program state from JSON
- **clear** - Clear screen
- **clear all** - Clear all variables
- **help** - Show command reference
- **exit** - Exit program

### Error Handling
All errors are reported as "skill issue" messages with descriptive information about what went wrong.

## Language Characteristics

### Syntax Rules
- All keywords are lowercase
- Strings must be enclosed in double quotes
- Comments start with # or //
- Case-sensitive variable names
- Whitespace-separated tokens

### Data Types
- Integers
- Floating-point numbers
- Strings
- Arrays (mixed types supported)
- Booleans (represented as 1/0)

### Execution Model
- Interpreted line by line
- Dynamic typing
- Automatic type conversion where appropriate
- Built-in execution tracking and performance monitoring

## File Structure
- **.aura** - Source code files
- **aura.py** - Main interpreter
- **aura_web.py** - Web server for browser-based execution
- **web_editor.html** - Web interface
- **launcher.bat** - Windows launcher script

## Technical Implementation
- Written in Python 3
- UTF-8 encoding support
- JSON state persistence
- Command-line argument parsing
- Debug mode with execution tracing
- Error handling with stack traces in debug mode

## Design Philosophy
AURA combines internet culture with practical programming concepts. While the syntax is humorous and culturally relevant, the language provides genuine computational capabilities including variables, functions, loops, conditionals, arrays, and mathematical operations. The goal is to make programming both entertaining and educational while maintaining the aesthetic of Gen Z internet culture.
## Example Programs

### Basic Example
```aura
aura x = 10
aura y = 5
maincharacter x
slay "Welcome to AURA!"
vibes slay x y
betif bigger x y
  periodt "x is bigger than y!"
nobet
```

### Array Example
```aura
squad numbers = [1, 2, 3, 4, 5]
squadpush numbers 6
vibes numbers
loop 3
  vibes loopindex
endloop
```

### Function Example
```aura
bet calculate (a, b)
  vibes slay a b
  vibes cap a b
no-cap

bet calculate (10, 5)
```

## Command Line Usage
```bash
py aura.py filename.aura          # Run program
py aura.py filename.aura --debug  # Run with debug mode
py aura.py --version              # Show version
py aura_web.py                    # Start web server
```

## Web Interface
The language includes a web-based editor accessible via the built-in web server. Features include:
- Syntax highlighting
- Live code execution
- Example programs
- Command reference
- Error reporting
- Mobile-responsive design

AURA represents a unique approach to esoteric programming languages by combining internet culture with genuine programming functionality, making it both entertaining and educational for users familiar with Gen Z terminology and memes.