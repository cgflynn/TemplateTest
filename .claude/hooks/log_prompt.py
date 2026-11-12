"""Claude Code UserPromptSubmit hook: append each user prompt to docs/ai-log/prompts/.

Reads the hook JSON from stdin. Never blocks the prompt; on any error it exits quietly.
"""
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
    user = git("config", "user.name") or os.environ.get("USERNAME") or os.environ.get("USER") or "unknown"
    safe_user = "".join(c if c.isalnum() or c in "-_" else "-" for c in user)
    now = datetime.now()
    out = root / "docs" / "ai-log" / "prompts" / f"{now:%Y-%m-%d}_{safe_user}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    branch = git("branch", "--show-current") or "unknown"
    entry = (
        f"\n### {now:%H:%M:%S}  branch `{branch}`  session `{data.get('session_id', '')[:8]}`\n"
        f"```text\n{prompt}\n```\n"
    )
    if not out.exists():
        out.write_text(f"# Prompt record: {now:%Y-%m-%d}, {user}\n", encoding="utf-8")
    with out.open("a", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
    sys.exit(0)
