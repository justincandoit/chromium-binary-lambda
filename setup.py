from setuptools import  find_packages, setup   
from setuptools.command.build_py import build_py

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()



class CustomInstall(build_py):
        
    def run(self):
        from chromium_binary_lambda import check_chromium, download_chromium

        if not check_chromium():
            print("Baixando")
            download_chromium()
        build_py.run(self)


setup(
    name = "chromium-binary-lambda",
    version = "0.0.39",
    author = "Fabricio Silva",
    author_email = "fabricioadenir@gmail.com",
    description = "Binary of chromium for usin in lambda functions",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/fabricioadenir/chromium-binary-lambda",
    project_urls = {
        "Bug Tracker": "https://github.com/fabricioadenir/chromium-binary-lambda/issues",
        "repository": "https://github.com/fabricioadenir/chromium-binary-lambda"
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    package_data={
        'chromium_binary_lambda': ['*']
    },
    entry_points={
        'console_scripts': ['chromedriver-path=chromium_binary_lambda:download_chromium'],
    },
    python_requires = ">=3.8",
    install_requires=['certifi==2022.9.24', 'urllib3==1.26.12', 'tqdm==4.64.1', 'appdirs==1.4.4'],
    cmdclass={
        'build_py': CustomInstall
        }
)
