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