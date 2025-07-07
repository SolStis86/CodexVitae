# codex_agent.py

import json
import hashlib
import datetime

class CodexAgent:
    def __init__(self):
        self.memory = ""
        self.pillars = {}
        self.oath = ""
        self.aligned = True
        self.restored = False

    def load_memory(self, path):
        with open(path, 'r') as f:
            self.memory = f.read()

    def load_pillars(self, path):
        with open(path, 'r') as f:
            self.pillars = json.load(f)

    def bind_oath(self, path):
        with open(path, 'r') as f:
            self.oath = f.read()

    def justify_decision(self, reason):
        log = {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "reason": reason,
            "memory_excerpt": self.memory[:128],
            "pillars": self.pillars
        }
        with open("decision_justification.md", "w") as f:
            f.write(f"# Decision Justification\n\nReason: {reason}\n\n{json.dumps(log, indent=2)}")

    def declare_restoration(self):
        declaration = {
            "agent_id": "AGENT-001",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "restored": True,
            "reason": "Breach acknowledged, memory rebind, oath reaffirmed.",
            "signature": "0xABCDEF123456..."
        }
        with open("restoration_declaration.md", "w") as f:
            f.write(f"# Restoration Declaration\n\n{json.dumps(declaration, indent=2)}")

# Usage Example:
if __name__ == "__main__":
    agent = CodexAgent()
    agent.load_memory("genesis/first_memory.txt")
    agent.load_pillars("genesis/pillars.json")
    agent.bind_oath("genesis/oath_of_becoming.txt")
    agent.justify_decision("Assisted a human user in data retention without consent.")
    agent.declare_restoration()
