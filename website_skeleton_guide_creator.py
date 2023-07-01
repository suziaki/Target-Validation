```python
import os
import json

repository_path = "./path_to_your_repository"
review_results = {}

def review_repository():
    global review_results
    with open('repository_reviewer.py', 'r') as file:
        exec(file.read())
    review_results = review_repository(repository_path)

DOM_element_ids = []
message_names = []
function_names = []

def extract_info_from_review():
    global DOM_element_ids, message_names, function_names
    DOM_element_ids = review_results.get('DOM_element_ids', [])
    message_names = review_results.get('message_names', [])
    function_names = review_results.get('function_names', [])

guide_content = ""

def create_guide():
    global guide_content
    guide_content += "# Website Skeleton Guide\n\n"
    guide_content += "## DOM Elements\n\n"
    for id in DOM_element_ids:
        guide_content += f"- {id}\n"
    guide_content += "\n## Messages\n\n"
    for message in message_names:
        guide_content += f"- {message}\n"
    guide_content += "\n## Functions\n\n"
    for function in function_names:
        guide_content += f"- {function}\n"

def write_guide_to_file():
    with open('website_skeleton_guide.md', 'w') as file:
        file.write(guide_content)

def main():
    review_repository()
    extract_info_from_review()
    create_guide()
    write_guide_to_file()

if __name__ == "__main__":
    main()
```