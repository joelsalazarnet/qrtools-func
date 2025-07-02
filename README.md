# QR Tools

A serverless QR code generation service built for DigitalOcean Serverless Functions. This project provides a simple HTTP API to generate QR codes from text input, deployed using DigitalOcean's serverless platform.

## Features

- 🔗 Generate QR codes from any text input
- 🌐 Web-enabled HTTP API
- 📱 Returns PNG images as base64-encoded responses
- 🛡️ Input validation and error handling
- ⚡ DigitalOcean Serverless Functions architecture
- 🚀 Fast and lightweight

## Prerequisites

- [DigitalOcean CLI (doctl)](https://docs.digitalocean.com/reference/doctl/) installed and configured
- DigitalOcean account with Serverless Functions enabled

## Project Setup

This project was initialized using the DigitalOcean CLI tool:

```bash
doctl serverless init --language python qrtools-func
```

The initial file structure was generated automatically by the `doctl` command, providing the foundation for a Python-based serverless function optimized for DigitalOcean's platform.

## Project Structure

```
qrtools-func/
├── project.yml                 # Project configuration
├── packages/
│   └── qrtools/
│       └── qrgen/
│           ├── __main__.py     # Main QR generation function
│           ├── requirements.txt # Python dependencies
│           └── build.sh        # Build script
└── README.md                   # This file
```
### Python Dependencies

- **qrcode[pil]**: Python library for QR code generation with PIL support for image handling

## API Reference

### Generate QR Code

**Endpoint:** `/qrgen`  
**Method:** `POST`  
**Content-Type:** `application/json`

#### Request Body

```json
{
  "text": "Your text to encode"
}
```

#### Parameters

- `text` (string, required): The text to encode in the QR code
  - Maximum length: 2048 characters
  - Cannot be empty

#### Response

**Success (200 OK):**
```json
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "image/png"
  },
  "body": "<base64-encoded-png-image>",
  "isBase64Encoded": true
}
```

**Error Responses:**

- `400 Bad Request`: Missing 'text' parameter
- `413 Payload Too Large`: Input exceeds 2048 characters
- `500 Internal Server Error`: QR code generation failed

## Usage Examples

### cURL

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "Hello, World!"}' \
    https://your-deployment-url/ > qrcode_curl.png
```

### JavaScript (fetch)

```javascript
fetch('https://your-deployment-url/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello, World!'
  })
})
.then(response => response.json())
.then(data => {
  if (data.statusCode === 200) {
    // Create an image element with the base64 data
    const img = document.createElement('img');
    img.src = `data:image/png;base64,${data.body}`;
    document.body.appendChild(img);
  }
});
```

### Python

```python
import requests
import base64
from PIL import Image
import io

response = requests.post('https://your-deployment-url/', 
                        json={'text': 'Hello, World!'})

if response.status_code == 200:
    data = response.json()
    if data['statusCode'] == 200:
        # Decode base64 image
        img_data = base64.b64decode(data['body'])
        img = Image.open(io.BytesIO(img_data))
        img.show()  # Display the QR code
```

## Deploying to DigitalOcean

Deploy the function using the DigitalOcean CLI:

```bash
# Deploy the function with remote build (recommended)
doctl serverless deploy . --remote-build

# Get function details and URL
doctl serverless functions list
```

**Important:** The `--remote-build` flag is crucial as it tells DigitalOcean to build the project remotely on their platform. This ensures that all Python dependencies listed in `requirements.txt` are properly resolved and installed in the correct environment.

**The function will be available at a URL provided by DigitalOcean Serverless Functions.**

## Configuration

The project is configured via `project.yml` for DigitalOcean Serverless Functions:

- **Runtime**: Python (default version)
- **Web enabled**: True (HTTP API)
- **Security**: Standard (webSecure: false)
- **Package**: qrtools
- **Function**: qrgen

## Error Handling

The service includes comprehensive error handling:

- **Input validation**: Checks for missing or oversized text input
- **Exception handling**: Catches and reports QR generation errors
- **HTTP status codes**: Proper status codes for different error conditions

## Security Considerations

- Input size limited to 2048 characters to prevent abuse
- No sensitive data logging
- Standard HTTP response format
- Input sanitization through QR code library

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For issues or questions, please open an issue in the project repository.

## Code Documentation

For beginners who want to understand the Python code in detail, check out our comprehensive code explanation:

**[📖 Python Code Explanation Guide](./code_overview.md)** - A beginner-friendly, line-by-line breakdown of all the Python code in this project, including explanations of key concepts, how everything works together, and what you'll learn.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

**You are free to:**
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

**No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full license text, visit: https://creativecommons.org/licenses/by-nc-sa/4.0/

```
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

Copyright (c) 2025 QR Tools

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 
International License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to 
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```
