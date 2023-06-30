import requests
from bs4 import BeautifulSoup
import time

# DOM Element IDs
AGENT_ID = "agent_id"
AGENT_STATUS = "agent_status"

# Data Schemas
AGENT_SCHEMA = {
    "id": "",
    "status": ""
}

# Message Names
UPDATE_MESSAGE = "Agent {} status: {}"

def web_scraping_function(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    agent_info = soup.find(id=AGENT_ID)
    agent_status = soup.find(id=AGENT_STATUS)

    AGENT_SCHEMA["id"] = agent_info.text
    AGENT_SCHEMA["status"] = agent_status.text

    return AGENT_SCHEMA

def update_function(agent_info):
    with open("readme.txt", "a") as file:
        file.write(UPDATE_MESSAGE.format(agent_info["id"], agent_info["status"]) + "\n")

def main():
    while True:
        agent_info = web_scraping_function("http://example.com")
        update_function(agent_info)
        time.sleep(3600)  # update every hour

if __name__ == "__main__":
    main()