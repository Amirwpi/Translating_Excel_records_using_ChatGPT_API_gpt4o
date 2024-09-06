import openai
import time
import pandas as pd
from tqdm import tqdm

#update your API HERE
openai.api_key = "YOUR_OPENAI_API"
#update your current directory as xlsx file
file_path = r'Z:\example.xlsx'

def translate_text(text, retries=3, wait=5):
    attempt = 0
    while attempt < retries:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": f"Translate the following text to English professionally:\n\n{text}"}
                ],
                max_tokens=2000,
                temperature=0.2
            )
            
            translated_text = response['choices'][0]['message']['content'].strip()
            return translated_text
        except Exception as e:
            if "502" in str(e):
                time.sleep(wait)
                attempt += 1
            else:
                return text
    return text

def process_excel_file(input_file_path):
    df = pd.read_excel(input_file_path)
    
    if 'message_Original_cleared' not in df.columns:
        print("Column 'message_Original_cleared' not found in the Excel file.")
        return
    
    tqdm.pandas(desc="Translating")
    df['translated_for_balancing'] = df['message_Original_cleared'].progress_apply(translate_text)
    
    output_file_path = input_file_path.replace('.xlsx', '_translated.xlsx')
    df.to_excel(output_file_path, index=False, encoding='utf-8-sig')
    print(f"Translated file saved to {output_file_path}")

if __name__ == "__main__":
    excel_file_path = file_path 
    
    process_excel_file(excel_file_path)
