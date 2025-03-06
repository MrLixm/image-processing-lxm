# image-processing-lxm

Personal resources for image-processing which include topics like :

* photography
* cinematography
* vfx

> [!WARNING]
> The package is not fully designed for public consumptions so use at your own
> risks. I can deploy major "breaking" changes at any time without notice.

## content

You can find 4 software components:

- _libraries_: collection of reusable code
- _clis_: command line interfaces programs
- _scripts_: entry point mixing the usage of _libraries_ and _clis_
- _plugins_: to be used in other software

| tool                                                                         | description                                                 | type    | tag                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------|---------|-----------------------------------------------------|
| [raw-to-dng.py](scripts/raw-to-dng.py)                                       | batch converting raw files to dng                           | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [raw-exr-converter.py](scripts/raw-exr-converter.py)                         | batch converting raw files to OpenEXR, including debayering | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [rw2-to-dng.py](scripts/rw2-to-dng.py)                                       | batch converting panasonic raw file to dng (personal need)  | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [mosaic-generator.py](scripts/mosaic-generator.py)                           | combine multiple image to a single big mosaic of image      | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [ffmpeg-apple-prores-converter.py](scripts/ffmpeg-apple-prores-converter.py) | encode to apple prores using ffmpeg                         | script  | ![video](https://img.shields.io/badge/video-4c78a6) |
| [lxmimgproc](libraries/lxmimgproc)                                           | python wrapper to interract with i-o libraries              | library | ![photo](https://img.shields.io/badge/photo-43896b) |
| [loog](plugins/loog)                                                         | nuke node to develop film negatives                         | plugin  | ![photo](https://img.shields.io/badge/photo-43896b) |

Each tool should come with its own documentation for details.

## usage pre-requisites

Most tool (except _plugins_) will require python and some dependencies.

- [uv](https://docs.astral.sh/uv/) is [installed](https://docs.astral.sh/uv/getting-started/installation/)
- you don't need to install python as `uv` will manage it for you

## usage

Project is managed through [uv](https://docs.astral.sh/uv/).

Assuming uv and git are installed and available on your system, open a 
terminal and execute the following commands:

```shell
cd path/you/want/to/download/the/project/to
# the git clone step can be replaced by a manual download of the repo
git clone https://github.com/MrLixm/image-processing-lxm.git
cd image-processing-lxm
uv run ./scripts/raw-exr-converter.py
```

You will usually to edit the global variables in the scripts to replace
with path for your system. You can also directly use the [clis](clis) instead
of the scripts wrapper.

If that can help I recorded for someone a quick video that explains how to use 
[raw-exr-converter.py](scripts/raw-exr-converter.py): https://youtu.be/-w_OqmZ0-NU


## runtime pre-requistes

some of the tools assume you have specific software available on your system:

| FFMPEG    | https://ffmpeg.org                                                                   |
|-----------|--------------------------------------------------------------------------------------|
| download  | https://ffmpeg.org/download.html                                                     |
| configure | expected to have the path to the executable set in the `FFMPEG` environment variable |

| OIIOTOOL  | https://openimageio.readthedocs.io/en/latest/oiiotool.html |
|-----------|------------------------------------------------------------|
| download  | managed with python dependencies through uv                |
| configure | /                                                          |

| EXIFTOOL  | https://exiftool.org/                                                                  |
|-----------|----------------------------------------------------------------------------------------|
| download  | https://exiftool.org/                                                                  |
| configure | expected to have the path to the executable set in the `EXIFTOOL` environment variable |

| Adobe DNG converter | https://helpx.adobe.com/camera-raw/digital-negative.html                                   |
|---------------------|--------------------------------------------------------------------------------------------|
| download            | https://helpx.adobe.com/camera-raw/digital-negative.html#downloads                         |
| configure           | expected to have the path to the executable set in the `ADOBEDNGTOOL` environment variable |
