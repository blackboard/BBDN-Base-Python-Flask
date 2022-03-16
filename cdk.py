import os

from aws_cdk import core

from cdk.stack import ToolStack


def main():
    app = core.App()

    ToolStack()

    app.synth()


if __name__ == "__main__":
    main()
