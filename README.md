# How to use

This is a python program to compress videos into smaller size mp4 videos for sharing on social media.

1. You can either use the HandbrakeCLI executable provided in the repo itself or download it from Handbrake's official website [here](https://handbrake.fr/downloads2.php) and then edit the `handbrake_path` var in the `main.py`.
2. Change the `source_dir`, `destination_dir` and `quality_value` according to you in `main.py`.
3. Higher value of `quality_value` means higher compression and therefore lower output video quality.
4. It will compress every video in the source directory which is not present in destination directory (if `overwrite` is set to `N`). If `overwrite` is set to `Y` then it will compress every video in the source directory and overwrite the file with same name in destination directory. 

