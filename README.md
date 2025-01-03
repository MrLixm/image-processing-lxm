# image-processing-lxm

Personal resources for image-processing which include topics like :

* photography
* cinematography
* vfx


> [!WARNING] 
> The package is not fully designed for public consumptions so use at your own
> risks. I can deploy major "breaking" changes at any time without notice.

# content

| tool                                                                         | description                                                 | type    | tag                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------|---------|-----------------------------------------------------|
| [raw-to-dng.py](scripts/raw-to-dng.py)                                       | batch converting raw files to dng                           | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [raw-exr-converter.py](scripts/raw-exr-converter.py)                         | batch converting raw files to OpenEXR, including debayering | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [rw2-to-dng.py](scripts/rw2-to-dng.py)                                       | batch converting panasonic raw file to dng (personal use)   | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [mosaic-generator.py](scripts/mosaic-generator.py)                           | combine multiple image to a single big mosaic of image      | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [ffmpeg-apple-prores-converter.py](scripts/ffmpeg-apple-prores-converter.py) | encode to apple prores using ffmpeg                         | script  | ![video](https://img.shields.io/badge/video-4c78a6) |
| [lxmImageProcessing](python/libraries/lxmimgproc)                            | python wrapper to interract with i-o libraries              | library | ![photo](https://img.shields.io/badge/photo-43896b) |

# installation

Project is managed through [uv](https://docs.astral.sh/uv/).

Assuming uv and git are installed and available on your system:

```shell
cd somewhere
git clone https://github.com/MrLixm/image-processing-lxm.git
cd image-processing-lxm
uv run ./scripts/raw-exr-converter.py --help
```

Next before installing dependencies you need to download some of them :

* OpenImageIO in [OpenImageIO](vendor/OpenImageIO) as python wheel,
  the initial wheel I was using are not available anymore so try to use
  instead:
    * https://github.com/ArchPlatform/oiio-python/releases
    * https://github.com/cgohlke/win_arm64-wheels/releases/tag/v2023.9.30

Update the [pyproject.toml](pyproject.toml) file according to where you
downloaded those wheels.

then to update the virtual environment run:

```shell
uv sync
```

## pre-requistes

some of the tools assume you have specific software available on your system:

| FFMPEG    | https://ffmpeg.org                                                                   |
|-----------|--------------------------------------------------------------------------------------|
| download  | https://ffmpeg.org/download.html                                                     |
| configure | expected to have the path to the executable set in the `FFMPEG` environment variable |

| OIIOTOOL  | https://openimageio.readthedocs.io/en/latest/oiiotool.html                             |
|-----------|----------------------------------------------------------------------------------------|
| download  | https://www.patreon.com/posts/openimageio-oiio-63609827                                |
| configure | expected to have the path to the executable set in the `OIIOTOOL` environment variable |

| EXIFTOOL  | https://exiftool.org/                                                                  |
|-----------|----------------------------------------------------------------------------------------|
| download  | https://exiftool.org/                                                                  |
| configure | expected to have the path to the executable set in the `EXIFTOOL` environment variable |

| Adobe DNG converter | https://helpx.adobe.com/camera-raw/digital-negative.html                                   |
|---------------------|--------------------------------------------------------------------------------------------|
| download            | https://helpx.adobe.com/camera-raw/digital-negative.html#downloads                         |
| configure           | expected to have the path to the executable set in the `ADOBEDNGTOOL` environment variable |
