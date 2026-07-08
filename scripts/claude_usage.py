#!/usr/bin/env python3
import os
import json
import glob
from datetime import datetime

# Claude API pricing per 1 Million Tokens (USD)
PRICING = {
    "claude-3-5-sonnet": {"input": 3.0, "output": 15.0, "cache_write": 3.75, "cache_read": 0.3},
    "claude-3-7-sonnet": {"input": 3.0, "output": 15.0, "cache_write": 3.75, "cache_read": 0.3},
    "claude-opus-4-7": {"input": 15.0, "output": 75.0, "cache_write": 18.75, "cache_read": 1.5},
    "default": {"input": 3.0, "output": 15.0, "cache_write": 3.75, "cache_read": 0.3}
}

CLAUDE_PROJECT_DIR = "/Users/eunsol/.claude/projects/-Users-eunsol-Project-para"

def get_pricing_key(model_name):
    if not model_name:
        return "default"
    model_name = model_name.lower()
    for key in PRICING:
        if key in model_name:
            return key
    return "default"

def calculate_cost(model_name, usage):
    pkey = get_pricing_key(model_name)
    pricing = PRICING[pkey]
    
    input_tokens = usage.get("input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)
    cache_read = usage.get("cache_read_input_tokens", 0)
    cache_write = usage.get("cache_creation_input_tokens", 0)
    
    # Costs per token
    cost = (
        (input_tokens * pricing["input"]) +
        (output_tokens * pricing["output"]) +
        (cache_read * pricing["cache_read"]) +
        (cache_write * pricing["cache_write"])
    ) / 1_000_000.0
    return cost

def parse_session(filepath):
    stats = {
        "messages": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_read_tokens": 0,
        "cache_write_tokens": 0,
        "cost": 0.0,
        "tools_used": {},
        "models": set(),
        "first_prompt": None,
        "summary": None
    }
    
    if not os.path.exists(filepath):
        return stats

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                
                # Try to extract first user prompt if not set
                if data.get("type") == "user" and not stats["first_prompt"]:
                    msg_content = data.get("message", {}).get("content", "")
                    if msg_content and not msg_content.startswith("<local-command-caveat>"):
                        stats["first_prompt"] = msg_content
                
                # Check for assistant messages
                if data.get("type") == "assistant" and "message" in data:
                    msg = data["message"]
                    stats["messages"] += 1
                    
                    # Track model
                    model = msg.get("model")
                    if model:
                        stats["models"].add(model)
                    
                    # Track usage
                    usage = msg.get("usage")
                    if usage:
                        stats["input_tokens"] += usage.get("input_tokens", 0)
                        stats["output_tokens"] += usage.get("output_tokens", 0)
                        stats["cache_read_tokens"] += usage.get("cache_read_input_tokens", 0)
                        stats["cache_write_tokens"] += usage.get("cache_creation_input_tokens", 0)
                        stats["cost"] += calculate_cost(model, usage)
                
                # Track tool usage
                if data.get("type") == "assistant" and "message" in data:
                    content = msg.get("content", [])
                    for item in content:
                        if item.get("type") == "tool_use":
                            tool_name = item.get("name")
                            stats["tools_used"][tool_name] = stats["tools_used"].get(tool_name, 0) + 1
                            
            except json.JSONDecodeError:
                continue
                
    return stats

def main():
    if not os.path.exists(CLAUDE_PROJECT_DIR):
        print(f"[-] Claude project directory not found at {CLAUDE_PROJECT_DIR}")
        return

    # Load session index if exists
    index_path = os.path.join(CLAUDE_PROJECT_DIR, "sessions-index.json")
    index_map = {}
    if os.path.exists(index_path):
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                index_data = json.load(f)
                for entry in index_data.get("entries", []):
                    index_map[entry.get("sessionId")] = entry
        except Exception as e:
            print(f"[!] Warning parsing sessions-index.json: {e}")

    # Scan for all JSONL files in directory
    jsonl_files = glob.glob(os.path.join(CLAUDE_PROJECT_DIR, "*.jsonl"))
    
    sessions = []
    for filepath in jsonl_files:
        filename = os.path.basename(filepath)
        sid = filename.replace(".jsonl", "")
        
        # Get modification time
        mtime = os.path.getmtime(filepath)
        dt = datetime.fromtimestamp(mtime)
        dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        stats = parse_session(filepath)
        
        # Merge index metadata
        idx_entry = index_map.get(sid, {})
        first_prompt = idx_entry.get("firstPrompt") or stats["first_prompt"] or "N/A"
        summary = idx_entry.get("summary") or stats["summary"] or "Active Session"
        git_branch = idx_entry.get("gitBranch") or "unknown"
        
        # Filter out empty sessions with no prompts/messages if they are not in index
        if stats["messages"] == 0 and first_prompt == "N/A":
            continue

        sessions.append({
            "sid": sid,
            "mtime": mtime,
            "dt_str": dt_str,
            "stats": stats,
            "first_prompt": first_prompt,
            "summary": summary,
            "git_branch": git_branch
        })

    # Sort sessions by modification time descending
    sessions.sort(key=lambda x: x["mtime"], reverse=True)

    print("\n" + "="*95)
    print(f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - CLAUDE CODE USAGE DASHBOARD (ALL SESSIONS)")
    print("="*95)
    print(f"{'Session ID':<38} | {'Date (Local)':<19} | {'Msgs':<4} | {'Cost (USD)':<10} | {'Git Branch'}")
    print("-"*95)

    total_msgs = 0
    total_cost = 0.0
    total_input = 0
    total_output = 0
    total_cache_read = 0
    total_cache_write = 0
    all_tools = {}

    for s in sessions:
        stats = s["stats"]
        total_msgs += stats["messages"]
        total_cost += stats["cost"]
        total_input += stats["input_tokens"]
        total_output += stats["output_tokens"]
        total_cache_read += stats["cache_read_tokens"]
        total_cache_write += stats["cache_write_tokens"]
        
        for tool, count in stats["tools_used"].items():
            all_tools[tool] = all_tools.get(tool, 0) + count

        prompt_text = s["first_prompt"].replace("\n", " ")
        if len(prompt_text) > 75:
            prompt_text = prompt_text[:72] + "..."
            
        summary_text = s["summary"].replace("\n", " ")
        if len(summary_text) > 75:
            summary_text = summary_text[:72] + "..."

        print(f"{s['sid']:<38} | {s['dt_str']:<19} | {stats['messages']:<4} | ${stats['cost']:<9.4f} | {s['git_branch']}")
        print(f"  └─ First prompt: {prompt_text}")
        print(f"  └─ Summary:      {summary_text}")
        print("-"*95)

    print("\n" + "="*95)
    print(" TOTAL ACCUMULATED METRICS")
    print("="*95)
    print(f"• Total Active Sessions: {len(sessions)}")
    print(f"• Total Conversations:   {total_msgs}")
    print(f"• Estimated Cost:        ${total_cost:.4f} USD")
    print(f"• Input Tokens:          {total_input:,} tokens")
    print(f"• Output Tokens:         {total_output:,} tokens")
    print(f"• Cache Read Tokens:     {total_cache_read:,} tokens")
    print(f"• Cache Created Tokens:  {total_cache_write:,} tokens")
    
    if all_tools:
        print("\n" + "-"*40 + " Top Tools Used " + "-"*39)
        sorted_tools = sorted(all_tools.items(), key=lambda x: x[1], reverse=True)
        for tool, count in sorted_tools[:8]:
            print(f" - {tool:<35} : {count} times")
    print("="*95 + "\n")

if __name__ == "__main__":
    main()
