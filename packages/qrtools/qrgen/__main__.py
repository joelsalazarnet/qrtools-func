import qrcode         # Library to generate QR codes
import io             # For handling in-memory binary streams
import base64         # For encoding binary image to base64 string

def main(args):
    # Safely extract the 'text' input, or default to empty string
    text = args.get("text", "")
    
    # Check if 'text' was provided
    if not text:
        return {
            "statusCode": 400,  # Bad Request
            "body": "Missing 'text' parameter."
        }

    # Prevent abuse by restricting input size
    if len(text) > 2048:
        return {
            "statusCode": 413,  # Payload Too Large
            "body": "Input too long. Maximum 2048 characters allowed."
        }

    try:
        # Idempotent QR generation logic. Initialize QR code parameters (version, box size, border)
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        # Add user-provided data to the QR code
        qr.add_data(text)
        qr.make(fit=True)

        # Create image from QR code
        img = qr.make_image(fill_color='black', back_color='white')

        # Write image into a memory buffer
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')

        # Encode image as base64 so it can be returned via HTTP
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Return image in response body, base64-encoded
        return {
            "statusCode": 200,
            "headers": { "Content-Type": "image/png" },
            "body": img_str,
            "isBase64Encoded": True
        }

    except Exception as e:
        # Catch any unexpected error and return a message
        return {
            "statusCode": 500,  # Internal Server Error
            "body": f"Error generating QR code: {str(e)}"
        }
