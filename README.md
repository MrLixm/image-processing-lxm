# image-processing-lxm

Personal resources for image-processing which include topics like :

* photography
* cinematography
* vfx

> [!WARNING]
> The package is not fully designed for public consumptions so use at your own
> risks. I can deploy major "breaking" changes at any time without notice.

## content

| tool                                                                         | description                                                 | type    | tag                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------|---------|-----------------------------------------------------|
| [raw-to-dng.py](scripts/raw-to-dng.py)                                       | batch converting raw files to dng                           | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [raw-exr-converter.py](scripts/raw-exr-converter.py)                         | batch converting raw files to OpenEXR, including debayering | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [rw2-to-dng.py](scripts/rw2-to-dng.py)                                       | batch converting panasonic raw file to dng (personal use)   | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [mosaic-generator.py](scripts/mosaic-generator.py)                           | combine multiple image to a single big mosaic of image      | script  | ![photo](https://img.shields.io/badge/photo-43896b) |
| [ffmpeg-apple-prores-converter.py](scripts/ffmpeg-apple-prores-converter.py) | encode to apple prores using ffmpeg                         | script  | ![video](https://img.shields.io/badge/video-4c78a6) |
| [lxmimgproc](libraries/lxmimgproc)                                           | python wrapper to interract with i-o libraries              | library | ![photo](https://img.shields.io/badge/photo-43896b) |

## usage pre-requisites

- [uv](https://docs.astral.sh/uv/) is [installed](https://docs.astral.sh/uv/getting-started/installation/)
- You have access to an [OpenImageIO](https://openimageio.readthedocs.io) python wheel.

### OpenImageIO wheels

As useful as OpenImageIO is, it currently doesn't ships official python wheels
and need to be manually compiled. As it's a complex task, its usuyally best
to try to find wheels made by other online:

* https://github.com/ArchPlatform/oiio-python/releases
* https://github.com/cgohlke/win_arm64-wheels/releases/tag/v2023.9.30
* upcoming official wheels, still in
  development (no png support): https://github.com/AcademySoftwareFoundation/OpenImageIO/actions/runs/11613214259/job/32338496571

After getting one you can edit the [pyproject.toml](pyproject.toml) file according to where you
downloaded those wheels OR rename it as specified in the pyproject.toml.


## installation

Project is managed through [uv](https://docs.astral.sh/uv/).

Assuming uv and git are installed and available on your system:

```shell
cd somewhere
# the git clone step can be replaced by a manual download of the repo
git clone https://github.com/MrLixm/image-processing-lxm.git
cd image-processing-lxm
uv run ./scripts/raw-exr-converter.py --help
```


## runtime pre-requistes

some of the tools assume you have specific software available on your system:

| FFMPEG    | https://ffmpeg.org                                                                   |
|-----------|--------------------------------------------------------------------------------------|
| download  | https://ffmpeg.org/download.html                                                     |
| configure | expected to have the path to the executable set in the `FFMPEG` environment variable |

| OIIOTOOL  | https://openimageio.readthedocs.io/en/latest/oiiotool.html                                                           |
|-----------|----------------------------------------------------------------------------------------------------------------------|
| download  | https://www.patreon.com/posts/openimageio-oiio-63609827                                                              |
| download  | find it in any houdini installation. ex: `C:\Program Files\Side Effects Software\Houdini 20.5.332\bin\hoiiotool.exe` |
| configure | expected to have the path to the executable set in the `OIIOTOOL` environment variable                               |

| EXIFTOOL  | https://exiftool.org/                                                                  |
|-----------|----------------------------------------------------------------------------------------|
| download  | https://exiftool.org/                                                                  |
| configure | expected to have the path to the executable set in the `EXIFTOOL` environment variable |

| Adobe DNG converter | https://helpx.adobe.com/camera-raw/digital-negative.html                                   |
|---------------------|--------------------------------------------------------------------------------------------|
| download            | https://helpx.adobe.com/camera-raw/digital-negative.html#downloads                         |
| configure           | expected to have the path to the executable set in the `ADOBEDNGTOOL` environment variable |
