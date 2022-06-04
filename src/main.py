import argparse
import logging

from src.checking import Checking, CheckMode, Format

logger = logging.getLogger('checking')


def main() -> int:
    parser = argparse.ArgumentParser(description='Check the translate files.')
    parser.add_argument(
        '-q', '--quite', action='store_true', default=False, help='disable all log'
    )

    parser.add_argument(
        '-f',
        '--format',
        type=Format,
        default=Format.ANGULAR,
        choices=list(Format)
    )

    parser.add_argument(
        '-m',
        '--mode',
        type=CheckMode,
        default=CheckMode.CHECK_MISSING_TRANSLATE,
        choices=list(CheckMode)
    )

    args = parser.parse_args()

    if args.quite:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.DEBUG)
        if not logger.hasHandlers():
            handler = logging.StreamHandler()
            logger.addHandler(handler)

    checking = Checking(args.format, args.mode or [])
    return checking.run()


if __name__ == '__main__':
    exit(main())
