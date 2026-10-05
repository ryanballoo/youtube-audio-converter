# YouTube Audio Converter

Extract high-quality 320 kbps MP3 audio from YouTube videos with optimized download speeds.

## Features

- 🎵 Downloads highest quality audio from YouTube videos
- 🎧 Converts to 320 kbps MP3 format
- 📝 Automatic proper file naming from video title
- ⚡ Optimized parallel downloads for faster speeds
- 📋 Smart playlist detection with options to download single videos or entire playlists
- 🔄 Resume incomplete downloads automatically
- ✅ Skip already downloaded files
- 🛡️ Error handling - continues with remaining downloads if one fails
- 🎯 Support for specific playlist ranges (e.g., "1-10")

## Requirements

- Python 3.7 or higher
- yt-dlp (automatically installed)
- FFmpeg (bundled with yt-dlp)

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/ryanballoo/youtube-audio-converter.git
cd youtube-audio-converter
```

### 2. Create and activate virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode
Run the script and provide a YouTube URL when prompted:
```bash
python youtube_audio_converter.py
```

### Command Line Mode
Provide the URL directly as an argument:
```bash
python youtube_audio_converter.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Playlist Handling

When you provide a playlist URL, you'll be prompted:
```
⚠️  Playlist detected!
Download entire playlist? (y/n) [n]: 
```

**Options:**
- Press `n` or Enter: Downloads only the single video (ignoring playlist)
- Press `y`: Downloads entire playlist
- Specify range: Enter "1-10" to download items 1-10, or "1,5,10-15" for specific items

### Examples

**Download single video:**
```bash
python youtube_audio_converter.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Download playlist (will prompt for confirmation):**
```bash
python youtube_audio_converter.py "https://www.youtube.com/playlist?list=PLxxxxxx"
```

**Output location:** All MP3 files are saved in the `downloads/` directory.

## Performance Optimizations

The tool includes several performance enhancements:
- **Concurrent fragment downloads**: Downloads 5 fragments in parallel
- **Large buffers**: 16MB buffer for faster I/O operations
- **Resume capability**: Automatically resumes interrupted downloads
- **Smart skip**: Won't re-download existing files
- **HTTP chunk optimization**: 10MB chunks for efficient network usage

## Project Structure

```
youtube-audio-converter/
├── youtube_audio_converter.py  # Main application
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
├── downloads/                  # Output directory (created automatically)
└── venv/                       # Virtual environment (not tracked)
```

## Troubleshooting

**Issue: "No module named 'yt_dlp'"**
- Solution: Activate virtual environment and run `pip install -r requirements.txt`

**Issue: "ERROR: unable to download video data: HTTP Error 403: Forbidden"**
- Solution: Update yt-dlp and run `pip install -U yt-dlp`

**Issue: Slow downloads**
- The script is already optimized with concurrent downloads
- Check your internet connection speed
- Some YouTube videos may have bandwidth limitations

**Issue: "ffmpeg not found"**
- yt-dlp includes ffmpeg binaries automatically
- If issues persist, install ffmpeg manually from https://ffmpeg.org/

**Issue: JavaScript runtime warnings**
- These warnings are normal and don't affect audio quality
- Downloads will complete successfully despite the warnings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

## Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Audio conversion powered by FFmpeg
