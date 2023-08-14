# YT-Script-Generator

Deployed application:

https://yt-script-generator.streamlit.app/

To run this application, follow the following steps:

1. Install the GPT4All Installer using GUI based installers
   
    Windows: https://gpt4all.io/installers/gpt4all-installer-win64.exe

    Mac: https://gpt4all.io/installers/gpt4all-installer-darwin.dmg

    Ubuntu: https://gpt4all.io/installers/gpt4all-installer-linux.run

2. Using above, download the Falcon LLM model, and note the download path.

3. Install the required dependencies:
   
    pip install -r requirements.txt

4. Update the path of the model in line 10 of llm.py

   It should look like this:

   "{path}/nomic.ai/GPT4All/ggml-model-gpt4all-falcon-q4_0.bin"

6. Start the python application using
   
    streamlit run llm.py
