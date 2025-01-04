import subprocess
import sys
import time
from pathlib import Path

THISDIR = Path(__file__).parent
SCRIPTSDIR = THISDIR.parent / "scripts"
SCRIPT = SCRIPTSDIR / "mosaic-generator.py"

INPUT_DIR = Path(r"G:\personal\photo\workspace\dcim\2023\2023_12_27_tarentaise")
DST_PATH = Path(r"Z:\packages-dev\lxmImageProcessing\tmp") / "mosaic2.jpg"

OIIOTOOL = Path(r"F:\softwares\apps\oiio\build\2.3.10\oiiotool.exe")


def main():
    print(f"💬 processing '{INPUT_DIR.name}' ...")
    command = [
        sys.executable,
        str(SCRIPT),
        str(DST_PATH),
        str(INPUT_DIR),
        "--image-extensions",
        "jpg",
        "--oiiotool",
        str(OIIOTOOL),
        # "--anamorphic-desqueeze",
        # "1.8",
    ]
    stime = time.time()
    subprocess.run(command)
    etime = time.time()
    print(f"✅ completed in {etime - stime:.2f}s ...")


if __name__ == "__main__":
    main()
