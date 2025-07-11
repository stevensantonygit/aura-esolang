# Flask backend for AURA Web Editor

from flask import Flask, request, jsonify, send_from_directory
import tempfile
import subprocess
import os
import sys
import time
import json
from datetime import datetime

app = Flask(__name__)

stats = {
    'total_runs': 0,
    'successful_runs': 0,
    'failed_runs': 0,
    'start_time': time.time()
}

@app.route('/run_aura', methods=['POST'])
def run_aura():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code.strip():
            return jsonify({'output': 'No code provided'})
        
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.aura', encoding='utf-8') as f:
            f.write(code)
            fname = f.name
        
        try:
            result = subprocess.run([
                sys.executable, 
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aura.py'), 
                fname
            ], capture_output=True, text=True, timeout=15, encoding='utf-8')
            
            output = result.stdout
            if result.stderr:
                output += "\n" + result.stderr
                
            stats['total_runs'] += 1
            if result.returncode == 0:
                stats['successful_runs'] += 1
            else:
                stats['failed_runs'] += 1
            
            if output:
                output = f"AURA Execution Results:\n{output}"
            else:
                output = "Code executed successfully (no output)"
                
        except subprocess.TimeoutExpired:
            output = "Execution timeout: Your code took too long to run (15s limit)"
            stats['total_runs'] += 1
            stats['failed_runs'] += 1
        except Exception as e:
            output = f"skill issue: {str(e)}"
            stats['total_runs'] += 1
            stats['failed_runs'] += 1
        finally:
            try:
                os.remove(fname)
            except:
                pass
                
        return jsonify({'output': output})
        
    except Exception as e:
        return jsonify({'output': f'Server skill issue: {str(e)}'})

@app.route('/stats', methods=['GET'])
def get_stats():
    runtime = time.time() - stats['start_time']
    return jsonify({
        'total_runs': stats['total_runs'],
        'successful_runs': stats['successful_runs'],
        'failed_runs': stats['failed_runs'],
        'success_rate': f"{(stats['successful_runs'] / max(stats['total_runs'], 1)) * 100:.1f}%",
        'runtime': f"{runtime:.1f}s",
        'server_status': 'running'
    })

@app.route('/validate', methods=['POST'])
def validate_code():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        lines = code.strip().split('\n')
        errors = []
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if line.startswith('aura ') or line.startswith('gyatt '):
                if ' = ' not in line:
                    errors.append(f"Line {i}: Missing '=' in assignment")
            elif line.startswith('bet ') and '(' in line:
                if 'no-cap' not in code:
                    errors.append(f"Line {i}: Function missing 'no-cap' ending")
            elif line.startswith('loop '):
                if 'endloop' not in code:
                    errors.append(f"Line {i}: Loop missing 'endloop'")
        
        return jsonify({
            'valid': len(errors) == 0,
            'errors': errors,
            'line_count': len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        })
        
    except Exception as e:
        return jsonify({'valid': False, 'errors': [f'Validation error: {str(e)}']})

@app.route('/help', methods=['GET'])
def get_help():
    help_data = {
        'variables': {
            'aura var = value': 'Declare a variable',
            'gyatt var = value': 'Assign to a variable',
            'maincharacter var': 'Protect a variable from deletion'
        },
        'output': {
            'rizz value': 'Basic output',
            'slay value': 'Output with [SLAY] prefix',
            'periodt value': 'Output with [PERIODT] prefix',
            'vibes value': 'Output with [VIBES] prefix'
        },
        'input': {
            'vibe var': 'Get user input'
        },
        'math': {
            'slay a b': 'Add (a + b)',
            'cap a b': 'Subtract (a - b)',
            'drip a b': 'Multiply (a * b)',
            'sus a b': 'Divide (a / b)',
            'power a b': 'Power (a ^ b)',
            'sqrt n': 'Square root',
            'random a b': 'Random number between a and b'
        },
        'arrays': {
            'squad arr = [1,2,3]': 'Create array',
            'squadget arr index': 'Get array element',
            'squadset arr index val': 'Set array element',
            'squadpush arr val': 'Add to array',
            'squadpop arr': 'Remove from array'
        },
        'loops': {
            'loop n...endloop': 'Repeat n times',
            'whileloop cond...endwhileloop': 'While loop'
        },
        'conditionals': {
            'betif condition...nobet': 'If statement',
            'susif condition...nosus': 'If not statement'
        },
        'functions': {
            'bet name(params)...no-cap': 'Define function',
            'bet name(args)': 'Call function'
        },
        'special': {
            'compliment': 'Random compliment',
            'motivation': 'Motivational quote',
            'aesthetic': 'Aesthetic vibes',
            'vibecheck': 'Show all variables',
            'help': 'Show help',
            'exit': 'Quit program'
        }
    }
    return jsonify(help_data)

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'web_editor.html')

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': 'AURA v2.0'
    })

if __name__ == '__main__':
    print("Starting AURA Web Server...")
    print("Open http://localhost:5000 in your browser")
    print("Ready to serve some fire AURA code!")
    app.run(port=5000, debug=True, host='0.0.0.0')