
import logging
import tempfile
import os
import subprocess
import glob
from dataclasses import dataclass

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

THREADS = 8


def silentremove(filename):
    try:
        os.remove(filename)
    except Exception as e:
        logging.warning(e)
        pass


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


def mp4cmd(input_path, output_path, null_path, config):
    scale = f'scale={config.size}:-2'
    kbps = config.kbps
    crf = config.crf
    preset = config.preset
    fps = config.fps
    aac_kbps = config.aac_kbps
    fmt = config.fmt
    codec = config.codec
    cmd = f'ffmpeg -i {input_path} -threads {THREADS} -an -vcodec {codec}'\
        + f' -crf {crf} -b:v {kbps}k -vf "fps={fps},{scale}" -pass 1'\
        + f' -preset {preset} -f {fmt} {null_path} && ffmpeg -i {input_path}'\
        + f' -threads {THREADS} -c:a aac -b:a {aac_kbps}k -vcodec {codec} -crf {crf}'\
        + f' -b:v {kbps}k -vf "fps={fps},{scale}"'\
        + f' -pass 2 -preset {preset} {output_path}.{fmt}'
    return cmd


def vp8cmd(input_path, output_path, null_path, config):
    scale = f'scale={config.size}:-2'
    kbps = config.kbps
    crf = config.crf
    fps = config.fps
    libopus_kbps = config.libopus_kbps
    fmt = config.fmt
    quality = config.quality
    codec = config.codec
    cmd = f'ffmpeg -i {input_path} -threads {THREADS} -an -vcodec {codec}'\
        + f' -crf {crf} -b:v {kbps}k -vf "fps={fps},{scale}" -pass 1'\
        + f' -f {fmt} {null_path}.{fmt} -quality {quality}'\
        + f'&& ffmpeg -i {input_path}'\
        + f' -threads {THREADS} -c:a libopus -b:a {libopus_kbps}k -vcodec {codec} -crf {crf}'\
        + f' -b:v {kbps}k -vf "fps={fps},{scale}"'\
        + f' -pass 2 {output_path}.{fmt}'
    return cmd


def convert(mp4config, vp8config, filename, input_dir='input', output_dir='output'):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, ''.join(filename.split('.')[:-1]))
    silentremove(output_path + '.mp4')
    silentremove(output_path + '.webm')
    with tempfile.TemporaryDirectory() as dname:
        null_path = os.path.join(dname, 'null')
        subprocess.check_call('rm -rf ffmpeg2pass*', shell=True)
        cmd = mp4cmd(input_path, output_path, null_path, mp4config)
        logging.debug(cmd)
        subprocess.check_call(cmd, shell=True)
        logging.info(f'converted {filename} to mp4')
        cmd = vp8cmd(input_path, output_path, null_path, vp8config)
        logging.debug(cmd)
        subprocess.check_call(cmd, shell=True)
        subprocess.check_call('rm -rf ffmpeg2pass*', shell=True)
        logging.info(f'converted {filename} to vp8')


def main():
    mp4config = ConfigMP4()
    vp8config = ConfigVP8()
    fmts = ['mp4', 'mov', 'MOV', 'webm', 'avi']
    files = sum([glob.glob(f'./input/*.{fmt}') for fmt in fmts], [])
    for fname in files:
        fname = fname.split('/')[-1]
        convert(mp4config, vp8config, fname)


if __name__ == '__main__':
    logging.info('converter started')
    main()
