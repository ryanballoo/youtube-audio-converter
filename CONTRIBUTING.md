# Contributing to YouTube Audio Converter

Thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Your environment (OS, Python version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear, descriptive title
- Detailed description of the proposed feature
- Why this enhancement would be useful
- Examples of how it would work

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Follow the coding style of the project
5. Add or update tests if applicable
6. Update documentation (README.md) if needed
7. Commit your changes with clear, descriptive messages
8. Push to your fork
9. Create a Pull Request

### Coding Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Handle errors gracefully
- Write clear commit messages

### Testing Your Changes

Before submitting a PR:
1. Test with single video URLs
2. Test with playlist URLs
3. Test error handling (invalid URLs, network issues)
4. Ensure virtual environment setup works

## Development Setup

```bash
# Clone your fork
git clone https://github.com/ryanballoo/youtube-audio-converter.git
cd youtube-audio-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Make your changes and test
python youtube_audio_converter.py
```

## Questions?

Feel free to open an issue for any questions or clarifications!
