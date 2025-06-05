#!/usr/bin/env python3
import subprocess

def get_current_branch():
    result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                            text=True, capture_output=True, check=True)
    return result.stdout.strip()


def main():
    branch = get_current_branch()
    remote_branch = f"codex/{branch}"
    url = (
        "https://htmlpreview.github.io/?https://raw.githubusercontent.com/"
        f"bryandebourbon/eMusicReader/{remote_branch}/index.html"
    )
    print(url)


if __name__ == "__main__":
    main()

