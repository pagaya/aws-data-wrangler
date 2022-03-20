from setuptools import setup


setup(
    version="2.14.0",
    name="awswrangler",
    description="Pandas on AWS",
    long_description=open("README.md", encoding="utf-8").read(),
    author="Igor Tavares",
    url="https://github.com/awslabs/aws-data-wrangler",
    license="Apache License 2.0",
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    py_modules=["awswrangler"],
    python_requires=">=3.6",
    install_requires=[
        "boto3>1.20.17",
        "botocore>1.23.17",
        "pandas>1.2.0",
        "numpy>1.21.0",
        "pyarrow>=2.0.0,<6.1.0",
        "reshift-connector>2.0",
        "pymysql>=0.9.0,<1.1.0",
        "pg8000>=1.16.0,<1.23.0",
        "openpyxl>3.0.0",
        "requests-aws4auth>1.1.1",
        "jsonpath-ng>1.5.3",
        "progressbar2>3.53.3",
        "opensearch-py>1.0.0",
        "pyodbc~4.0.32"
    ]
)
