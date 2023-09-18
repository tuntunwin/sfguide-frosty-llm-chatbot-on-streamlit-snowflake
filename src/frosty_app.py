import openai
import re
import streamlit as st
from prompts import get_system_prompt
from sql_connection import query
st.title("☃️ Frosty")

# Initialize the chat messages history
openai.api_type = "azure"
openai.api_base = "https://nete2oai-test.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "28d253a056eb488da62a9dfb9039352a"
#openai.api_key = st.secrets.OPENAI_API_KEY
if "messages" not in st.session_state:
    # system prompt includes table information, rules, and prompts the LLM to produce
    # a welcome message to the user.
    sys_prompt = get_system_prompt()
    print("system prompt: ", sys_prompt)
    st.session_state.messages = [{"role": "system", "content": sys_prompt}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

# display the existing chat messages
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "results" in message:
            st.dataframe(message["results"])
            

# If last message is not from assistant, we need to generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response = ""
        resp_container = st.empty()
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        #print("prompt ", messages)
        response = openai.ChatCompletion.create(
            engine="mychat",
            messages=messages,
           
             temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)
        print("OpenAPI response ", response)
        response = response.choices[0].message.content
        resp_container.markdown(response)
        message = {"role": "assistant", "content": response}
        # Parse the response for a SQL query and execute if available
        sql_match = re.search(r"```sql\n(.*)\n```", response, re.DOTALL)
        if sql_match:
            sql = sql_match.group(1)
            ##conn = st.experimental_connection("snowpark")
            message["results"] = query(sql)
            #message["results"] = sql
            st.text_input("sql", value=sql)
            st.dataframe(message["results"])
            #st.bar_chart(message["results"], x="Town", y="NumOfIncidents")
            st.map(message["results"], latitude="Location_lat", longitude="Location_lon")
        st.session_state.messages.append(message)
