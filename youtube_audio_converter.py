#!/usr/bin/env python3
"""
YouTube Audio Converter
Extracts high-quality 320 kbps MP3 audio from YouTube videos.
"""

import os
import sys
import yt_dlp
from pathlib import Path


class YouTubeAudioConverter:
    """Handles downloading and converting YouTube videos to high-quality MP3."""
    
    def __init__(self, output_dir: str = "downloads", concurrent_downloads: int = 5, 
                 download_playlist: bool = False, playlist_items: str = None):
        """
        Initialize the converter.
        
        Args:
            output_dir: Directory where MP3 files will be saved
            concurrent_downloads: Number of parallel downloads (default: 5)
            download_playlist: Whether to download entire playlists (default: False)
            playlist_items: Specific playlist items to download (e.g., "1-5,10,15-20")
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Configure yt-dlp options for highest quality MP3 with optimizations
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': True,
            'extract_flat': False,
            'noplaylist': not download_playlist,  # Download only single video by default
            # Performance optimizations
            'concurrent_fragment_downloads': concurrent_downloads,  # Parallel fragment downloads
            'retries': 3,  # Retry failed downloads
            'fragment_retries': 3,
            'file_access_retries': 3,
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
            'buffersize': 1024 * 1024 * 16,  # 16MB buffer
            'throttledratelimit': None,  # No speed limit
            'noprogress': False,  # Show progress
            'ignoreerrors': True,  # Continue on errors instead of stopping
            'continuedl': True,  # Resume incomplete downloads
            'overwrites': False,  # Skip already downloaded files
        }
        
        # Add playlist items filter if specified
        if playlist_items:
            self.ydl_opts['playlist_items'] = playlist_items
    
    def download(self, url: str) -> bool:
        """
        Download and convert a YouTube video to MP3.
        
        Args:
            url: YouTube video URL
            
        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"\n🎵 Processing: {url}")
            print("=" * 60)
            
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # Extract video info first
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)
                
                print(f"Title: {title}")
                print(f"Duration: {duration // 60}:{duration % 60:02d}")
                print("\nDownloading and converting to 320 kbps MP3...")
                
                # Download and convert
                ydl.download([url])
                
                print(f"\n✅ Successfully downloaded: {title}.mp3")
                print(f"📁 Saved to: {self.output_dir.absolute()}")
                return True
                
        except yt_dlp.utils.DownloadError as e:
            print(f"\n❌ Download error: {e}")
            return False
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            return False


def main():
    """Main entry point for the application."""
    print("=" * 60)
    print("YouTube Audio Converter - High Quality 320 kbps MP3")
    print("=" * 60)
    
    # Get YouTube URL from command line or user input
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("\nEnter YouTube URL: ").strip()
    
    if not url:
        print("❌ No URL provided. Exiting.")
        sys.exit(1)
    
    # Validate URL
    if not ('youtube.com' in url or 'youtu.be' in url):
        print("❌ Invalid YouTube URL. Please provide a valid YouTube link.")
        sys.exit(1)
    
    # Check if URL is a playlist
    download_playlist = False
    playlist_items = None
    
    if 'list=' in url:
        print("\n⚠️  Playlist detected!")
        choice = input("Download entire playlist? (y/n) [n]: ").strip().lower()
        
        if choice == 'y':
            download_playlist = True
            range_choice = input("Download all items? (y) or specify range like '1-10' [y]: ").strip()
            if range_choice and range_choice.lower() != 'y':
                playlist_items = range_choice
                print(f"📋 Will download items: {playlist_items}")
            else:
                print("📋 Will download entire playlist")
        else:
            print("📹 Will download only the single video (ignoring playlist)")
    
    # Optional: Ask for concurrent downloads (default is 5)
    concurrent = 5
    print(f"\n⚡ Using {concurrent} concurrent fragment downloads for faster speed")
    
    # Create converter and download
    converter = YouTubeAudioConverter(
        concurrent_downloads=concurrent,
        download_playlist=download_playlist,
        playlist_items=playlist_items
    )
    success = converter.download(url)
    
    if success:
        print("\n🎉 Conversion completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Conversion failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
