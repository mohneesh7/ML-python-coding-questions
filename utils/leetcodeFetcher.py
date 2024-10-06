import os
import requests
from bs4 import BeautifulSoup as bs



def get_question_html(slug_name):
    print("debug_slug_name", slug_name)
    # Code snippet shamelessly stolen from https://stackoverflow.com/a/56610178
    data = {"operationName":"questionData","variables":{"titleSlug":slug_name},
            "query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}

    r = requests.post('https://leetcode.com/graphql', json = data).json()
    soup = bs(r['data']['question']['content'], 'lxml')
    return soup

# code to get a URL and exteract the last path component
def get_last_path_component(url):
    # Check if the domain is leetcode.com
    print("debug_URL", url)
    if 'leetcode.com' not in url:
        raise ValueError('URL does not point to LeetCode')
    # Split the URL by '/' and return the last element
    return url.split('/')[-1] if url.split('/')[-1] != '' else url.split('/')[-2]

def get_question_content_as_html(url,folder_path):
    slug_name = get_last_path_component(url)
    markup = get_question_html(slug_name)
    # save markup to a file
    with open(os.path.join(folder_path, 'question.html'), 'w', encoding='utf-8') as f:
        f.write(str(markup))
