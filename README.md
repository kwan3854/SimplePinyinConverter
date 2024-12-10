# Simple Pinyin Converter

A simple desktop app for typing/converting Chinese Pinyin.

---

## Download

Download the pre-built application for your platform from the **Releases** section:

- **Windows (.exe)**: [Download here](https://github.com/kwan3854/SimplePinyinConverter/releases)
- **macOS**: [Download here](https://github.com/kwan3854/SimplePinyinConverter/releases)

No installation required—just download and run!

---

## Features

- Convert Chinese text to Pinyin with or without tone marks.
- Customize Pinyin format (add start/end symbols).
- Handle non-Chinese characters with optional settings.
- Convert Pinyin input with tone numbers (e.g., `a1`, `e2`) into tone-marked Pinyin (e.g., `ā`, `é`).
- Dark theme for better readability.

---

## Running the Application from Source

If you want to run the app from source code, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SimplePinyinConverter.git
cd SimplePinyinConverter
```

### 2. Install Dependencies

Install all dependencies at once:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install pypinyin==0.52.0
pip install PyQt5==5.15.11
pip install PyQt5-Qt5==5.15.14
pip install PyQt5-stubs==5.15.6.0
pip install PyQt5_sip==12.15.0
```

### 3. Run the Application

```bash
python pinyin_converter.py
```

### Building the Executable (Optional)

If you’d like to build the executable yourself using pyinstaller:

1. Install pyinstaller:
    ```bash
    pip install pyinstaller
    ```
2. Build the application:
    ```bash
    pyinstaller --onefile --windowed pinyin_converter.py
    ```
3. The executable will be in the `dist/` folder.

---

## Example

### Input:

Chinese Text:

```
你好，世界！
```

### Options:

- Start Symbol: `(`
- End Symbol: `)`

### Output:

```
你(nǐ)好(hǎo)，世(shì)界(jiè)！
```

Enjoy converting Chinese characters to Pinyin effortlessly! 😊
