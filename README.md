# Simple Pinyin Converter

A simple desktop app for typing/converting Chinese Pinyin.

![Pinyin Converter](Documentation/simple_pinyin_converter.png)

---

## Download

Download the pre-built application for your platform from the **Releases** section:

- **Windows (.exe)**: [Download here](https://github.com/kwan3854/SimplePinyinConverter/releases)
- **macOS (.app)**: [Download here](https://github.com/kwan3854/SimplePinyinConverter/releases)

No installation required—just download and run!

---

## Features and Usage

### 1. **Convert Chinese Characters to Pinyin**

#### Example Input:

```text
你好，世界！
```

#### Options:

- **Start Symbol**: Specify a character or string to prefix each Pinyin syllable.
    - Example: `(`
- **End Symbol**: Specify a character or string to suffix each Pinyin syllable.
    - Example: `)`

#### Example Output:

```text
你(nǐ)好(hǎo)，世(shì)界(jiè)！
```

### 2. **Handle Non-Chinese Characters**

#### Default Behavior:

Non-Chinese characters can be included in the conversion output as-is.

#### Example Input:

```text
Hello, 你好!
```

#### Example Output:

```text
Hello, 你(nǐ)好(hǎo)!
```

#### Options:

| Pinyin Only Display | Ignore Non-Chinese Characters | Output              |
|---------------------|-------------------------------|---------------------|
| ✅                   | ✅                             | nǐ hǎo              |
| ✅                   | ❌                             | Hello, nǐ hǎo !     |
| ❌                   | ✅                             | 你(nǐ)好(hǎo)         |
| ❌                   | ❌                             | Hello, 你(nǐ)好(hǎo)! |

### 3. **Tone Number Conversion**

Convert Pinyin with tone numbers into tone-marked Pinyin.

#### Example Input:

```text
a1a2a3a4
e1e2e3e4
i1i2i3i4
o1o2o3o4
u1u2u3u4
v1v2v3v4

ha3o
shi4
```

#### Example Output:

```text
āáǎà
ēéěè
īíǐì
ōóǒò
ūúǔù
ǖǘǚǜ

hǎo
shì
```

### 4. **Special Handling for 'ü'**

The app automatically maps `v` to `ü` for convenience.

#### Example Input:

```text
nv3, lv4
```

#### Example Output:

```text
nǚ, lǜ
```

---

## Running the Application from Source (Advanced Users)

### 1. Clone the Repository

```bash
git clone https://github.com/kwan3854/SimplePinyinConverter.git
cd SimplePinyinConverter
```

### 2. Install Dependencies

Install all necessary Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python pinyin_converter.py
```

---

## Building from Source

To build the application yourself using `PyInstaller`, follow these steps:

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Build Executable

#### **Windows**

```bash
pyinstaller --onefile --windowed pinyin_converter.py
```

#### **macOS**

1. Include `pypinyin` resources in the build:
   ```bash
   pyinstaller --onefile --windowed --add-data="/path/to/pypinyin:pypinyin" pinyin_converter.py
   ```

   Replace `/path/to/pypinyin` with the path to `pypinyin` in your environment.

2. Ensure the `.app` file has execution permissions:
   ```bash
   chmod +x dist/pinyin_converter.app/Contents/MacOS/*
   ```

---

## Troubleshooting for macOS Users

1. **App Doesn't Open**:
    - Control-click the `.app` file, select "Open," and confirm to bypass macOS Gatekeeper.

2. **Missing Resource Errors**:
    - Ensure you used the `--add-data` option during the PyInstaller build process.

3. **Permissions Issue**:
    - Run the following command to add execution permissions:
      ```bash
      chmod +x dist/pinyin_converter.app/Contents/MacOS/*
      ```

---

## Contributing

We welcome contributions to this project. If you have ideas for new features or improvements, feel free to open an issue
or submit a pull request.

### Requesting New Features

If you want to request a new feature or report a bug, please visit
the [Issues](https://github.com/kwan3854/SimplePinyinConverter/issues) page of the repository and create a new issue.
Make sure to provide a detailed description of your request or problem to help us address it effectively.

------

## License

This project is licensed under the MIT License. See the LICENSE file for details.
