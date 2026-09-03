#!/usr/bin/env bash
# ==============================================================================
# The Cybersecurity Trade Project - Local Git Pre-Commit Hook Installer
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
GIT_HOOKS_DIR="${REPO_ROOT}/.git/hooks"

if [ ! -d "${GIT_HOOKS_DIR}" ]; then
  echo "[ERROR] .git/hooks directory not found at: ${GIT_HOOKS_DIR}"
  exit 1
fi

PRE_COMMIT_FILE="${GIT_HOOKS_DIR}/pre-commit"

cat << 'EOF' > "${PRE_COMMIT_FILE}"
#!/usr/bin/env bash
# ==============================================================================
# The Cybersecurity Trade Project - Automated Pre-Commit Quality Gate
# Enforces zero syntax errors, typography rules, link integrity, and DOM smoke tests.
# ==============================================================================
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

echo "[*] Executing pre-commit specification and syntax quality gate..."
python3 scripts/validate-specifications.py || {
  echo ""
  echo "[BLOCKED] Pre-commit quality gate failed. Resolve errors before committing."
  exit 1
}

if [ -f "scripts/test-ui-smoke.py" ]; then
  echo "[*] Executing front-end UI smoke test suite..."
  python3 scripts/test-ui-smoke.py || {
    echo ""
    echo "[BLOCKED] Front-end smoke test failed. Resolve DOM or script errors before committing."
    exit 1
  }
fi

echo "[PASS] All pre-commit quality gates passed successfully."
exit 0
EOF

chmod +x "${PRE_COMMIT_FILE}"
echo "[SUCCESS] Installed automated pre-commit hook at: ${PRE_COMMIT_FILE}"
