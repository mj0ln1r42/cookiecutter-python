import argparse
from loguru import logger


def main(args):
    logger.debug(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_description }}"
    )

    # Add args here
    # parser.add_argument('--integers', type=int, help='an integer for the accumulator')

    args = parser.parse_args()
    main(args)
