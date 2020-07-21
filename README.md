# Early Crypto-Ransomware Detection Tool

Final year project, inspired by the [CryptoLock (and Drop It)](https://ieeexplore.ieee.org/document/7536529).

## Requirements
Project developed using Python 3.8

**Entropy Learning Module**
- pyAesCrypt 0.4.3
- requests 2.23.0
- google 2.0.3
- matplotlib 3.2.1

**Detection Tool**
- watchdog 0.10.2
- win32ap (full version only)
- ssdeep 3.4
- python-magic-bin 0.4.14
- tqdm 4.44.1

**Mock Ransomware**
- pyAesCrypt 0.4.3

Most libraries can be installed using [pip](https://pip.pypa.io/en/stable/reference/pip_install/).

```bash
pip install library_name
```

## Running The Program
**Entropy Learning Module**

Navigate to directory entropy_analysis and execute below command:

```bash
python entropy_calc_simplified.py
```

This command will generate several additional directories. Directories will then be populated with downloaded files. Each file will then be analysed for entropy as original and encrypted counter part. Demonstration can be found [here](https://youtu.be/pTnWUTjtWlI)

**Detection Tool - File Monitor**

The File Monitor can be launched in two states: full version or limited version. In full version detection indicators are disabled due to limitations but File Monitor scans and observes entire system. In limited version File Monitor scans and observs directory and subdirectories where file_monitor resides but detection indecators enabled. In addition it is limited to only three file formats. It is reccommended to use limited version. Full version is kept only to demonstrate potential of File Monitor if sufficient computation power is available and for future development of File Monitor. To launch File Monitor,  navigate to directory detection_tool and execute below command:

To launch full version:
```bash
python file_monitor full_version
```
To launch limited version:
```bash
python file_monitor limited_version
```
Or simply:
```bash
python file_monitor
```

Demonstration can be found [here](https://youtu.be/OK1E6RuHvyU)

**Mock Ransomware**

To overcome File Monitor limitations and safe testing, a mock crypto-ransomware was developed. Mock crypto-ransomware is safe to use as it operates on a single host, directory and it does not destroy original file. While it is extermely oversimpliefied version of crypto-ransomware, it implements key features of crypto-ransomware destruction phase.


Navigate to directory mock_ransomware and execute below command:

```bash
python class_C_ransomware.py
```