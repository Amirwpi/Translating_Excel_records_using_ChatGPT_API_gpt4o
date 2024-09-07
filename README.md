# Excel Translation Script

This Python script translates text in the "message_Original_cleared" column of an Excel file to English using OpenAI's GPT-4 model and saves the results in a new column named "translated_for_balancing".

## Requirements

- Python 3.x
- [OpenAI API key](https://platform.openai.com/)
- Required Python packages: `pandas`, `tqdm`, `openai`, `openpyxl`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Amirwpi/Translating_Excel_records_using_ChatGPT_API_gpt4o.git
    cd Translating_Excel_records_using_ChatGPT_API_gpt4o
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set your OpenAI API key in the script file (`translate_excel.py`):
    ```python
    openai.api_key = "your_api_key_here"  # Replace with your OpenAI API key
    ```

## Usage

1. Place your Excel file in the repository directory or provide the correct path to it in `translate_excel.py`.
2. Run the script:
    ```sh
    python translate_excel.py
    ```

The script will process the Excel file, translate the specified column, and save the results in a new file with "_translated" appended to the original file name.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
