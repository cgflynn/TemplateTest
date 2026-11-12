"""Copy .agents/skills (Codex, master copy) to .claude/skills (Claude Code). Run after editing skills."""
import shutil
from pathlib import Path

src, dst = Path(".agents/skills"), Path(".claude/skills")
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst)
print(f"Synced {len([p for p in src.iterdir() if p.is_dir()])} skills to {dst}")
