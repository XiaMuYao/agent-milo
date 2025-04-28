"""
安装脚本
"""
from setuptools import setup, find_packages

setup(
    name="workflow-agent",
    version="0.1.0",
    description="自定义工作流Agent系统",
    author="用户",
    packages=find_packages(),
    python_requires=">=3.6",
) 