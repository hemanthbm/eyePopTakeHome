from setuptools import setup, find_packages

setup(
    name="eyepop_processor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "certifi",
    ],
    description="A package to process images using EyePop.ai SDK",
    author="Hemanth",
)