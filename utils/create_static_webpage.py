import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
import base64
from dotenv import load_dotenv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dotenv_path = os.path.join(project_root, '.env')
problems_csv = os.path.join(project_root, 'problems.csv')
output_file = os.path.join(project_root, 'index.html')

load_dotenv(dotenv_path)

def create_static_webpage(problems_csv=problems_csv, output_file=output_file):
    # Read the problems CSV
    df = pd.read_csv(problems_csv)

    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ML Python Coding Questions</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
            h1 {{ color: #333; text-align: center; }}
            .nav-tags {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                margin-bottom: 30px;
            }}
            .nav-tag {{
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                border-radius: 20px;
                padding: 5px 15px;
                margin: 5px;
                text-decoration: none;
                color: #333;
                transition: background-color 0.3s;
            }}
            .nav-tag:hover {{
                background-color: #e0e0e0;
            }}
            .problem {{ 
                margin-bottom: 30px; 
                padding: 20px; 
                border-bottom: 2px solid #ddd;
            }}
            .problem:nth-of-type(odd) {{ background-color: #f9f9f9; }}
            .problem:nth-of-type(even) {{ background-color: #ffffff; }}
            .problem h2 {{ 
                color: #0066cc; 
                text-align: center;
                margin-bottom: 20px;
            }}
            .problem-content {{
                display: flex;
                justify-content: space-between;
            }}
            .question, .solution {{ 
                width: 48%; 
                padding: 0 15px;
            }}
            .vertical-divider {{
                width: 1px;
                background-color: #ddd;
                margin: 0 10px;
            }}
            pre {{ background-color: #f4f4f4; padding: 10px; overflow-x: auto; }}
            @media (max-width: 768px) {{
                .problem-content {{
                    flex-direction: column;
                }}
                .question, .solution {{ 
                    width: 100%; 
                    padding: 0;
                }}
                .solution {{ 
                    margin-top: 20px; 
                }}
                .vertical-divider {{
                    display: none;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>ML Python Coding Questions</h1>
        <div class="nav-tags">
            {nav_tags}
        </div>
        {problem_content}
    </body>
    </html>
    """

    nav_tags = ""
    problem_content = ""

    for index, row in df.iterrows():
        problem_name = row['problem_name']
        question_path = row['question_path']
        solution_path = row['solution_path']
        question_path = os.path.join(project_root, question_path)
        solution_path = os.path.join(project_root, solution_path)

        # Create navigation tag
        nav_tags += f'<a href="#problem-{index}" class="nav-tag">{problem_name}</a>\n'

        # Read question HTML
        with open(question_path, 'r', encoding='utf-8') as f:
            question_html = f.read()

        # Read solution code
        with open(solution_path, 'r', encoding='utf-8') as f:
            solution_code = f.read()

        # Create GitHub Gist for the solution
        gist_url = create_github_gist(problem_name, solution_code)

        # Format problem content
        problem_content += f"""
        <div id="problem-{index}" class="problem">
            <h2>{problem_name}</h2>
            <div class="problem-content">
                <div class="question">
                    <h3>Question:</h3>
                    {question_html}
                </div>
                <div class="vertical-divider"></div>
                <div class="solution">
                    <h3>Solution:</h3>
                    <script src="{gist_url}.js"></script>
                </div>
            </div>
        </div>
        """

    # Generate the final HTML
    final_html = html_template.format(nav_tags=nav_tags, problem_content=problem_content)

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Static webpage created: {output_file}")

def create_github_gist(filename, content):
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        raise ValueError("GitHub token not found. Set the GITHUB_TOKEN environment variable.")

    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    # Check if a gist with the given filename already exists
    existing_gist_url = check_existing_gist(filename, headers)
    if existing_gist_url:
        return existing_gist_url

    # If no existing gist found, create a new one
    data = {
        "description": f"Solution for {filename}",
        "public": True,
        "files": {
            f"{filename}.py": {
                "content": content
            }
        }
    }

    response = requests.post('https://api.github.com/gists', headers=headers, json=data)
    
    if response.status_code == 201:
        return response.json()['html_url']
    else:
        print(f"Failed to create Gist: {response.content}")
        return None

def check_existing_gist(filename, headers):
    # Get the list of user's gists
    response = requests.get('https://api.github.com/gists', headers=headers)
    
    if response.status_code == 200:
        gists = response.json()
        for gist in gists:
            for gist_file in gist['files']:
                if gist_file == f"{filename}.py":
                    return gist['html_url']
    else:
        print(f"Failed to fetch gists: {response.content}")
    
    return None

