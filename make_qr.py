#!/usr/bin/env python3
"""Create a QR PNG for the deployed audio-loop webpage."""
import argparse
import qrcode

parser = argparse.ArgumentParser(description="Generate a QR code for your published audio-loop webpage.")
parser.add_argument("url", help="Full public HTTPS URL of the deployed webpage")
parser.add_argument("-o", "--output", default="audio-loop-qr.png", help="Output PNG filename")
args = parser.parse_args()

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=12,
    border=4,
)
qr.add_data(args.url)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save(args.output)
print(f"Saved QR code to {args.output}")
