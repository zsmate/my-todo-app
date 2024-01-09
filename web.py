import streamlit as st
import functions

todos = functions.read_todos()
def add_todo():
    todo = st.session_state['new_todo'] +'\n'
    todos.append(todo)
    functions.write_todos(todos)

def remove_todo():
    for skey in st.session_state.keys():
        if skey != 'new_todo' and st.session_state[skey] == True:
            todos.pop(int(skey))
    functions.write_todos(todos)

st.title('My To-do App')
st.subheader('This is my todo app.')
st.write('This app is to increase productivity!!!!')

for k,todo in enumerate(todos):
    st.checkbox(key=str(k), label=todo, on_change=remove_todo)


st.text_input(label='', on_change=add_todo, key='new_todo',
              placeholder="Enter a new todo...")

st.session_state