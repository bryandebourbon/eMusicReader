#!/usr/bin/env python3
import subprocess

def get_current_branch():
    result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                            text=True, capture_output=True, check=True)
    return result.stdout.strip()


def main():
    branch = get_current_branch()
    url = (
        "https://htmlpreview.github.io/?https://raw.githubusercontent.com/"
        f"bryandebourbon/eMusicReader/{branch}/index.html"
    )
    print(url)


if __name__ == "__main__":
    main()

