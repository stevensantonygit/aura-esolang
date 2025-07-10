# AURA: The Gen Z Esolang

import sys
import time
import random
import math
import os
import json
from datetime import datetime

class AuraEsolang:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.lines = []
        self.line_num = 0
        self.call_stack = []
        self.main_character = None
        self.arrays = {}
        self.debug_mode = False
        self.total_lines_executed = 0
        self.execution_start_time = None
        self.trend_phrases = [
            "is trending rn!",
            "just went viral!",
            "is a whole mood!",
            "is lowkey iconic!",
            "is giving main character energy!",
            "is a certified slay!",
            "is on the FYP!",
            "is a vibe!",
            "is not mid!",
            "is bussin'!",
            "is absolutely sending me!",
            "is giving main character energy!",
            "is a certified moment!",
            "is living rent-free in my head!",
            "is the main character fr!",
            "is not it chief!",
            "is lowkey bussin!",
            "is giving me life!",
            "is the vibe we needed!",
            "is absolutely iconic!"
        ]
        self.compliment_phrases = [
            "You're doing amazing!",
            "Period!",
            "That's bussin!",
            "Absolutely slaying!",
            "You're the main character!",
            "Living your best life!",
            "That's iconic behavior!",
            "You're glowing up!",
            "Pure main character energy!",
            "That's a whole mood!"
        ]

    def parse(self, code):
        self.lines = [line.split('#')[0].strip() for line in code.strip().split('\n') if line.strip() and not line.strip().startswith('#')]
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
            return random.randint(self.get_value(tokens[1]), self.get_value(tokens[2]))
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
        elif token in self.vars:
            return self.vars[token]
        else:
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
        
        while self.line_num < len(self.lines):
            self.log_execution(self.lines[self.line_num])
            self.exec_line(self.lines[self.line_num])
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
        
        if cmd == 'aura':
            name = tokens[1]
            if tokens[2] != '=':
                self.skill_issue('expected =')
            value = self.eval_expr(' '.join(tokens[3:]))
            self.vars[name] = value
        elif cmd == 'gyatt':
            name = tokens[1]
            if tokens[2] != '=':
                self.skill_issue('expected =')
            value = self.eval_expr(' '.join(tokens[3:]))
            self.vars[name] = value
        
        elif cmd == 'rizz':
            arg = ' '.join(tokens[1:])
            if arg.startswith('"') and arg.endswith('"'):
                print(arg[1:-1])
            elif arg in self.vars:
                print(self.vars[arg])
            else:
                try:
                    result = self.eval_expr(arg)
                    if result is not None:
                        print(result)
                except Exception:
                    self.skill_issue(f'cannot rizz {arg}')
        
        elif cmd == 'slay':
            arg = ' '.join(tokens[1:])
            result = self.eval_expr(arg) if arg not in self.vars else self.vars[arg]
            if arg.startswith('"') and arg.endswith('"'):
                result = arg[1:-1]
            print(f"[SLAY] {result}")
        elif cmd == 'periodt':
            arg = ' '.join(tokens[1:])
            result = self.eval_expr(arg) if arg not in self.vars else self.vars[arg]
            if arg.startswith('"') and arg.endswith('"'):
                result = arg[1:-1]
            print(f"[PERIODT] {result}")
        elif cmd == 'vibes':
            arg = ' '.join(tokens[1:])
            result = self.eval_expr(arg) if arg not in self.vars else self.vars[arg]
            if arg.startswith('"') and arg.endswith('"'):
                result = arg[1:-1]
            print(f"[VIBES] {result}")
        
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
        
        elif cmd == 'squad':
            name = tokens[1]
            if tokens[2] != '=':
                self.skill_issue('expected =')
            if '[' in line and ']' in line:
                array_str = line[line.index('['):line.index(']')+1]
                elements = array_str[1:-1].split(',')
                self.arrays[name] = [self.get_value(e.strip()) for e in elements if e.strip()]
            else:
                self.skill_issue('expected array format [1, 2, 3]')
        elif cmd == 'squadget':
            arr_name = tokens[1]
            index = self.get_value(tokens[2])
            if arr_name in self.arrays and 0 <= index < len(self.arrays[arr_name]):
                return self.arrays[arr_name][index]
            else:
                self.skill_issue(f"can't get index {index} from {arr_name}")
        elif cmd == 'squadset':
            arr_name = tokens[1]
            index = self.get_value(tokens[2])
            value = self.get_value(tokens[3])
            if arr_name in self.arrays and 0 <= index < len(self.arrays[arr_name]):
                self.arrays[arr_name][index] = value
            else:
                self.skill_issue(f"can't set index {index} in {arr_name}")
        elif cmd == 'squadpush':
            arr_name = tokens[1]
            value = self.get_value(tokens[2])
            if arr_name in self.arrays:
                self.arrays[arr_name].append(value)
            else:
                self.skill_issue(f"array {arr_name} not found")
        elif cmd == 'squadpop':
            arr_name = tokens[1]
            if arr_name in self.arrays and self.arrays[arr_name]:
                return self.arrays[arr_name].pop()
            else:
                self.skill_issue(f"can't pop from {arr_name}")
        elif cmd == 'squadlen':
            arr_name = tokens[1]
            if arr_name in self.arrays:
                return len(self.arrays[arr_name])
            else:
                self.skill_issue(f"array {arr_name} not found")

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
            if '(' in line and ')' in line:
                name = tokens[1]
                params = line[line.index('(')+1:line.index(')')].split(',')
                params = [p.strip() for p in params if p.strip()]
                body = []
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'no-cap':
                    body.append(self.lines[self.line_num])
                    self.line_num += 1
                self.functions[name] = (params, body)
            else:
                name = tokens[1]
                args = line[line.index('(')+1:line.index(')')].split(',')
                args = [a.strip() for a in args if a.strip()]
                if name not in self.functions:
                    self.skill_issue(f'no such function: {name}')
                params, body = self.functions[name]
                if len(params) != len(args):
                    self.skill_issue('argument count mismatch')
                old_vars = self.vars.copy()
                for p, a in zip(params, args):
                    self.vars[p] = self.get_value(a)
                for bline in body:
                    self.exec_line(bline)
                self.vars = old_vars
        
        elif cmd == 'betif':
            cond = self.eval_expr(' '.join(tokens[1:]))
            if cond:
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nobet':
                    self.exec_line(self.lines[self.line_num])
                    self.line_num += 1
            else:
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nobet':
                    self.line_num += 1
        elif cmd == 'susif':
            cond = self.eval_expr(' '.join(tokens[1:]))
            if not cond:
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nosus':
                    self.exec_line(self.lines[self.line_num])
                    self.line_num += 1
            else:
                self.line_num += 1
                while self.line_num < len(self.lines) and self.lines[self.line_num] != 'nosus':
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
            if self.arrays:
                print("Arrays:")
                for k, v in self.arrays.items():
                    print(f"  {k}: {v}")
        elif cmd == 'maincharacter':
            name = tokens[1]
            self.main_character = name
            print(f"{name} is now the main character!")