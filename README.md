# convert_for_insta
Convert your video files to H.264 and VP8 format for instagram in-feed videos.

Put the files into input dir, and exec `docker-compose up -d --build && docker-compose run convert`.


## Convert video files to 1080 x *** (H.264 and VP8, 30fps)

```bash
# Before running, put the video file in the input directory.

docker-compose up -d --build
docker-compose run convert

# After running, convert the video files to .mp4 and .wemb
# and automatically store them in the output directory.
```

## Details

- 3500kbps
- mono 128kbps audio
- width 1080 pixels

You can change more parameters by editing `config.py`.


# Regulations of in-feed videos on Instagram
- Maximum 30 frames per second.
- Square video minimum resolution is 600 x 600. Max is 1080 x 1080.
- Portrait video minimum resolution is 600 x 750. Max is 1080 x 1350.
- Landscape video minimum resolution is 600 x 315. Max is 1080 x 608.
- Stories video minimum resolution is 600 x 1067. Max is 1080 x 1920.
- Carousel video minimum resolution is 600 x 700. Max is 1080 x 1080.

- Maximum length of 60 seconds (NOT CONSIDERED IN THIS PROGRAM).
- Maximum file size of 4 GB (NOT CONSIDERED IN THIS PROGRAM).

### Ref.
- https://www.quora.com/What-is-the-minimum-or-maximum-size-of-a-video-for-Instagram