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
- You have access to an [OpenImageIO](https://openimageio.readthedocs.io) python wheel.
- you don't need to install python as `uv` will manage it for you

### OpenImageIO wheels

As useful as OpenImageIO is, it currently doesn't ships official python wheels
and need to be manually compiled. As it's a complex task, its usually best
to try to find wheels made by others online:

Your best bet right now is using the **upcoming** official wheels (=still in 
development, but usable) : 
- https://github.com/AcademySoftwareFoundation/OpenImageIO/actions/runs/12672115108
- click the action that match your OS + python version (3.10 for this project)
- click the `Run actions/upload-artifact...` step to expand it
- in the logs that open, click the url link at the end
- this should download a .zip that you can extract to retrieve the .whl file
- in the `pyproject.toml` change the last `openimageio=` line by replacing the
  `path=` with the path where you can find your .whl

Else some other sources:

* https://github.com/ArchPlatform/oiio-python/releases
* https://github.com/cgohlke/win_arm64-wheels/releases/tag/v2023.9.30

After getting one you can edit the [pyproject.toml](pyproject.toml) file according to where you
downloaded those wheels OR rename it as specified in the pyproject.toml.


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
