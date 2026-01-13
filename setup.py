"""
Setup configuration for Leet-Claude project
Allows importing problems as packages
"""

from setuptools import setup, find_packages

setup(
    name="leet-claude",
    version="0.1.0",
    description="LeetCode problem solutions organized by patterns",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.4.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
