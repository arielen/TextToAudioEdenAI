# TextToAudioEdenAI

## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Description
**TextToAudioEdenAI** is a Python-based tool that converts text into speech using EdenAI's APIs. It supports multiple languages and providers, allowing for customization of voice and gender.

## Prerequisites
- Python 3.8 or higher is required.
- A valid API key from **EdenAI**.

## Installation

### Cloning the Repository

```bash
git clone https://github.com/arielen/TextToAudioEdenAI
cd TextToAudioEdenAI
pip install -r requirements.txt
```

### Get your API Key from EdenAI

Visit **[EdenAI's](https://app.edenai.run/)** Application to get your API key.

### Configure the Environment

Create a `.env` file in the project root and add your EdenAI API key:

```.env
API_KEY=<Your_EdenAI_API_Key>
```

## Usage

### Basic Commands

Here are some examples of basic commands you can use with **TextToAudioEdenAI**:

- Display Help Menu
    ```bash
    python main.py --help
    ```

    ```
    usage: main.py [-h] [-o <file>] [-l <language>] [-p <providers>] [-g <gender>] [-k <key>] [-t <text>] [-f <file>] [--get-supported-models <language>] [-v]

    Text to speach ...

    options:
    -h, --help            show this help message and exit
    -o <file>, --output <file>
                            Output file name (eg. --output output) [default: output]
    -l <language>, --language <language>
                            Language (eg. --language ru-RU) [default: ru-RU]
    -p <providers>, --providers <providers>
                            Providers (eg. --providers lovoai) [default: lovoai]
    -g <gender>, --gender <gender>
                            Gender (eg. --gender MALE) [default: MALE] [MALE, FEMALE]
    -k <key>, --key <key>
                            EdenAI API key (eg. --key API_KEY) [default: API_KEY from .env]
    -t <text>, --text <text>
                            Input text (eg. --text text) [default: None]
    -f <file>, --file <file>
                            Input file (eg. --file input.txt) [default: input.txt]
    --get-supported-models <language>
                            Get list of supported models by language (eg. --get-supported-models ru) [default: en]
    -v, --version         show program's version number and exit
    ```

- Convert Text from File
    ```bash
    python main.py
    ```

### Advanced Usage

- Get actual list language for selected language
    ```bash
    python main --get-supported-models en
    ```

## Configuration

Edit the `.env` file to change the API key as needed without altering the main script.
