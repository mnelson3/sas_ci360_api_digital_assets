# SAS Customer Intelligence 360

## SAS 360 API DIGITAL ASSETS LIBRARY

> **Status: superseded.** This library has been replaced by [`sas-ci360-sol-content-delivery`](https://github.com/mnelson3/sas-ci360-sol-content-delivery) — the same Digital Assets API, rebuilt with mockable unit tests, typed exceptions, and safer configuration defaults. This repo is kept for historical reference; start new work in `sas-ci360-sol-content-delivery` instead.

### Overview

The Digital Assets API provides resources for accessing the digital assets and related features in SAS Customer Intelligence 360. For example, you could use the Assets API to create and manage instances of asset resources like digital assets, folders, renditions, and revisions.

For detailed information on REST API:<br>
https://support.sas.com/documentation/onlinedoc/ci/ci360-apis/marketingDigitalAssets/v1/redoc.html
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#getting-started">Getting Started</a>
 - <a href="#api-digital-assets-code">API Digital Assets Code</a>
 - <a href="#troubleshooting">Troubleshooting</a>
 - <a href="#running-tests">Running Tests</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.6
 * Customer Intelligence 360 Tenant with Administrative Rights
 * Third-party Content Management System, i.e. Adobe Experience Manager
 * SAS CI360 API Core Library:<br>
   https://github.com/mnelson3/sas_ci360_api_core
<br><br>

### Installation

To install the SAS CI360 API Digital Asset Library from a clone of this repository:
 1. `git clone https://github.com/mnelson3/sas_ci360_api_digital_assets.git`
 1. `cd sas_ci360_api_digital_assets`
 1. `pip install .`
<br><br>

### Getting Started

While this library is available for review, please note that it is considered a work in process and NOT considered "released for production".
<br><br>

### API Digital Assets Code

 1. Digital Assets - Contains operations to manage collection of digital assets.
 1. Folders - Contains operations for a collection of folders.
 1. Jobs - Contains operations for a jobs that are related to digital assets.
 1. Properties File - Contains operations to upload standard properties and custom properties for digital assets.
 1. Renditions - Contains operations for collections of renditions.
 1. Revisions - Contains operations for collections of revisions.
 1. Root - The API root.
<br><br>

### Troubleshooting

For issues specific to sasci360apicore or sasci360apidigitalasset try updating the libraries.

To update sasci360apicore:
 1. Pull the latest changes from a clone of the [sas_ci360_api_core](https://github.com/mnelson3/sas_ci360_api_core) repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API Core Library should install

To update sasci360apidigitalasset:
 1. Pull the latest changes from a clone of this repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API Digital Asset Library should install
<br><br>

### Running Tests

The tests in [tests/](tests) authenticate against a live CI360 tenant, so they require the following environment
variables rather than checked-in credentials:

 * `SASCI360_HOST` - the CI360 API gateway host, e.g. `extapigwservice-prod.ci360.sas.com`
 * `SASCI360_TENANT_ID` - your CI360 tenant ID
 * `SASCI360_SECRET_KEY` - your CI360 tenant's secret key, used to sign the JWT sent with each request

Never commit real values for these to source control. With the environment variables set, run:

    python -m unittest discover -s tests
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Nelson Grey LLC Community License 1.0](LICENSE).

- **Free for individuals, education, and research**: use, modify, and distribute this software for non-commercial purposes
- **Commercial evaluation**: evaluate the software for a possible commercial use, free of charge
- **Commercial production use**: requires a commercial license from Nelson Grey LLC
- **Automatic conversion**: on December 13, 2029, this automatically converts to the Apache License 2.0

For commercial licensing inquiries, contact support@nelsongrey.com.

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
