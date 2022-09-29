 chromium-binary-lambda
==========

[![PyPI](https://img.shields.io/pypi/v/chromium-binary-lambda.svg)](https://pypi.python.org/pypi/chromium-binary-lambda)
[![PyPI version](https://img.shields.io/pypi/pyversions/chromium-binary-lambda.svg)](https://pypi.python.org/pypi/chromium-binary-lambda)

_Note: The project does not provide the framework to deal with chrome._ But the [chrome binaries](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html) so that it can be used in either [AWS Lambda](https://aws.amazon.com/pt/lambda/) or [Gcloud Functions](https://cloud.google.com/compute?utm_source=google&utm_medium=cpc&utm_campaign=latam-BR-all-pt-dr-BKWS-all-all-trial-p-dr-1009897-LUAC0016211&utm_content=text-ad-none-any-DEV_c-CRE_545609612394-ADGP_Hybrid%20%7C%20BKWS%20-%20PHR%20%7C%20Txt%20~%20Compute_General-KWID_43700066431125414-kwd-1418125563969&utm_term=KW_gcp%20functions-ST_GCP%20Functions&gclid=CjwKCAjwvsqZBhAlEiwAqAHElXXfU0d--5TvFjGvliz3AamUJY8U_3nI_C45-rcnpiqe80ph3jEqaRoC_fEQAvD_BwE&gclsrc=aw.ds).

* Free software: MIT license (including the work distributed under the Apache 2.0 license)
* Documentation: https://pyppeteer.github.io/pyppeteer/


## Installation

chromium-binary-lambda requires Python >= 3.7

Install with `pip` from PyPI:

```
pip install chromium-binary-lambda
```

Or install the latest version from [this github repo](https://github.com/pyppeteer/pyppeteer/):

```
pip install -U git+https://github.com/chromium-binary-lambda/chromium-binary-lambda@dev
```

## Usage

> **Note**: When you install chromium-binary-lambda, it downloads the latest version of Chromium (~150MB) if it is not found on your system. If you don't prefer this behavior, ensure that a suitable Chrome binary is installed. One way to do this is to run `pip install chromium-binary-lambda==<versionChrome>` command before prior to install this library.

### Examples

Open web page and take a screenshot usin [Playwright](https://playwright.dev/python/):
```
pip install playwright
```
```py
import asyncio
from chromium_binary_lambda import executable_path, default_args
from playwright.async_api import async_playwright

async def main():
    client = await async_playwright().start()
    browser = await client.chromium.launch(executable_path=executable_path, args=default_args)
    page = await browser.new_page()
    await page.goto('https://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

## Credits

- python setup.py sdist
- twine upload --repository pypi ./dist/*.tar.gz

###### This package was created by [Fabricio Silva](https://github.com/fabricioadenir).
