# Character-n-Token-Calculator

Some Documentation:
https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them

## Overview

Characters n' Token Calculator is a simple and lightweight desktop application built in Python. The application serves as a utility tool to monitor various text metrics in real-time like Token Count, Keystroke count, and other metrics like:

- **Token Count**: Number of tokens in the clipboard.
- **Character Count**: Number of characters in the clipboard.
- **Words in Clipboard**: Number of words in the clipboard.
  
Additionally, the application offers:

- **Typed Words**: Keeps track of the number of words you have typed.
- **Keystrokes**: Keeps track of the number of keystrokes you have made.

The application also provides a text field with metrics for:

- **Field Token Count**: Tokens in the field.
- **Field Character Count**: Characters in the field.
- **Field Words**: Words in the field.

Users can also export these metrics to a CSV file for later analysis. Metrics can be reset with a single click.

## Prerequisites

- Python 3.x
- Tkinter
- pyperclip
- pynput

## Installation

1. Clone this repository.

\`\`\`bash
git clone https://github.com/AcidAlchamy/Character-n-Token-Calculator.git
\`\`\`

2. Navigate to the project folder.

\`\`\`bash
cd Character-n-Token-Calculator
\`\`\`

3. Install the required packages.

\`\`\`bash
pip install pyperclip pynput
\`\`\`

## How to Use

1. Run the `main.py` script to launch the application.

\`\`\`bash
python main.py
\`\`\`

2. After launching the application, you will see a dashboard that updates in real-time.
   - Clipboard metrics will update every second.
   - Typed Words and Keystrokes metrics will update as you type.

3. You can write text into the text field to get the text metrics for that field.

4. Use the **Export History to CSV** button to save the metrics history to a CSV file.

5. Use the **Reset Metrics** button to reset all the metrics to zero.

## Contributing

Feel free to submit pull requests, create issues, or provide feedback.
