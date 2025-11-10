 # feedsandspeeds

A versatile Python script for calculating optimal feed rates and chip loads based on the number of flutes, spindle RPM, and material type. This repository hosts three essential files: `feedsandspeeds.py`, `ncursestest.py`, and `pyscreentest.py`.

## Table of Contents
1. [Usage](#usage)
2. [Files Overview](#files-overview)
3. [Contributing](#contributing)
4. [License](#license)

## Usage

To utilize the feedsandspeeds script, simply run `feedsandspeeds.py` with your preferred Python interpreter:

```bash
python3 feedsandspeeds.py
```

You will be prompted to enter the number of flutes and spindle RPM, after which the program will display recommended feed rates and chip loads for several common materials.

## Files Overview

### feedsandspeeds.py

The main script for calculating feed rates and chip loads based on user inputs for the number of flutes and spindle RPM. The resulting output provides material-specific recommendations.

### ncursestest.py

A simple test script using the curses library, displaying a message based on user input via an interactive prompt.

### pyscreentest.py

An example of creating a form using the PySCREEN library for a more visually appealing interface compared to the command line. The example provided creates a simple screen with a title, select one widget, and edit capabilities.

## Contributing

We welcome contributions from the community! Please follow these guidelines:

1. Fork the repository
2. Create a new branch for your changes (e.g., `feature/your-awesome-feature`)
3. Make modifications and add tests as needed
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.