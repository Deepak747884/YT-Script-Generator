# YT-Script-Generator

To run this application, follow the following steps:

1. Install the GPT4All Installer using GUI based installers
    Windows: https://gpt4all.io/installers/gpt4all-installer-win64.exe
    Mac: https://gpt4all.io/installers/gpt4all-installer-darwin.dmg
    Ubuntu: https://gpt4all.io/installers/gpt4all-installer-linux.run

2. Download the Falcon LLM model, and note the download path.

3. Install the required dependencies:
    pip install -r requirements.txt

4. Update the path of the model in line 11 of llm.py

5. Start the python application using
    streamlit run llm.py