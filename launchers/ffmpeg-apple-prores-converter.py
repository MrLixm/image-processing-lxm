import subprocess
import sys
import time
from pathlib import Path

from lxmimgproc.ffmpeg import FFmpegProResDataRate


THISDIR = Path(__file__).parent
SCRIPTSDIR = THISDIR.parent / "scripts"
SCRIPT = SCRIPTSDIR / "ffmpeg-apple-prores-converter.py"

SRC_DIR = Path(
    r"G:\personal\photo\workspace\dcim\2024\2024_04_13_salieres\P1000653.MOV"
)
DST_PATH = SRC_DIR.with_stem(SRC_DIR.stem + ".{datarate}.q{quality}")
DST_PATH = DST_PATH.with_suffix(".mov")


def main():
    print(f"💬 processing '{SRC_DIR.name}' ...")

    command = [
        sys.executable,
        str(SCRIPT),
        str(DST_PATH),
        str(SRC_DIR),
        "--datarate",
        FFmpegProResDataRate.s422.name,
        "--quality",
        "10",
    ]
    stime = time.time()
    subprocess.run(command)
    etime = time.time()
    print(f"✅ completed in {etime - stime:.2f}s ...")


if __name__ == "__main__":
    main()
