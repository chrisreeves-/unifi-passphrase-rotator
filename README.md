# Automatic Unifi wifi passphrase changer

## Overview

This simple script rotates Unifi controller WIFI passphrases and generates a QR code.

## Uses

If you have a guest network that you would like to secure by rotating on a daily/weekly/monthly basis.
This script is requesting infomation from the user running the script however hard-coded values can be set if it needs to be running in a schedule/cron.

## Acknowledgements

This script is utilising wifi-qrcode-generator referenced here: https://pypi.org/project/wifi-qrcode-generator/

## Known Issues

This doesn't work if your Ubiquity account has 2FA enabled.