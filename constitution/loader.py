import json
from pathlib import Path
from typing import Dict, Optional

# =====================================================
# CONSTITUTION LOADER
# =====================================================

CONSTITUTION_DIR = Path(__file__).parent / "constitution"


def load_constitution(filename: str) -> Dict:
    """Load a constitution JSON file."""
    path = CONSTITUTION_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Constitution file not found: {path}")
    
    with open(path, 'r') as f:
        return json.load(f)


def get_global_constitution() -> Dict:
    """Load the global constitution applied to all agents."""
    return load_constitution("constitution.json")


def get_agent_constitution(agent_name: str) -> Dict:
    """Load agent-specific constitution."""
    filename = f"{agent_name}_constitution.json"
    return load_constitution(filename)


def merge_constitutions(agent_name: str) -> Dict:
    """Merge global + agent-specific constitutions."""
    global_const = get_global_constitution()
    agent_const = get_agent_constitution(agent_name)
    
    return {
        "global": global_const,
        "agent_specific": agent_const,
        "agent_name": agent_name,
    }


def format_constitution_prompt(agent_name: str) -> str:
    """Format constitution as system prompt text."""
    merged = merge_constitutions(agent_name)
    
    global_const = merged["global"]
    agent_const = merged["agent_specific"]
    
    prompt = f"""
# CONSTITUTION FOR {agent_const.get('role', agent_name).upper()}

## MISSION
{agent_const.get('mission', 'No mission specified')}

## CORE DIRECTIVES
"""
    
    for directive in agent_const.get('core_directives', []):
        prompt += f"\n- {directive}"
    
    prompt += "\n\n## GLOBAL PRINCIPLES"
    for principle in global_const.get('principles', []):
        prompt += f"\n- {principle}"
    
    prompt += "\n\n## CONSTRAINTS"
    for constraint in agent_const.get('constraints', []):
        prompt += f"\n- {constraint}"
    
    return prompt


# =====================================================
# CONSTITUTION INJECTION INTO PROMPTS
# =====================================================

def inject_constitution_into_prompt(
    system_prompt: str,
    agent_name: str,
) -> str:
    """Prepend constitution to system prompt."""
    constitution_text = format_constitution_prompt(agent_name)
    return f"{constitution_text}\n\n{system_prompt}"


# =====================================================
# UTILITY: LIST ALL CONSTITUTIONS
# =====================================================

def list_constitutions() -> Dict[str, str]:
    """List all available constitution files."""
    if not CONSTITUTION_DIR.exists():
        return {}
    
    files = {}
    for path in CONSTITUTION_DIR.glob("*.json"):
        try:
            const = json.loads(path.read_text())
            files[path.name] = const.get("name", "Unknown")
        except:
            pass
    
    return files


if __name__ == "__main__":
    # Test loading
    print("Available Constitutions:")
    for filename, name in list_constitutions().items():
        print(f"  {filename}: {name}")
    
    print("\n" + "="*60)
    print("Sample - Plaintiff Strategy Constitution")
    print("="*60)
    sample = get_agent_constitution("plaintiff_strategy")
    print(json.dumps(sample, indent=2))
