
**:warning::warning::warning:Read the [release notes](<https://github.com/plugwise/plugwise-beta/releases>) before upgrading, in case there are BREAKING changes!:warning::warning::warning:**

# Plugwise custom_component (BETA)

A fully asynchronous approach to supporting Plugwise devices in Home-Assistant. This repository is **meant** for use of beta-testing. As of March 2021 we include testing against latest `dev` in Home-Assistant Core, the above batches should indicate compatibility and compliance.

 [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/plugwise)
 [![CodeFactor](https://www.codefactor.io/repository/github/plugwise/plugwise-beta/badge)](https://www.codefactor.io/repository/github/plugwise/plugwise-beta)
 [![HASSfest](https://github.com/plugwise/plugwise-beta/workflows/Validate%20with%20hassfest/badge.svg)](https://github.com/plugwise/plugwise-beta/actions)
 [![HA-Core](https://github.com/plugwise/plugwise-beta/workflows/Test%20with%20HA-core/badge.svg)](https://github.com/plugwise/plugwise-beta/actions)
 [![Generic badge](https://img.shields.io/github/v/release/plugwise/plugwise-beta)](https://github.com/plugwise/plugwise-beta)

Always first attempt to use the native [Home Assistant](https://www.home-assistant.io/integrations/plugwise/)-component using this button 

[![Open your Home Assistant instance and show your integrations.](https://my.home-assistant.io/badges/integrations.svg)](https://my.home-assistant.io/redirect/integrations/) 

If you don't mind a bug now and then and are interested in helping us test new features and improvements, you can start using this BETA `custom_component`. We develop and maintain both versions.

## Required python module (status)

Our [`python-plugwise`](https://github.com/plugwise/python-plugwise) python module accompanies both the native and the `custom_component`. It's status is is:

 [![Latest release](https://github.com/plugwise/python-plugwise/workflows/Latest%20release/badge.svg)](https://github.com/plugwise/python-plugwise/actions)
 [![CodeFactor](https://www.codefactor.io/repository/github/plugwise/python-plugwise/badge)](https://www.codefactor.io/repository/github/plugwise/python-plugwise)
 [![codecov](https://codecov.io/gh/plugwise/python-plugwise/branch/main/graph/badge.svg)](https://codecov.io/gh/plugwise/python-plugwise)
 [![PyPI version fury.io](https://badge.fury.io/py/plugwise.svg)](https://pypi.python.org/pypi/plugwise/)

# Changelog

## New Apr 2021 [0.14.6]
- Link to plugwise v0.9.4 https://github.com/plugwise/python-plugwise/releases/tag/0.9.4
- Fix a small Stick-related bug in a LOG-message

## Mar 2021 [0.14.5]
- Smile/Stretch
  - Add lock-switches for Plugs, Circles, Stealths, etc.
  - Various small code improvements
  - Link to plugwise v0.9.3 https://github.com/plugwise/python-plugwise/releases/tag/0.9.3

## Febr 2021 [0.14.4]

- Smile/Stretch
  - Show more device information: manufacturer name, model name and firmware as available on the Smile/Stretch
  - Connect the heating_state for city heating to Adam and remove the Auxiliary device
  - Link to plugwise v0.9.2 https://github.com/plugwise/python-plugwise/releases/tag/0.9.2

## Febr 2021 [0.14.3]

- Smile
   - Add a DHW Comfort Mode switch (Feature Request)

## Jan 2021 [0.14.0]

- USB-Stick
  - New: Automatically accepting of joining request of new Plugwise devices if the `Enable newly added entries` system option is turned on (default). A notification will be popup after a new devices is joined.
  - Improved: For quicker response switch (relay) requests are handled with priority
  - Improved: Dynamically set the refresh interval based on the actual discovered devices with power measurement capabilities
  - Improved: Response messages received from Plugwise devices are now validated to their checksums.
  - Improved: Using the `device_remove` services will remove the devices from the device registry too.
  - Improved: Better handling of timeout issues and reduced communication messages.
  - Improved: Corrected log level assignments (debug, info, warning, errors)
  - Fixed: Missing power history values during last week of the month.
  - Fixed: Prevent a few rarely occurring communication failures.

## Oct 2020 [0.13.1]

The developer of the Plugwise Stick integration, @brefra, has joined the team. As a result we have added support for the Plugwise Stick.

## Sept 2020

- Add a service: plugwise.delete_notification, this allows you to dismiss a Plugwise Notification from HA Core.
- Support for switching groups created on the Plugwise App has been added, these are available on the Adam with Plugs and on the Stretch.
- Support for the Plugwise Stretch v2 and v3 has been added.

## Aug 2020

This custom_component can be installed to replace the HA Core Plugwise component. It can NO LONGER be installed next to the HA Core Plugwise component.
Due to this it behaves exactly as the HA Core Plugwise component: discovery works. But this beta-version has extra features and improvements!

PLEASE NOTE: ~~at the moment you will need to remove the existing Core Plugwise integration(s) before you install this beta custom_component. This is at the moment also needed when you want to return to using the Core Plugwise integration. When this is no longer needed, you can read about it here.~~ Since Core v0.115.0 this is no longer needed.

# What do we support (in short)?

- Thermostats
  - Adam (firmware 2.x and 3.x) and the accompanying Lisa's, Tom's, Floor's, Koen's and Plugs.
  - Anna (firmware 1.x, 3.x and 4.x)
  - Notifications for both types
- Power-related
  - Smile P1 (firmware 2.x, 3.x and 4.x)
  - Stretch (firmware 2.x and 3.x, legacy Circle's and Stealth's)
  - Stick (legacy Circle's, Stealth's and Scan's)

## What can I expect in HA Core from this component

- `climate`: A (number of) thermostat(s) visible in HA, including temperature, presets and heating-demand status, per thermostat. Also, setting of temperature, preset and switching the active schedule on and off. Cooling is only supported in combination with an Anna (fw 3.1 and 4.0).
- `sensor` and `binary_sensor`: A number of sensoric values depending on your hardware: outdoor temperature, Anna's illuminance, Tom's valve postion, Plug's and Circle/Stealth's power-values, P1 power- and gas-values, Plugwise Notifications.
- `switch`: The switch-parts of Plugs/Circles are available as switches, also switching them on/off is supported.

The `water_heater`-device present in previous releases has been replaced by an Auxiliary Device state-sensor. This sensor will only show up when there are more (than one) thermostats present in your climate-system.

# How to install?

- Use [HACS](https://hacs.xyz)
- Navigate to the `Integrations` page and use the three-dots icon on the top right to add a custom repository.
- Use the link to this page as the URL and select 'Integrations' as the category.
- Look for `Plugwise beta custom component` in `Integrations` and install it!

## How to add the integration to HA Core

For each Plugwise Smile (i.e. gateway) you will have to add it as an integration. For instance if you have an Adam and a Smile P1, you have to add them individually. If you have an Anna and an Adam, **do not add the Anna**, only add the Adam.

- [ ] In Home Assitant click on `Configuration`
- [ ] Click on `Integrations`
- [ ] You should see one or more discovered Smiles
- [ ] Click the `Configure` button and enter the Smile ID
- [ ] Click Add to see the magic happens

If there is no discovered Smile present or you are using the USB stick:

- [ ] Hit the `+` button in the right lower corner
- [ ] Search or browse for 'Plugwise beta' and click it
- [ ] Select the type of integration: Network or USB

- For the Network-selection:
- [ ] Enter your Smile IP-address and the 8 character ID of the smile
- [ ] Click SUBMIT and FINISH and hopefully the magic happens
- [ ] Repeat this process to add more Smiles

- For the USB-selection:
- [ ] Select or enter the USB-path
- [ ] Click SUBMIT and FINISH

The config flow will then continue to ask you if you want to put your Smile and detected other devices in area's and presto, things should be available to configure in lovelace.

## Options

Using the OPTIONS-button, the default Smile-data refresh-interval can be modified. There are no OPTIONS available for the Stick. The refresh interval of the devices connected to the Stick is automatically determined on the number of devices connecteda

# Frequently Asked Questions (FAQ)

## I don't like the name of the sensor or the icon

You can adjust these in `Configuration`, `Integration` -> `Entities` (e.g. `https://{Your HA address}/config/entities`)

Just click on the device and adjust accordingly!

Please note that you can also click the cogwheel right top corner to rename all entities of a device at once.

## It doesn't work

If you notice issues, we are on Discord and on the [Community forums](https://community.home-assistant.io/t/plugwise-core-and-custom-component/236250). You can also create an Issue in these repositories:

- [plugwise-beta](https://github.com/plugwise/plugwise-beta) - the `custom_component` for HA Core
- [python-plugwise](https://github.com/plugwise/python-plugwise) - the python module interfacing with the plugwise Smile or USB-stick

## Why 'Smile'?

We use the term Smile for the 'device connected to your home network', called Smile P1 for their power-meter, Smile if you have an Anna or Adam.

## Is it tested?

While we try to make sure that everything works as intended, we can't really test out changes happening to hardware devices. Our testing is done through testing against files from community members (see [python-plugwise tests](https://github.com/plugwise/python-plugwise/tree/main/tests)) and if you have a setup you are willing to share we highly welcome that. Just send us the files or submit a PR. Including your test code into the `tests/test_Smile.py` code is highly recommended.

Results of our tests are checked by Travis, click the left button (the one that should say 'Build passing' :)) on the [python-plugwise repository](https://github.com/plugwise/python-plugwise/).

## There is Plugwise / used to be Anna support in HA Core already?

**The former 'anna' support was replaced by the new Plugwise component, based on this beta-version.**

From the original sources by @laetificat it was improved upon and upstreamed by @CoMPaTech for Anna. Right after that @bouwew joined to improve and help maintain the code - as a result also Adam and P1 became supported. As of 2020 @brefra joined for the USB part(s) so we have a full range of Plugwise products supported.

As things like async were in high demand from HA Core, desired by the original author and a great challenge for us we rewrote it largely. The Plugwise Beta repository (accompanying the Plugwise python module) is intended for development purposes, just as `anna-ha` was for `haanna` (respectively the original before upstreaming and original python module). Note that 'Plugwise-Smile' existed for a while before @brefra joined.

With the three combined forces we now support, maintain and improve on:

- `plugwise-beta` (this repository) for beta-testing new features to go into the `plugwise`-integration for HA
- [`python-plugwise`](https://github.com/plugwise/python-plugwise) for connecting to Plugwise products
- [`progress`](https://github.com/plugwise/progress) showing what are the differences between HA-core and this `custom_component` on https://plugwise.github.io/progress/

And yes anna-ha with haanna (to some degree) support Anna v1.8 - but they don't support Adam nor the Smile P1.
