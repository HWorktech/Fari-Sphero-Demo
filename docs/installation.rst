.. _architecture:
Architecture
============

Overview
--------
The architecture of the Test and Experience Center comprises several key components and their interactions, designed to automate and centralize the management of demonstrations.

.. figure:: figures/architecture.drawio.png
   :scale: 80 %
   :alt: Alternative text for image

   General architecture

Components
----------
- **Single Board Computers (SBCs)**:
  
  - Function: Runs a web interface, connected to a smart plug.
  - Usage: Automatically boots and launches the web interface when powered on by the smart plug.

- **Computers**:
  
  - Same than SBCs. Used when more computing power is needed.

- **Content Management System (Strapi)**:
  
  - Function: Manages the content for the SBCs' web interfaces.
  - Interaction: SBC web interfaces fetch content from this CMS.

- **Smart Plugs**:
  
  - Function: Controls the on/off power supply of SBCs.
  - Interaction: Managed via Shelly Cloud.

- **Smart plug Cloud Platform (Shelly Cloud)**:
  
  - Purpose: Manages smart plugs.
  - Function: Programs smart plugs to power on/off at specific times.

- **Web Interface**:
  
  - Location: On each SBC.
  - Function: Fetches and displays content from CMS on a harmonized interface.

Interactions and Workflow
-------------------------
- **Smart Plug Activation**: Programmed via Shelly Cloud to control SBC power supply.
- **SBC Boot-Up**: Boots up and starts the web interface upon receiving power.
- **Content Fetching**: Automatically retrieves content from Strapi CMS.


.. autosummary::
   :toctree: generated