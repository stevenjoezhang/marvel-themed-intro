# Marvel Themed Intro

漫威的电影片头特点非常鲜明——伴随着翻动漫画书的背景，「Marvel Studios」的标题渐渐浮现出来。使用 After Effects 或者 Final Cut Pro 这些视频编辑软件就可以仿制出这样的效果，在 YouTube 上可以找到许多教程。不过，对于这样的搬砖工作，也许用脚本来处理会更加灵活和方便。

## 安装 Install

```bash
# Clone this repository
git clone https://github.com/stevenjoezhang/marvel-themed-intro.git
# Go into the repository
cd marvel-themed-intro
```

## 依赖 Dependencies

需要 Python3 环境，并需要使用 `pip3` 安装 `numpy` 和 `opencv-contrib-python`。执行
```bash
# Install dependencies
pip3 install -r requirements.txt
```

你也可以手动安装这些依赖。值得注意的是，`opencv-python` 和 `opencv-contrib-python` 两者皆可，但同时安装会出现冲突。如果不幸出现了这一问题，请将两者卸载后再选择其一安装。

如果 `pip` 没有成功获取预编译的 OpenCV 版本，而是从源码编译安装，那么需要先准备好 OpenCV 相关组件。这可以通过包管理工具完成，例如在 macOS 上执行`brew install opencv`，而 Debian 系执行`sudo apt install libopencv-dev`。

## 使用 Usage

将你要用来制作片头的图片放在一个文件夹里，例如 `images/` 文件夹，我们假定其绝对目录为 `/path/to/your/images/`。这些图片最好分辨率足够高，并且宽高比与期望输出视频的宽高比接近。该脚本会对所有图片进行预处理，以使得它们适合进行进一步的操作。  
这一步完成后，执行
```bash
python3 marvel.py
```
然后按提示输入参数即可，例如前面提到的绝对目录。视频默认为 1920x1080，24fps，每张图片持续 3 帧。  
为了制作时间足够长的片头，你可以准备更多的图片，或者增加每张图片持续的帧数。如果这些照片都是漫威的漫画截图，那么就可以做出一个高仿的片头了。  
完成后，会在你的执行目录下生成 `save.mp4`，看看效果如何吧！  
当然，这个脚本只是处理了一部分的（搬砖）工作。你还是需要使用视频后期处理软件，加上你的字幕等内容（对应于 MARVEL STUDIOS 标志），此处不再赘述。如果视频的编码出现问题，可以试试使用 `ffmpeg` 转码。

## Credits

* [Mimi](https://zhangshuqiao.org) Developer of this project.

## License

Released under the GNU General Public License v3  
http://www.gnu.org/licenses/gpl-3.0.html
