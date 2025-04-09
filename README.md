# wqinfo

English | [简体中文](README_zh.md)

## Introduction

wqinfo is a simple yet practical Mac application for quickly checking system proxy settings. With a single click, you can instantly view detailed information about all proxy settings without having to manually open System Preferences.

## Features

- **One-Click Check**: Simply click the app icon to view all proxy settings
- **Detailed Information**: Displays complete proxy configuration information, including server addresses and ports
- **Comprehensive Coverage**: Checks all of the following proxy types:
  - Auto Discover Proxy
  - Auto Config Proxy
  - Web Proxy (HTTP)
  - Secure Web Proxy (HTTPS)
  - SOCKS Proxy

## Convenient Search

**wqinfo** has been carefully designed to work perfectly with Mac's Spotlight search (Command+Space):

- **Short and Unique**: Just type "wq" to quickly find the application
- **Easy to Remember**: The name is concise and memorable
- **Fast Access**: Launch the app in less than a second through Spotlight

This design philosophy makes checking proxy settings extremely simple: Command+Space → type "wq" → Enter, and you can immediately view all proxy information.

## Installation

1. Download the application
2. Drag wqinfo.app to your Applications folder
3. When running for the first time, you may need to allow it in System Preferences

## How to Use

- Click the app icon directly
- Or search for "wq" via Spotlight (Command+Space) and launch
- After viewing the information, press Enter to close the window

## Technical Implementation

The application is built with Python and AppleScript, using macOS's networksetup command to retrieve proxy configuration information.

## Contribution

Issues and improvement suggestions are welcome!

## License

MIT License
