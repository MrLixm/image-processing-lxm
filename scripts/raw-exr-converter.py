import subprocess
import sys
import time
from pathlib import Path

from lxmimgproc.browse import get_dir_content

THISDIR = Path(__file__).parent
CLISDIR = THISDIR.parent / "clis"
CLIPATH = CLISDIR / "raw-exr-converter.py"

RAW_SRC_DIR = Path(r"G:\personal\photo\workspace\dcim\2024\2024_06_20_mshootsweat")
EXIFTOOL_PATH = Path(r"F:\softwares\apps\exiftool\build\12.70\exiftool.exe")


def main():
    src_paths = get_dir_content(
        RAW_SRC_DIR,
        file_extensions=[".dng"],
    )
    print(f"processing {len(src_paths)} files")

    for index, src_path in enumerate(src_paths):
        print(f"{index+1}/{len(src_paths)} 💬 starting '{src_path.name}' ...")

        dst_path = src_path.with_stem("{input_filestem}.{preset}.{colorspace}")
        dst_path = dst_path.with_suffix(".exr")

        command = [
            sys.executable,
            str(CLIPATH),
            str(dst_path),
            str(src_path),
            "--colorspace",
            "@native",
            "--preset",
            "normal",
            # "--overwrite-existing",
            "--exiftool",
            str(EXIFTOOL_PATH),
        ]
        stime = time.time()
        subprocess.run(command)
        etime = time.time()
        print(f"{index+1}/{len(src_paths)} ✅ completed in {etime - stime:.2f}s ...")


if __name__ == "__main__":
    main()
