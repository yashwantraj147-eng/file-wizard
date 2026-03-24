<div align="center">
  
# 🧙‍♂️ File Wizard

**The ultimate command-line tool for seamless data format conversions.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Build Status](https://github.com/yashwantraj147-eng/file-wizard/actions/workflows/ci.yml/badge.svg)](https://github.com/yashwantraj147-eng/file-wizard/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Convert safely between **CSV, JSON, YAML, XML, TOML**, and **Markdown** with just a single command.

[Features](#-features) • [Installation](#%EF%B8%8F-installation) • [Usage](#-usage) • [Supported Formats](#-supported-formats) 

</div>

---

## ✨ Features

- 🪄 **Auto-Magic Format Detection**: Automatically infers input and output formats from file extensions.
- 💅 **Pretty Printing**: Perfectly formatted output with the `--pretty` flag.
- 🧪 **Dry Run Mode**: Preview your conversions safely without writing any data using `--dry-run`.
- 🔍 **Verbose Logging**: Get a step-by-step breakdown of the parsing process with `--verbose`.
- 🔁 **Pipeline Ready**: Native stdin/stdout (`-`) support for seamless bash piping.
- 🚀 **Lightning Fast**: Built on top of `click` and robust parsing libraries.

## 📦 Supported Formats

| Format   | Read Support | Write Support |
| :------- | :----------: | :-----------: |
| **CSV**  |      ✅      |       ✅      |
| **JSON** |      ✅      |       ✅      |
| **YAML** |      ✅      |       ✅      |
| **XML**  |      ✅      |       ✅      |
| **TOML** |      ✅      |       ✅      |
| **MD**   |      ❌      |       ✅ *(Tables)*   |

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yashwantraj147-eng/file-wizard.git
   cd file-wizard
   ```

2. **Install the CLI package:**
   ```bash
   pip install -e .
   ```

*(For development and testing, install with dev dependencies: `pip install -e .[dev]`)*

## 🚀 Usage

### Basic Conversion
The wizard will automatically detect the formats based on your file extensions:
```bash
wizard convert data.csv data.json
```

### Beautiful Output
Make your JSON, YAML, or XML cleanly formatted and human-readable:
```bash
wizard convert config.yaml config.json --pretty
```

### Safe Preview (Dry Run)
Check the resulting Markdown table without actually modifying or creating external files:
```bash
wizard convert examples/employees.csv examples/employees.md --dry-run
```

### Advanced Piping
Use standard input and standard output for complex script workflows!
```bash
cat data.csv | wizard convert - - --in-format csv --out-format json > data.json
```

---

<div align="center">
  <i>Built with Python & Click</i>
</div>
