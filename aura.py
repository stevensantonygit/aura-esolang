import math
import random
import time
import sys
import json
import os
from datetime import datetime

# AURA: The Gen Z Esolang

class AuraInterpreter:
    def exec_line(self, line):
        tokens = line.split()
        if not tokens:
            return
        cmd = tokens[0]
        if cmd in ('aura', 'gyatt') and len(tokens) >= 4 and tokens[2] == '=':
            var = tokens[1]
            expr = ' '.join(tokens[3:])
            self.vars[var] = self.eval_expr(expr)
            return
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.lines = []
        self.line_num = 0
        self.total_lines_executed = 0
        self.main_character = None
        self.debug_mode = False
        self.execution_start_time = None
        self.compliment_phrases = [
            "You're the main character!",
            "Living your best life!",
            "That's iconic behavior!",
            "You're glowing up!",
            "Pure main character energy!",
            "That's a whole mood!"
        ]

    def parse(self, code):
        processed_lines = []
        for line in code.strip().split('\n'):
            if '#' in line:
                line = line.split('#')[0]
            if '//' in line:
                line = line.split('//')[0]
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('//'):
                processed_lines.append(line)
        self.lines = processed_lines
        self.line_num = 0

    def eval_expr(self, expr):
        tokens = self.tokenize(expr)
        if not tokens:
            return None
        
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        
        if tokens[0] == 'slay':
            return self.get_value(tokens[1]) + self.get_value(tokens[2])
        elif tokens[0] == 'cap':
            return self.get_value(tokens[1]) - self.get_value(tokens[2])
        elif tokens[0] == 'drip':
            return self.get_value(tokens[1]) * self.get_value(tokens[2])
        elif tokens[0] == 'sus':
            b = self.get_value(tokens[2])
            if b == 0:
                self.skill_issue("can't sus by zero")
            return self.get_value(tokens[1]) / b
        elif tokens[0] == 'mod':
            return self.get_value(tokens[1]) % self.get_value(tokens[2])
        elif tokens[0] == 'power':
            return self.get_value(tokens[1]) ** self.get_value(tokens[2])
        
        elif tokens[0] == 'flex':
            return int(self.get_value(tokens[1]) == self.get_value(tokens[2]))
        elif tokens[0] == 'shade':
            return int(self.get_value(tokens[1]) != self.get_value(tokens[2]))
        elif tokens[0] == 'bigger':
            return int(self.get_value(tokens[1]) > self.get_value(tokens[2]))
        elif tokens[0] == 'smaller':
            return int(self.get_value(tokens[1]) < self.get_value(tokens[2]))
        elif tokens[0] == 'bigflex':
            return int(self.get_value(tokens[1]) >= self.get_value(tokens[2]))
        elif tokens[0] == 'smallflex':
            return int(self.get_value(tokens[1]) <= self.get_value(tokens[2]))
        
        elif tokens[0] == 'and':
            return int(self.get_value(tokens[1]) and self.get_value(tokens[2]))
        elif tokens[0] == 'or':
            return int(self.get_value(tokens[1]) or self.get_value(tokens[2]))
        elif tokens[0] == 'not':
            return int(not self.get_value(tokens[1]))
        
        elif tokens[0] == 'lit':
            return 1
        elif tokens[0] == 'false':
            return 0
        
        elif tokens[0] == 'sqrt':
            return math.sqrt(self.get_value(tokens[1]))
        elif tokens[0] == 'abs':
            return abs(self.get_value(tokens[1]))
        elif tokens[0] == 'floor':
            return math.floor(self.get_value(tokens[1]))
        elif tokens[0] == 'ceil':
            return math.ceil(self.get_value(tokens[1]))
        elif tokens[0] == 'round':
            return round(self.get_value(tokens[1]))
        elif tokens[0] == 'sin':
            return math.sin(self.get_value(tokens[1]))
        elif tokens[0] == 'cos':
            return math.cos(self.get_value(tokens[1]))
        elif tokens[0] == 'tan':
            return math.tan(self.get_value(tokens[1]))
        elif tokens[0] == 'log':
            return math.log(self.get_value(tokens[1]))
        elif tokens[0] == 'random':
            a = self.get_value(tokens[1])
            b = self.get_value(tokens[2])
            try:
                a = int(a)
                b = int(b)
            except Exception:
                self.skill_issue("random arguments must be integers")
            if a > b:
                a, b = b, a
            return random.randint(a, b)
        elif tokens[0] == 'min':
            return min(self.get_value(tokens[1]), self.get_value(tokens[2]))
        elif tokens[0] == 'max':
            return max(self.get_value(tokens[1]), self.get_value(tokens[2]))
        
        elif tokens[0] == 'length':
            return len(str(self.get_value(tokens[1])))
        elif tokens[0] == 'concat':
            if len(tokens) >= 3:
                str1 = self.get_value(tokens[1])
                str2 = self.get_value(tokens[2])
                return str(str1) + str(str2)
            else:
                self.skill_issue("concat requires two arguments")
        elif tokens[0] == 'upper':
            return str(self.get_value(tokens[1])).upper()
        elif tokens[0] == 'lower':
            return str(self.get_value(tokens[1])).lower()

        elif tokens[0] == 'ratio':
            a = self.get_value(tokens[1])
            b = self.get_value(tokens[2])
            if b > a:
                print(f"{a} got ratio'd by {b} - That's embarrassing!")
                return None
            return a / b
        elif tokens[0] == 'simp':
            name = tokens[1]
            value = self.get_value(tokens[2])
            if name in self.vars and self.vars[name] < value:
                self.vars[name] = value
            return self.vars.get(name, value)
        elif tokens[0] == 'clout':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] *= 2
                return self.vars[name]
            else:
                self.skill_issue(f"can't clout {name}, not found")
        elif tokens[0] == 'cancel':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] = 0
                return 0
            else:
                self.skill_issue(f"can't cancel {name}, not found")
        elif tokens[0] == 'manifest':
            name = tokens[1]
            value = self.get_value(tokens[2])
            if name not in self.vars:
                self.vars[name] = value
            return self.vars[name]
        elif tokens[0] == 'vibeflip':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] = -self.vars[name]
                return self.vars[name]
            else:
                self.skill_issue(f"can't vibeflip {name}, not found")
        elif tokens[0] == 'squad':
            return self.get_value(tokens[1]) + self.get_value(tokens[2]) + self.get_value(tokens[3])
        elif tokens[0] == 'glowup':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] = self.vars[name] ** 2
                return self.vars[name]
            else:
                self.skill_issue(f"can't glowup {name}, not found")
        elif tokens[0] == 'spill':
            name = tokens[1]
            if name in self.vars:
                val = self.vars[name]
                print(f"Spilling the tea on {name}: {val}")
                del self.vars[name]
                return val
            else:
                self.skill_issue(f"can't spill {name}, not found")
        elif tokens[0] == 'pause':
            n = self.get_value(tokens[1])
            time.sleep(n)
            return None
        elif tokens[0] == 'trend':
            name = tokens[1]
            if name in self.vars:
                phrase = random.choice(self.trend_phrases)
                print(f"{name} ({self.vars[name]}) {phrase}")
                return self.vars[name]
            else:
                self.skill_issue(f"can't trend {name}, not found")
        elif tokens[0] == 'time':
            return int(time.time())
        elif tokens[0] == 'year':
            return datetime.now().year
        elif tokens[0] == 'month':
            return datetime.now().month
        elif tokens[0] == 'day':
            return datetime.now().day
        elif tokens[0] == 'hour':
            return datetime.now().hour
        elif tokens[0] == 'minute':
            return datetime.now().minute
        elif tokens[0] == 'second':
            return datetime.now().second
        
        elif tokens[0].replace('.', '', 1).isdigit() or (tokens[0][0] == '-' and tokens[0][1:].replace('.', '', 1).isdigit()):
            return float(tokens[0]) if '.' in tokens[0] else int(tokens[0])
        elif tokens[0] in self.vars:
            return self.vars[tokens[0]]
        else:
            self.skill_issue(f"undefined variable or bad expr: {tokens[0]}")

    def get_value(self, token):
        if token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        if token.replace('.', '', 1).isdigit() or (token[0] == '-' and token[1:].replace('.', '', 1).isdigit()):
            return float(token) if '.' in token else int(token)
        if token in self.vars:
            return self.vars[token]
        self.skill_issue(f"undefined variable: {token}")

    def skill_issue(self, msg):
        print(f"skill issue: {msg}")
        if self.debug_mode:
            print(f"Debug: Line {self.line_num + 1}")
            print(f"Debug: Variables: {self.vars}")
        sys.exit(1)

    def log_execution(self, line):
        self.total_lines_executed += 1
        if self.debug_mode:
            print(f"Debug: Executing line {self.line_num + 1}: {line}")

    def run(self, code):
        self.execution_start_time = time.time()
        self.parse(code)
        print("AURA interpreter starting...")
        self.line_num = 0
        while self.line_num < len(self.lines):
            line = self.lines[self.line_num]
            self.log_execution(line)
            result = self.exec_line(line)
            if result == 'skip_increment':
                continue
            self.line_num += 1
        execution_time = time.time() - self.execution_start_time
        print(f"\nProgram completed in {execution_time:.3f}s")
        print(f"Total lines executed: {self.total_lines_executed}")
        if self.main_character:
            print(f"Main character: {self.main_character}")
        print("That's a wrap! No cap!")

    def exec_line(self, line):
        tokens = line.split()
        if not tokens:
            return
        cmd = tokens[0]
        
        if cmd in ('aura', 'gyatt') and len(tokens) >= 4 and tokens[2] == '=':
            var = tokens[1]
            expr = ' '.join(tokens[3:])
            self.vars[var] = self.eval_expr(expr)
            return
        if cmd == 'bet':
            if '(' in line and ')' in line and (self.line_num + 1 < len(self.lines)) and self.lines[self.line_num + 1] != 'no-cap':
                name = line.split('(',1)[0].split()[1]
                params_str = line[line.index('(')+1:line.index(')')]
                params = [p.strip() for p in params_str.split(',') if p.strip()]
                body = []
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'no-cap':
                    body.append(self.lines[self.line_num])
                    self.line_num += 1
                self.functions[name] = (params, body)
                if self.line_num < len(self.lines) and self.lines[self.line_num] == 'no-cap':
                    self.line_num += 1
                return 'skip_increment'
            elif '(' in line and ')' in line:
                name = line.split('(',1)[0].split()[1]
                args_str = line[line.index('(')+1:line.index(')')]
                args = [a.strip() for a in args_str.split(',') if a.strip()]
                if name not in self.functions:
                    self.skill_issue(f'no such function: {name}')
                params, body = self.functions[name]
                if len(params) != len(args):
                    self.skill_issue('argument count mismatch')
                old_vars = self.vars.copy()
                for p, a in zip(params, args):
                    if a.startswith('"') and a.endswith('"'):
                        self.vars[p] = a[1:-1]
                    elif a.replace('.', '', 1).isdigit() or (a.startswith('-') and a[1:].replace('.', '', 1).isdigit()):
                        self.vars[p] = float(a) if '.' in a else int(a)
                    else:
                        self.vars[p] = self.get_value(a)
                for bline in body:
                    self.exec_line(bline)
                self.vars = old_vars
                return
        elif cmd == 'ghost':
            name = tokens[1]
            if self.main_character == name:
                self.skill_issue(f"can't ghost the main character {name}")
            if name in self.vars:
                print(f"{name} has been ghosted")
                del self.vars[name]
            else:
                self.skill_issue(f"can't ghost {name}, not found")
        elif cmd == 'rizzup':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] += 1
                print(f"{name} rizzed up to {self.vars[name]}")
            else:
                self.skill_issue(f"can't rizzup {name}, not found")
        elif cmd == 'gyattdown':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] -= 1
                print(f"{name} gyatt down to {self.vars[name]}")
            else:
                self.skill_issue(f"can't gyattdown {name}, not found")
        elif cmd == 'vibecheck':
            print("Current aura:")
            for k, v in self.vars.items():
                if k != 'loopindex':
                    print(f"  {k}: {v}")
        elif cmd == 'maincharacter':
            name = tokens[1]
            self.main_character = name
            print(f"{name} is now the main character!")
        elif cmd == 'compliment':
            phrase = random.choice(self.compliment_phrases)
            print(f"{phrase}")
        elif cmd == 'motivation':
            motivational_quotes = [
                "You're absolutely slaying today!",
                "Main character energy activated!",
                "You're literally glowing up!",
                "That's iconic behavior!",
                "You're living your best life!",
                "Main character energy is immaculate!",
                "You're the moment!",
                "Your vibe is unmatched!",
                "You're a certified gem!",
                "You're absolutely sending me (in the best way)!"
            ]
            print(random.choice(motivational_quotes))
        elif cmd == 'aesthetic':
            aesthetics = [
                "soft girl vibes",
                "dark academia energy",
                "beach day mood",
                "cottagecore dreams",
                "ethereal night vibes",
                "edgy main character",
                "rainbow unicorn energy",
                "kawaii princess mode"
            ]
            print(random.choice(aesthetics))
        elif cmd == 'debug':
            self.debug_mode = not self.debug_mode
            status = "ON" if self.debug_mode else "OFF"
            print(f"Debug mode: {status}")
        elif cmd == 'save':
            filename = tokens[1] if len(tokens) > 1 else "aura_save.json"
            save_data = {
                'vars': self.vars,
                'main_character': self.main_character
            }
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=2)
            print(f"State saved to {filename}")
        elif cmd == 'load':
            filename = tokens[1] if len(tokens) > 1 else "aura_save.json"
            try:
                with open(filename, 'r') as f:
                    save_data = json.load(f)
                self.vars = save_data.get('vars', {})
                self.main_character = save_data.get('main_character')
                print(f"State loaded from {filename}")
            except FileNotFoundError:
                self.skill_issue(f"save file {filename} not found")
        elif cmd == 'clear':
            if len(tokens) > 1 and tokens[1] == 'all':
                self.vars.clear()
                self.main_character = None
                print("All variables cleared")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd == 'help':
            print("AURA Commands:")
            print("  aura/gyatt var = value - declare/assign variable")
            print("  rizz/slay/periodt/vibes - output with style")
            print("  vibe var - get input")
            print("  loop n...endloop - basic loop")
            print("  whileloop condition...endwhileloop - while loop")
            print("  betif/susif condition - conditionals")
            print("  bet func(params)...no-cap - define function")
            print("  ghost var - delete variable")
            print("  rizzup/gyattdown var - increment/decrement")
            print("  vibecheck - show all variables")
            print("  maincharacter var - set main character")
            print("  compliment/motivation/aesthetic - random positivity")
            print("  debug - toggle debug mode")
            print("  save/load filename - save/load state")
            print("  clear [all] - clear screen or variables")
            print("  exit - quit program")
        elif cmd == 'exit':
            print('aura out! Thanks for vibing with us!')
            sys.exit(0)

        elif cmd in ['vibes', 'periodt', 'rizz']:
            if len(tokens) > 1 and tokens[1] in [
                'slay', 'cap', 'drip', 'sus', 'mod', 'power',
                'flex', 'shade', 'bigger', 'smaller', 'bigflex', 'smallflex',
                'and', 'or', 'not', 'min', 'max', 'ratio', 'simp', 'clout', 'cancel',
                'manifest', 'vibeflip', 'squad', 'glowup', 'spill', 'pause', 'trend',
                'time', 'year', 'month', 'day', 'hour', 'minute', 'second',
                'sqrt', 'abs', 'floor', 'ceil', 'round', 'sin', 'cos', 'tan', 'log', 'random',
                'length', 'concat', 'upper', 'lower', 'lit', 'false']:
                try:
                    result = self.eval_expr(' '.join(tokens[1:]))
                    print(f"[{cmd.upper()}] {result}")
                except Exception:
                    self.skill_issue(f'cannot {cmd} {' '.join(tokens[1:])}')
            else:
                output_parts = []
                for arg in tokens[1:]:
                    if arg in self.vars:
                        output_parts.append(str(self.vars[arg]))
                    elif arg.startswith('"') and arg.endswith('"'):
                        output_parts.append(arg[1:-1])
                    else:
                        output_parts.append(arg)
                joined = ' '.join(output_parts)
                print(f"[{cmd.upper()}] {joined}")
        
        elif cmd == 'vibe':
            name = tokens[1]
            try:
                val = input(f"vibe for {name}: ")
                try:
                    self.vars[name] = int(val)
                except ValueError:
                    try:
                        self.vars[name] = float(val)
                    except ValueError:
                        self.vars[name] = val
            except Exception as e:
                self.skill_issue(f'input fail: {e}')
        
        
        elif cmd == 'loop':
            count = self.get_value(tokens[1])
            loop_body = []
            self.line_num += 1
            while self.line_num < len(self.lines) and self.lines[self.line_num] != 'endloop':
                loop_body.append(self.lines[self.line_num])
                self.line_num += 1
            for i in range(count):
                self.vars['loopindex'] = i
                for l in loop_body:
                    self.exec_line(l)
        elif cmd == 'endloop':
            pass
        
        elif cmd == 'whileloop':
            condition = ' '.join(tokens[1:])
            loop_body = []
            self.line_num += 1
            while self.line_num < len(self.lines) and self.lines[self.line_num] != 'endwhileloop':
                loop_body.append(self.lines[self.line_num])
                self.line_num += 1
            while self.eval_expr(condition):
                for l in loop_body:
                    self.exec_line(l)
        elif cmd == 'endwhileloop':
            pass
        
        elif cmd == 'bet':
            is_def = False
            if self.line_num + 1 < len(self.lines):
                next_line = self.lines[self.line_num + 1]
                if not (next_line.startswith('bet') and '(' in next_line and ')' in next_line):
                    is_def = True
            if is_def and self.line_num + 1 < len(self.lines):
                name = line.split('(',1)[0].split()[1]
                params_str = line[line.index('(')+1:line.index(')')]
                params = [p.strip() for p in params_str.split(',') if p.strip()]
                body = []
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'no-cap':
                    body.append(self.lines[self.line_num])
                    self.line_num += 1
                self.functions[name] = (params, body)
                if self.line_num < len(self.lines) and self.lines[self.line_num] == 'no-cap':
                    pass
            elif '(' in line and ')' in line:
                name = line.split('(',1)[0].split()[1]
                args_str = line[line.index('(')+1:line.index(')')]
                args = [a.strip() for a in args_str.split(',') if a.strip()]
                if name not in self.functions:
                    self.skill_issue(f'no such function: {name}')
                params, body = self.functions[name]
                if len(params) != len(args):
                    self.skill_issue('argument count mismatch')
                old_vars = self.vars.copy()
                for p, a in zip(params, args):
                    if a.startswith('"') and a.endswith('"'):
                        self.vars[p] = a[1:-1]
                    elif a.replace('.', '', 1).isdigit() or (a.startswith('-') and a[1:].replace('.', '', 1).isdigit()):
                        self.vars[p] = float(a) if '.' in a else int(a)
                    else:
                        self.vars[p] = self.get_value(a)
                print(f"DEBUG: vars after param assignment: {self.vars}")
                for bline in body:
                    print(f"DEBUG: vars before '{bline}': {self.vars}")
                    self.exec_line(bline)
                self.vars = old_vars
        
        elif cmd == 'betif':
            cond = self.eval_expr(' '.join(tokens[1:]))
            self.line_num += 1
            if cond:
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nobet':
                    self.exec_line(self.lines[self.line_num])
                    self.line_num += 1
                while self.line_num < len(self.lines):
                    if self.lines[self.line_num] == 'nobet':
                        self.line_num += 1
                        break
                    self.line_num += 1
                while self.line_num < len(self.lines):
                    if self.lines[self.line_num].startswith('susif'):
                        self.line_num += 1
                        while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nosus':
                            self.line_num += 1
                        if self.line_num < len(self.lines) and self.lines[self.line_num] == 'nosus':
                            self.line_num += 1
                        continue
                    break
                return 'skip_increment'
            else:
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nobet':
                    self.line_num += 1
                if self.line_num < len(self.lines) and self.lines[self.line_num] == 'nobet':
                    self.line_num += 1
        elif cmd == 'susif':
            cond = self.eval_expr(' '.join(tokens[1:]))
            self.line_num += 1
            if not cond:
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nosus':
                    self.exec_line(self.lines[self.line_num])
                    self.line_num += 1
                while self.line_num < len(self.lines):
                    if self.lines[self.line_num] == 'nosus':
                        self.line_num += 1
                        break
                    self.line_num += 1
                return 'skip_increment'
            else:
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nosus':
                    self.line_num += 1
                if self.line_num < len(self.lines) and self.lines[self.line_num] == 'nosus':
                    self.line_num += 1
        elif cmd == 'no-cap' or cmd == 'nobet' or cmd == 'nosus':
            pass
        
        elif cmd == 'dripcheck':
            name = tokens[1]
            val = self.vars.get(name, 0)
            if val:
                print(f"{name} got drip")
            else:
                print(f"{name} dry fr")
        elif cmd == 'ghost':
            name = tokens[1]
            if self.main_character == name:
                self.skill_issue(f"can't ghost the main character {name}")
            if name in self.vars:
                print(f"{name} has been ghosted")
                del self.vars[name]
            else:
                self.skill_issue(f"can't ghost {name}, not found")
        elif cmd == 'rizzup':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] += 1
                print(f"{name} rizzed up to {self.vars[name]}")
            else:
                self.skill_issue(f"can't rizzup {name}, not found")
        elif cmd == 'gyattdown':
            name = tokens[1]
            if name in self.vars:
                self.vars[name] -= 1
                print(f"{name} gyatt down to {self.vars[name]}")
            else:
                self.skill_issue(f"can't gyattdown {name}, not found")
        elif cmd == 'vibecheck':
            print("Current aura:")
            for k, v in self.vars.items():
                if k != 'loopindex':
                    print(f"  {k}: {v}")
        elif cmd == 'maincharacter':
            name = tokens[1]
            self.main_character = name
            print(f"{name} is now the main character!")

        elif cmd == 'compliment':
            phrase = random.choice(self.compliment_phrases)
            print(f"{phrase}")
        elif cmd == 'motivation':
            motivational_quotes = [
                "You're absolutely slaying today!",
                "Main character energy activated!",
                "You're literally glowing up!",
                "That's iconic behavior!",
                "You're living your best life!",
                "Main character energy is immaculate!",
                "You're the moment!",
                "Your vibe is unmatched!",
                "You're a certified gem!",
                "You're absolutely sending me (in the best way)!"
            ]
            print(random.choice(motivational_quotes))
        elif cmd == 'aesthetic':
            aesthetics = [
                "vibes",
                "dark academia energy",
                "beach day mood",
                "cottagecore dreams",
                "ethereal night vibes",
                "edgy main character",
                "rainbow unicorn energy",
                "kawaii princess mode"
            ]
            print(random.choice(aesthetics))
        elif cmd == 'debug':
            self.debug_mode = not self.debug_mode
            status = "ON" if self.debug_mode else "OFF"
            print(f"Debug mode: {status}")
        elif cmd == 'save':
            filename = tokens[1] if len(tokens) > 1 else "aura_save.json"
            save_data = {
                'vars': self.vars,
                'main_character': self.main_character
            }
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=2)
            print(f"State saved to {filename}")
        elif cmd == 'load':
            filename = tokens[1] if len(tokens) > 1 else "aura_save.json"
            try:
                with open(filename, 'r') as f:
                    save_data = json.load(f)
                self.vars = save_data.get('vars', {})
                self.main_character = save_data.get('main_character')
                print(f"State loaded from {filename}")
            except FileNotFoundError:
                self.skill_issue(f"save file {filename} not found")
        elif cmd == 'clear':
            if len(tokens) > 1 and tokens[1] == 'all':
                self.vars.clear()
                self.main_character = None
                print("All variables cleared")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd == 'help':
            print("AURA Commands:")
            print("  aura/gyatt var = value - declare/assign variable")
            print("  rizz/slay/periodt/vibes - output with style")
            print("  vibe var - get input")
            print("  loop n...endloop - basic loop")
            print("  whileloop condition...endwhileloop - while loop")
            print("  betif/susif condition - conditionals")
            print("  bet func(params)...no-cap - define function")
            print("  squad arr = [1,2,3] - create array")
            print("  ghost var - delete variable")
            print("  rizzup/gyattdown var - increment/decrement")
            print("  vibecheck - show all variables")
            print("  maincharacter var - set main character")
            print("  compliment/motivation/aesthetic - random positivity")
            print("  debug - toggle debug mode")
            print("  save/load filename - save/load state")
            print("  clear [all] - clear screen or variables")
            print("  exit - quit program")
        elif cmd == 'exit':
            print('aura out! Thanks for vibing with us!')
            sys.exit(0)
        else:
            self.skill_issue(f'unknown command: {cmd}')

    def tokenize(self, expr):
        """Tokenize expression properly handling quoted strings with spaces"""
        tokens = []
        current_token = ""
        in_quotes = False
        
        i = 0
        while i < len(expr):
            char = expr[i]
            
            if char == '"':
                if in_quotes:
                    current_token += char
                    tokens.append(current_token)
                    current_token = ""
                    in_quotes = False
                else:
                    if current_token:
                        tokens.append(current_token)
                        current_token = ""
                    current_token += char
                    in_quotes = True
            elif char == ' ' and not in_quotes:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
            
            i += 1
        
        if current_token:
            tokens.append(current_token)
        
        return tokens

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='AURA Esolang Interpreter - The Gen Z Programming Language')
    parser.add_argument('file', help='Path to your AURA esolang file')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debug mode')
    parser.add_argument('--version', '-v', action='version', version='AURA v2.0')
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            code = f.read()
        interpreter = AuraInterpreter()
        if args.debug:
            interpreter.debug_mode = True
        interpreter.run(code)
    except FileNotFoundError:
        print(f"skill issue: file '{args.file}' not found")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"skill issue: encoding error in file '{args.file}' - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"skill issue: {e}")
        sys.exit(1)