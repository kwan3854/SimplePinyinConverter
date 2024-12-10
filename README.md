
# Simple Pinyin Converter

A simple desktop app for typing/converting Chinese Pinyin.

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

Non-Chinese characters can be included in the conversion output as-is.

#### Example Input:
```text
Hello, 你好!
```

#### Example Output:
```text
Hello, 你(nǐ)好(hǎo)!
```

### 3. **Tone Number Conversion**

Convert Pinyin with tone numbers into tone-marked Pinyin.

#### Example Input:
```text
hao3, shi4
```

#### Example Output:
```text
hǎo, shì
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

## Options Explained

1. **Start Symbol**: Adds a symbol before each Pinyin syllable.
   - Default: None.
   - Example:
      - Input: `你好`
      - Option: Start Symbol = `[`
      - Output: `你[nǐ]好[hǎo]`
2. **End Symbol**: Adds a symbol after each Pinyin syllable.
   - Default: None.
   - Example:
      - Input: `你好`
      - Option: End Symbol = `]`
      - Output: `你[nǐ]好[hǎo]`
3. **Include Non-Chinese Characters**: Toggle whether non-Chinese characters appear in the output.
   - Default: Enabled.
   - Example:
      - Input: `Hello, 你好!`
      - Output: `Hello, 你(nǐ)好(hǎo)!`

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

