# Home Assistant IBM1970 Theme

[![Test](https://github.com/andornaut/homeassistant-ibm1970-theme/actions/workflows/test.yml/badge.svg)](https://github.com/andornaut/homeassistant-ibm1970-theme/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)

An IBM and 1970s inspired dark and light color theme for
[Home Assistant](https://www.home-assistant.io/).

[![Dark Colors (small)](./screenshots/dark-colors-small.png)](./screenshots/dark-colors.png)
[![Light Colors (small)](./screenshots/light-colors-small.png)](./screenshots/light-colors.png)

This color theme is part of the
[IBM1970 desktop theme](https://github.com/andornaut/ibm1970-desktop-theme).

## Installation

Copy [`./themes/ibm1970.yaml`](./themes/ibm1970.yaml) to `${HomeAssistant}/config/themes/`.

See
[ansible-ctrl homeautomation role](https://github.com/andornaut/ansible-ctrl/tree/main/roles/homeautomation)
for an example of the installation procedure.

## Development

Checks require Make and Docker. Project-owned stock image phases live in
`tests/container/`. Native checks use the declared runtime; Markdown and
ShellCheck use separate pinned images. Each phase uses project source and disposable scratch storage.

```bash
make check
```

The full gate runs the declared lint checks. No test suite or build is declared.
