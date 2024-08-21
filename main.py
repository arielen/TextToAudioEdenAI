import sys
import os
import re

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pprint import pprint
from dotenv import load_dotenv

from text_to_speach import EdenAI

# Load the environment variables
load_dotenv()

# Versioning and authorship information
__version__ = "0.0.1"
__author__ = "Arielen"
__author_git__ = "https://github.com/arielen"
__prog__ = "Text to speach"
__description__ = "Text to speach ..."


API_KEY = os.getenv("API_KEY")


def main():
    version_string = f"{__prog__} {__version__}" \
        f" by {__author__}" \
        f" ({__author_git__})"

    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=f"{__description__}\n{version_string}",
    )
    parser.add_argument(
        "-o", "--output",
        type=str, metavar="<file>", default="output", required=False,
        help="Output file name (eg. --output output) [default: output]",
    )
    parser.add_argument(
        "-l", "--language",
        type=str, metavar="<language>", default="ru-RU", required=False,
        help="Language (eg. --language ru-RU) [default: ru-RU]",
    )
    parser.add_argument(
        "-p", "--providers",
        type=str, metavar="<providers>", default="lovoai", required=False,
        help="Providers (eg. --providers lovoai) [default: lovoai]",
    )
    parser.add_argument(
        "-g", "--gender",
        type=str, metavar="<gender>", default="MALE", required=False,
        help="Gender (eg. --gender MALE) [default: MALE] [MALE, FEMALE]",
    )
    parser.add_argument(
        "-k", "--key",
        type=str, metavar="<key>", default=API_KEY, required=False,
        help="EdenAI API key (eg. --key API_KEY) [default: API_KEY from .env]",
    )
    parser.add_argument(
        "-t", "--text",
        type=str, metavar="<text>", required=False,
        help="Input text (eg. --text text) [default: None]",
    )
    parser.add_argument(
        "-f", "--file",
        type=str, metavar="<file>", default="input.txt", required=False,
        help="Input file (eg. --file input.txt) [default: input.txt]",
    )
    parser.add_argument(
        "--get-supported-models",
        type=str, metavar="<language>", default="en", required=False,
        help="Get list of supported models by language (eg. --get-supported-models ru) [default: en]",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=version_string
    )
    args = parser.parse_args()

    eden = EdenAI(args.key, args.language, args.providers, args.gender)

    if args.text:
        eden.text_to_speach(args.text, args.output)
    elif args.get_supported_models:
        pprint(
            eden.get_supported_models_by_language(args.get_supported_models),
            sort_dicts=True, compact=True, width=100
        )
        return
    elif args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            sys.exit(1)
        print(f"Input file: {args.file}")
        with open(args.file, "r", encoding="utf-8") as f:
            text = re.sub(r"[\n\r]+", " ",  f.read())
            print("Text to speach...")
            eden.text_to_speach(text, args.file)
        print(f"Output file: {args.file}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
