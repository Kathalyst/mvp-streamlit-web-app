import streamlit as st
import requests
import json

def get_repo_info(url):
    if "github.com" not in url:
        return None
    username = url.split('/')[1]
    repo_name = url.split('/')[2]
    access_token = 'your-access-token'
    headers = {'Authorization': f'token {access_token}'}
    api_url = f'https://api.github.com/repos/{username}/{repo_name}'
    response = requests.get(api_url, headers=headers)
    return response.json()

def app():
    st.title('GitHub Repo Information')
    repo_url = st.text_input('Enter the GitHub repo URL', '')
    if st.button('Submit'):
        repo_info = get_repo_info(repo_url)
        if repo_info:
            st.write(f'Repo Name: {repo_info["name"]}')
            st.write(f'Description: {repo_info["description"]}')
            st.write(f'Stars: {repo_info["stargazers_count"]}')
            st.write(f'Forks: {repo_info["forks_count"]}')
            st.write(f'Created at: {repo_info["created_at"]}')
            st.write(f'Updated at: {repo_info["updated_at"]}')
        else:
            st.error('Invalid GitHub URL')

if __name__ == '__main__':
    app()