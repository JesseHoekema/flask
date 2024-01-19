from flask import Flask, redirect
import requests

app = Flask(__name__)

def get_github_pages_urls(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    repos = response.json()
    github_pages_urls = [repo['html_url'] for repo in repos if repo['has_pages']]
    return github_pages_urls

@app.route('/<repo_name>')
def redirect_to_github_pages(repo_name):
    github_pages_urls = get_github_pages_urls('JesseHoekema')
    
    for url in github_pages_urls:
        if repo_name in url:
            return redirect(url)

    return f'Repo "{repo_name}" not found or does not have GitHub Pages enabled.'

if __name__ == '__main__':
    app.run(debug=True)
