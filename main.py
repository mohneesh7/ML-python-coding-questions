import os
import pandas as pd
import utils.leetcodeFetcher as lcf
import utils.create_static_webpage as csw
import utils.createDirsFiles as cdf


def create_html_file(question_path, folder_path):
    """
        if question_path file contain a URL then fetch the content using the 
        get_question_content_as_html function then delete the question.txt file
    """
    with open(question_path, 'r') as f:
        question_content = f.read()
        if 'https://leetcode.com/' in question_content:
            lcf.get_question_content_as_html(question_content,folder_path)
    question_path = os.path.join(folder_path, 'question.html')
    return question_path

def parse_problem_repo(repo_path='ProblemRepo'):
    def markdown_to_html(markdown_content):
        # TODO: Implement markdown to HTML conversion
        # This function will be filled later with an API
        return ""

    problems = []

    for problem_folder in os.listdir(repo_path):
        folder_path = os.path.join(repo_path, problem_folder)
        
        if os.path.isdir(folder_path):
            question_html_path = os.path.join(folder_path, 'question.html')
            if not os.path.exists(question_html_path):
                question_path = os.path.join(folder_path, 'question.txt')
                question_path = create_html_file(question_path, folder_path)
            else:
                question_path = question_html_path
            solution_path = os.path.join(folder_path, 'solution.py')
            
            if os.path.exists(question_path) and os.path.exists(solution_path):
                # the paths should be forward slashes
                question_path = question_path.replace('\\', '/')
                solution_path = solution_path.replace('\\', '/')
                problems.append({
                    'problem_name': problem_folder,
                    'question_path': question_path,
                    'solution_path': solution_path
                })
            
    df = pd.DataFrame(problems)
    return df

# Add this function before parse_problem_repo
def create_problem_directories():
    cdf.create_problem_directories()

# Modify the main execution part
if __name__ == "__main__":
    create_problem_directories()
    result_df = parse_problem_repo()
    print(result_df)
    result_df.to_csv('problems.csv', index=False)
    csw.create_static_webpage(problems_csv='problems.csv')

