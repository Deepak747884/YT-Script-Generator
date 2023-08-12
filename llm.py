import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All

PATH = 'C:/Users/Deepak Dhingra/AppData/Local/nomic.ai/GPT4All/ggml-model-gpt4all-falcon-q4_0.bin'

# App framework
st.title('YT Script Generator')
prompt = st.text_input('Enter the topic of the YT video') 

llm = GPT4All(model=PATH, verbose=True)

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a youtube video script based on the title: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title) 
    st.write(script) 

    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Script History'): 
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)
