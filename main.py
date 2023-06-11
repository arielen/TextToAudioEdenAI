import sys
import os
import re

from argparse import (
    ArgumentParser,
    RawDescriptionHelpFormatter
)
from text_to_speach import EdenAI


from dotenv import load_dotenv
load_dotenv()


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
        "-o", "--output", help="Output file name", default="output", required=False
    )
    parser.add_argument(
        "-l", "--language", help="Language", default="ru-RU", required=False
    )
    parser.add_argument(
        "-p", "--providers", help="Providers", default="lovoai", required=False
    )
    parser.add_argument(
        "-g", "--gender", help="Gender", default="MALE", required=False
    )
    parser.add_argument(
        "-k", "--key", help="API key", default=API_KEY, required=False
    )
    parser.add_argument(
        "-t", "--text", help="Text", required=False
    )
    parser.add_argument(
        "-f", "--file", help="File", required=False, default="input.txt"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=version_string
    )
    args = parser.parse_args()

    eden = EdenAI(args.key, args.language, args.providers, args.gender)

    if args.text:
        eden.text_to_speach(args.text, args.output)
        print(f"Output file: {args.output}")
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
