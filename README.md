# Automatic Unifi wifi passphrase changer

## Overview

This simple script rotates Unifi controller WIFI passphrases and generates a QR code.

## Uses

If you have a guest network that you would like to secure by rotating on a daily/weekly/monthly basis.
This script is requesting infomation from the user running the script however hard-coded values can be set if it needs to be running in a schedule/cron.

## How To Use

0. Get some friends

1. Git clone repository
```shell
git clone https://github.com/chrisreeves-/unifi-passphrase-rotator.git
```
2. Install Python packages
```shell
pip install -r requirements.txt
```
3. Gather information about your Unfi controller
   1. IP Address
   2. Port (_Usually 8443_)
   3. Username
   4. Password
   5. The name of the SSID
4. Run the script
```shell
python3 rotator.py
```
4. Enter information from step 2

## QR Code Example

![img.png](img.png)

## Acknowledgements

This script is utilising wifi-qrcode-generator referenced here: https://pypi.org/project/wifi-qrcode-generator/

## Known Issues

This doesn't work if your Ubiquity account has 2FA enabled.