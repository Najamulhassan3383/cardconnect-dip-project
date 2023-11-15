import re
import json

class TextExtractor:
    def __init__(self):
        pass

    def extract_info_from_list(self, entity_list):
        
        # print(entity_list)
        # Define regular expressions for extracting information
        phone_pattern = re.compile(r'(\+\d{1,4}|\(\d{1,4}\)|\d{1,4})?[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})', re.IGNORECASE)
        email_pattern = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', re.IGNORECASE)

        # Extract information using regular expressions
        
        
        
        phone_match = phone_pattern.search(entity_list)
        email_match = email_pattern.search(entity_list)

        entity_info = {
            
            'Phone': phone_match.group(0) if phone_match else None,
            'Email': email_match.group(0) if email_match else None,
        }

           

        return json.dumps(entity_info, indent=4)
    
def main():
    text_extractor = TextExtractor()
    entity_list = """Najam ul Hassan
                    najamul@gmail.com
                    0923445677"""

    extracted_data = text_extractor.extract_info_from_list(entity_list)
    print(extracted_data)

if __name__ == "__main__":
    main()

