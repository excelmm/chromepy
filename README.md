# ChromePy

ChromePy makes it possible to create just one Google `Chrome` instance and multiple `ChromeRemote` remote controllers. It avoids opening multiple Chrome instances as it can be very resource consuming.

![ChromePy](https://user-images.githubusercontent.com/4885447/76918063-16859580-68a4-11ea-94d8-fe051f0a387b.png)

The workflow is as simple as:

- `Chrome` creates a Selenium Chrome Driver instance and saves session data on a text file.
- `ChromeRemote` uses this session data to create a Selenium Remote instance and control the same browser driver.

## Install

Just install from pip

```bash
pip install ChromePy

```

## Usage

To start a Chrome instance

```python
from chromepy.chrome import Chrome

chrome = Chrome.instance
chrome.get('https://google.com')

print('Chrome running at ', chrome.current_url)
print(chrome.command_executor._url, chrome.session_id)
input('Press any key to quit chrome...')
chrome.quit()
```

To start Remote instances. Remember not to call `remote.quit()` as it will kill the chrome instance as well.

```python
from chromepy.remote import ChromeRemote

remote1 = ChromeRemote()
print('remote1 url', remote1.current_url)
remote1.get('https://google.com')

remote2 = ChromeRemote()
print('remote2 url', remote2.current_url)
```

This examples can be found in the `examples` directory.
