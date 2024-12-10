import sys
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, QCheckBox, QLabel, \
    QHBoxLayout, QVBoxLayout, QFrame, QDockWidget, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt, QTimer
from pypinyin import pinyin, Style

# Map of tone numbers to the appropriate Pinyin vowel with tone marks
tone_map = {
    'a': ['a', 'ā', 'á', 'ǎ', 'à'],
    'e': ['e', 'ē', 'é', 'ě', 'è'],
    'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
    'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
    'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
    'v': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']  # 'v'를 'ü'로 매핑
}


class PinyinConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window settings
        self.setWindowTitle('Chinese to Pinyin Converter')
        self.setGeometry(300, 300, 1200, 600)

        # Set up timers for throttled conversion
        self.input_timer = QTimer(self)
        self.input_timer.setSingleShot(True)
        self.input_timer.setInterval(1000)

        self.pinyin_input_timer = QTimer(self)
        self.pinyin_input_timer.setSingleShot(True)
        self.pinyin_input_timer.setInterval(1000)

        # Connect timers to conversion methods
        self.input_timer.timeout.connect(self.convert_to_pinyin)
        self.pinyin_input_timer.timeout.connect(self.convert_pinyin_input)

        # Dockable widget for the Pinyin Converter (left section)
        converter_dock = QDockWidget("Pinyin Converter", self)
        converter_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        converter_widget = QWidget(self)
        converter_layout = QVBoxLayout(converter_widget)

        # Options at the top
        options_layout = QHBoxLayout()

        self.pinyin_only_checkbox = QCheckBox("Pinyin Only Display", self)
        self.pinyin_only_checkbox.stateChanged.connect(self.on_option_changed)
        options_layout.addWidget(self.pinyin_only_checkbox)

        self.ignore_non_chinese_checkbox = QCheckBox("Ignore Non-Chinese Characters", self)
        self.ignore_non_chinese_checkbox.stateChanged.connect(self.on_option_changed)
        options_layout.addWidget(self.ignore_non_chinese_checkbox)

        self.start_symbol_label = QLabel("Start Symbol:", self)
        self.start_symbol_input = QLineEdit(self)
        self.start_symbol_input.setPlaceholderText("(")
        self.start_symbol_input.setText("(")
        self.start_symbol_input.setMaximumWidth(50)
        self.start_symbol_input.textChanged.connect(self.on_option_changed)

        self.end_symbol_label = QLabel("End Symbol:", self)
        self.end_symbol_input = QLineEdit(self)
        self.end_symbol_input.setPlaceholderText(")")
        self.end_symbol_input.setText(")")
        self.end_symbol_input.setMaximumWidth(50)
        self.end_symbol_input.textChanged.connect(self.on_option_changed)

        options_layout.addWidget(self.start_symbol_label)
        options_layout.addWidget(self.start_symbol_input)
        options_layout.addWidget(self.end_symbol_label)
        options_layout.addWidget(self.end_symbol_input)

        converter_layout.addLayout(options_layout)

        # Input field for Chinese characters (QTextEdit for multi-line input)
        self.input_field = QTextEdit(self)
        self.input_field.setPlaceholderText("Enter Chinese characters here")
        self.input_field.setMinimumHeight(150)
        self.input_field.textChanged.connect(self.on_input_field_text_changed)
        converter_layout.addWidget(self.input_field)

        # Non-editable, selectable text output (QTextBrowser allows selection, but no editing)
        self.output_browser = QTextBrowser(self)
        self.output_browser.setText("Pinyin will appear here")
        self.output_browser.setMinimumHeight(150)
        converter_layout.addWidget(self.output_browser)

        converter_dock.setWidget(converter_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, converter_dock)

        # Dockable widget for the Pinyin Input (right section)
        input_dock = QDockWidget("Pinyin Input", self)
        input_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        input_widget = QWidget(self)
        input_layout = QVBoxLayout(input_widget)

        # Pinyin input field for typing with tones
        self.pinyin_input_field = QTextEdit(self)
        self.pinyin_input_field.setPlaceholderText("Enter Pinyin with tone numbers (e.g., a1, e2)")
        self.pinyin_input_field.setMinimumHeight(150)
        self.pinyin_input_field.textChanged.connect(self.on_pinyin_input_field_text_changed)
        input_layout.addWidget(self.pinyin_input_field)

        # Non-editable, selectable text output for the Pinyin conversion result
        self.pinyin_output_browser = QTextBrowser(self)
        self.pinyin_output_browser.setText("Pinyin conversion result will appear here")
        self.pinyin_output_browser.setMinimumHeight(150)
        input_layout.addWidget(self.pinyin_output_browser)

        input_dock.setWidget(input_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, input_dock)

        # Initially hide start and end symbol inputs
        self.toggle_ignore_non_chinese_checkbox(self.pinyin_only_checkbox.isChecked())

    def on_input_field_text_changed(self):
        self.input_timer.start()

    def on_pinyin_input_field_text_changed(self):
        self.pinyin_input_timer.start()

    def on_option_changed(self):
        self.convert_to_pinyin()

    def toggle_ignore_non_chinese_checkbox(self, state):
        self.ignore_non_chinese_checkbox.setVisible(not state)
        self.start_symbol_label.setVisible(not state)
        self.start_symbol_input.setVisible(not state)
        self.end_symbol_label.setVisible(not state)
        self.end_symbol_input.setVisible(not state)
        self.convert_to_pinyin()  # 옵션 변경 시 즉시 변환 수행

    def convert_to_pinyin(self):
        chinese_text = self.input_field.toPlainText()
        if not chinese_text:  # 입력 텍스트가 없으면 변환하지 않음
            return

        ignore_non_chinese = self.ignore_non_chinese_checkbox.isChecked()

        pinyin_result = pinyin(chinese_text, style=Style.TONE,
                               errors='ignore' if ignore_non_chinese or self.pinyin_only_checkbox.isChecked() else 'default')

        start_symbol = self.start_symbol_input.text().strip()
        end_symbol = self.end_symbol_input.text().strip()

        if self.pinyin_only_checkbox.isChecked():
            pinyin_string = ' '.join([item[0] for item in pinyin_result if item])
        else:
            pinyin_string = ''
            for ch, pin in zip(chinese_text, pinyin_result):
                if pin:  # This means it's a Chinese character
                    pinyin_string += f'{ch}{start_symbol}{pin[0]}{end_symbol}'
                else:  # Non-Chinese characters
                    pinyin_string += ch

        self.output_browser.setText(pinyin_string)

    def convert_tones(self, text):
        output = []
        i = 0
        while i < len(text):
            char = text[i].lower()
            if char in tone_map and i + 1 < len(text) and text[i + 1] in '01234':
                tone_number = int(text[i + 1])
                output.append(tone_map[char][tone_number])
                i += 2
            else:
                output.append(text[i])
                i += 1
        return ''.join(output)

    def convert_pinyin_input(self):
        pinyin_input_text = self.pinyin_input_field.toPlainText()
        converted_pinyin = self.convert_tones(pinyin_input_text)
        self.pinyin_output_browser.setText(converted_pinyin)


# Main loop
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Apply Fusion theme
    app.setStyle("Fusion")

    # Apply dark theme
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))

    app.setPalette(dark_palette)

    converter = PinyinConverter()
    converter.show()
    sys.exit(app.exec_())
