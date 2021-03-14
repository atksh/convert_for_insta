# convert_for_insta

## Convert video files to 1080 x *** (H.264 and VP8, 30fps)

```bash
# Before running, put the video file in the input directory.

docker-compose up -d --build
docker-compose run convert

# After running, convert the video files to .mp4 and .wemb
# and automatically store them in the output directory.
```