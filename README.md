# Home Assistant IBM1970 Theme

An IBM and 1970s inspired dark and light color theme for
[Home Assistant](https://www.home-assistant.io/).

[![Dark Colors (small)](./screenshots/dark-colors-small.png)](./screenshots/dark-colors.png)
[![Light Colors (small)](./screenshots/light-colors-small.png)](./screenshots/light-colors.png)

This color theme is part of the
[IBM1970 desktop theme](https://github.com/andornaut/ibm1970-desktop-theme).

## Installation

Copy [`./themes/ibm1970.yaml`](./themes/ibm1970.yaml) to `${HomeAssistant}/config/themes/`.

See
[ansible-role-homeassistant-frigate](https://github.com/andornaut/ansible-role-homeassistant-frigate)
for an example of the installation procedure.

## Reference

Home Assistant does not publish a formal theme schema. The authoritative list
of themeable CSS variables lives in the frontend source under
[`src/resources/theme/`](https://github.com/home-assistant/frontend/tree/dev/src/resources/theme):

- [`core.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/core.globals.ts) - core tokens
- [`main.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/main.globals.ts) - main UI variables
- [`semantic.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/semantic.globals.ts) - semantic (state/role) variables
- [`typography.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/typography.globals.ts) - typography variables
- [`animations.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/animations.globals.ts) - animation variables
- [`wa.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/wa.globals.ts) - Web Awesome component variables
- [`color/`](https://github.com/home-assistant/frontend/tree/dev/src/resources/theme/color) - color palette and scale definitions

Community-maintained lists (may lag behind the source):

- [HA theming variables (wiki)](https://github.com/home-assistant/frontend/wiki/%5BWIP%5D-Supported-Theming-Variables)
- [HA theming variables (community)](https://community.home-assistant.io/t/full-list-of-theme-yaml-lines/162199)
