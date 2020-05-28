import requests
import json
import wget


base_url = 'https://api.github.com'
base_url_for_download = 'https://raw.githubusercontent.com/'
base_url_for_db_addition = 'https://intelli-script.herokuapp.com/'

exclude_list = [
    '.gitignore', 'LICENSE.txt', 'README.md', '.github', 'tests', '.travis.yml', 
    'LICENSE', 'backup', 'git-scripts', 'screen-capturing', 'searching-files',
    '.tmp'
    ]


headers = {
    'Accept': 'application/vnd.github.v3+json'
}

def getting_popular_scripts_in_folder(user, repoName, path):
    url = base_url + '/repos/{}/{}/contents/{}'.format(user,repoName, path)
    response = requests.get(url)
    data = json.loads(response.text)
    required_data = {}
    for i in data:
        required_data[i['name']] = i['download_url']
    print(required_data)
    return required_data


def getting_popular_scripts_in_folder_2(user, repoName, path=''):
    if path:
        url = base_url + '/repos/{}/{}/contents/{}'.format(user,repoName, path)
    else:
        url = base_url + '/repos/{}/{}/contents'.format(user,repoName)
    response = requests.get(url)
    data = json.loads(response.text)
    required_data = {}
    for i in data:
        if i['name'] in exclude_list:
            pass
        else:
            required_data[i['name']] = i['download_url']
    print(required_data)
    return required_data

def getting_popular_scripts_from_file():
    pass

def downloading_files(url):
    #url = base_url_for_download + '/{}/{}/{}/{}'.format(user,repoName, branch, path)
    wget.download(url)

def adding_scripts_to_db(data):
    url = base_url_for_db_addition + 'script/'
    for i in data:
        payload = {
            'name': i,
            'url': data[i]
        }
        response = requests.post(url, data=payload)
        if response.status_code == 400:
            print(response.text)
            print(response.status_code)
        else:
            print(response.status_code)
    



# data = getting_popular_scripts_in_folder('ruanyf', 'simple-bash-scripts', 'scripts')
# data1 = getting_popular_scripts_in_folder_2('miguelgfierro','scripts')
# data2 = getting_popular_scripts_in_folder_2('epety','100-shell-script-examples')
# data3 = getting_popular_scripts_in_folder_2('aviaryan','utility-bash-scripts')
# data4 = getting_popular_scripts_in_folder_2('ryanoasis','public-bash-scripts')
# adding_scripts_to_db(data)
# adding_scripts_to_db(data1)
# adding_scripts_to_db(data2)
# adding_scripts_to_db(data3)
# adding_scripts_to_db(data4)
#downloading_files('ruanyf', 'simple-bash-scripts', 'scripts/addition.sh')

