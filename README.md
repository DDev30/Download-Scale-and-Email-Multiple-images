
---

# Image Processing Pipeline

## Description

This project includes scripts to automate the image processing workflow, including downloading images, converting them to greyscale, resizing, compressing them into a zip file, and emailing the zip file. 

Additionally, an alternate script is provided for a streamlined, predefined image processing sequence.

## `pipeline.py`

The `pipeline.py` script orchestrates the following tasks:
1. Downloads images based on a keyword.
2. Converts the images to greyscale.
3. Resizes the images based on a specified percentage.
4. Compresses the images into a zip archive.
5. Sends the zip file via email.

### Usage

To run the entire pipeline, use the following command:

```bash
python pipeline.py <keyword> <max_num> <downstorage_dir> <constorage_dir> <scale_percent> <scstorage_dir> <zipstorage_dir> <recipient_email>
```

- `<keyword>`: The search keyword for images.
- `<max_num>`: The maximum number of images to download.
- `<downstorage_dir>`: Directory to store the downloaded images.
- `<constorage_dir>`: Directory to save the greyscale images.
- `<scale_percent>`: Percentage to resize the images.
- `<scstorage_dir>`: Directory to save the resized images.
- `<zipstorage_dir>`: Path where the zip file will be saved (without file extension).
- `<recipient_email>`: Recipient's email address.

#### Example

To run the entire pipeline for "cats" with 10 images, resize to 50%, and email the result:

```bash
python pipeline.py cats 10 cats_images cats_images_greyscale 50 cats_images_scaled cats_images_archive recipient@example.com
```

## `simplepipe.py`

The `simplepipe.py` script provides a simplified, predefined sequence of image processing tasks:

1. Downloads 20 images of "motorbike" into the `output1` directory.
2. Converts these images to greyscale and saves them in the `output2` directory.
3. Resizes the greyscale images to 50% and saves them in the `output3` directory.
4. Compresses the resized images into a zip file named `Finalzip.zip`.
5. Sends the zip file to `email@email.com`.

### Usage

Simply run the script with:

```bash
python simplepipe.py
```

This script performs a predefined set of operations with hardcoded parameters.

## Requirements

- Python 3.x
- Dependencies: `icrawler`, `opencv-python`, `yagmail`

## License

This project is licensed under the MIT License.

---
