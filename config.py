from dataclasses import dataclass


@dataclass
class ConfigMP4:
    size: int = 1080
    fps: int = 30
    crf: int = 18
    kbps: int = 3500
    aac_kbps: int = 128
    fmt: str = 'mp4'
    codec: str = 'libx264'
    preset: str = 'slow'


@dataclass
class ConfigVP8:
    size: int = 1080
    fps: int = 30
    crf: int = 5
    qmin: int = 5
    qmax: int = 50
    kbps: int = 3500
    libopus_kbps: int = 128
    fmt: str = 'webm'
    codec: str = 'libvpx'
    quality: str = 'good'