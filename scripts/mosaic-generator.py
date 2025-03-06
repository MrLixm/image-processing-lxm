import subprocess
import sys
import time
from pathlib import Path

THISDIR = Path(__file__).parent
CLISDIR = THISDIR.parent / "clis"
CLIPATH = CLISDIR / "mosaic-generator.py"

INPUT_DIR = Path(r"G:\personal\photo\workspace\dcim\2023\2023_12_27_tarentaise")
DST_PATH = Path(r"Z:\packages-dev\lxmImageProcessing\tmp") / "mosaic2.jpg"


def main():
    print(f"💬 processing '{INPUT_DIR.name}' ...")
    command = [
        sys.executable,
        str(CLIPATH),
        str(DST_PATH),
        str(INPUT_DIR),
        "--image-extensions",
        "jpg",
        # "--anamorphic-desqueeze",
        # "1.8",
    ]
    stime = time.time()
    subprocess.run(command)
    etime = time.time()
    print(f"✅ completed in {etime - stime:.2f}s ...")


if __name__ == "__main__":
    main()
