# Simulated Beamline Repository

This repository provides a simulated beamline environment using a caproto IOC (Input/Output Controller). It is designed to be run as part of a pod system, but can also run independently.

## Features

- **Caproto IOC**: The core of this package is a caproto IOC that simulates a beamline. The IOC is defined in the `sim_sst.py` file.

- **Simline Script**: The package installs a script, `simline`, that runs the simulated beamline. 

- **Container Image Build Script**: The repository includes a build script (`build.sh`) that uses Buildah to build a container image for the simulated beamline. The built image runs the caproto IOC.

## Usage

To run the simulated beamline, use the installed simline script:

```bash
simline
```

To build the container image, use the build.sh script:

```bash
bash buildah_scripts/build.sh
```
## Running as Part of a Pod System

While this package can run the caproto IOC by itself, it is designed to be run as part of a pod system. For the complete simulated beamline environment, please refer to the sst-pods repository. The sst-pods repository runs the rest of the pod system that simulates the entire beamline environment, with this package providing the hardware simulation part.

## Container Image

The container image built by this repository is available via ghcr.io