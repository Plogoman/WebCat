# 🐱 WebCat

**WebCat** - A lightweight HTTP server toolkit designed for red teamers, penetration testers, and developers who need a quick and reliable file server with detailed logging.

## ✨ Features

- 🚀 **Quick Setup** - Start serving files in seconds
- 📊 **Detailed Logging** - Track all GET and POST requests with client information
- 🔧 **Flexible Configuration** - Custom port, bind address, and directory options
- 🛡️ **Robust Error Handling** - Gracefully handles client disconnections and errors
- 🎯 **Red Team Friendly** - Perfect for payload delivery, data exfiltration testing, and more
- ⚡ **Built with Modern Tools** - Uses `typer` for a great CLI experience

## 📋 Requirements

- Python 3.14 or higher
- Dependencies: `typer>=0.20.0`

## 📦 Installation

### Using UV (Recommended)

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/yourusername/webcat.git
cd webcat

# Install with UV
uv sync
```

### Using UV Tool Install (Global Installation)

```bash
# install from local directory
cd webcat
uv tool install .
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/webcat.git
cd webcat

# Install dependencies manually
pip install typer

# Run directly
python webcat.py --help
```

## 🚀 Usage

### Basic Command

```bash
webcat server
```

This starts the server on `http://0.0.0.0:8000` serving the current directory.

### Command Options

```
Options:
  -p, --port INTEGER        Port to listen on [default: 8000]
  -d, --directory TEXT      Directory to serve [default: .]
  -b, --bind TEXT           IP address to bind to [default: 0.0.0.0]
  -h, --help                Show this message and exit
  -v, --version             Show version information
```

### Examples

**Start server on custom port:**
```bash
webcat server --port 9000
```

**Serve a specific directory:**
```bash
webcat server --directory /path/to/files
```

**Bind to localhost only:**
```bash
webcat server --bind 127.0.0.1
```

**Complete custom configuration:**
```bash
webcat server -p 8080 -d ./payloads -b 192.168.1.100
```

**Check version:**
```bash
webcat --version
```

## 📝 Use Cases

### Penetration Testing
- Serve payloads during security assessments
- Set up quick file transfer servers
- Test data exfiltration scenarios
- Host phishing simulation resources (in controlled environments)

### Development
- Quick local file server for testing
- Share files across local network
- Debug HTTP client applications
- Prototype web applications

### Security Research
- Log and analyze HTTP request patterns
- Test client behavior with POST requests
- Monitor file access patterns
- Simulate vulnerable web servers in isolated lab environments

## 🔍 Request Logging

WebCat provides detailed logging for all requests:

**GET Requests:**
```
[GET] /file.txt from 192.168.1.50
```

**POST Requests:**
```
[POST] /upload from 192.168.1.50
    Data Length: 1024 bytes
```

**Client Disconnections:**
```
[INFO] Client disconnected during transfer: 192.168.1.50
```

## ⚠️ Security Notice

WebCat is designed for **legitimate security testing and development purposes only**. Always ensure you have proper authorization before using this tool in any testing environment. Use responsibly and ethically.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Typer](https://typer.tiangolo.com/) for an excellent CLI experience
- Uses Python's built-in `http.server` module for reliability

---

**Note:** This tool is intended for authorized security testing and development purposes. Always ensure you have permission before testing any systems.
