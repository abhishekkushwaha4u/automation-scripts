import click
import requests
import json
import wget

@click.command()
@click.option('--mode', default=1, help='Specify mode 1 to show scripts by --number or 2 for scripts by name, 1 by default')
@click.option('--number', default=0, help='Specify no of scripts you want to see, all will be shown by default')
@click.option('--name', default=None ,prompt='Full or partial name of the script you want to view or download',
              help='Here you enter the full or partial name of the script you want to download or view')

def main_operation(mode, name, number):
    if mode == 1:
        output = requests.get('https://intelli-script.herokuapp.com/search/script/byNumber/?offset=1&limit={}'.format(number))
        new_output = json.loads(output.text)
        for i in range(len(new_output)):
            click.echo('{}) {}'.format(i+1, new_output[i]['name']))
    elif mode == 2:
        if name:
            output = requests.get('https://intelli-script.herokuapp.com/search/script/byName/?name={}'.format(name))
        else:
            output = requests.get('https://intelli-script.herokuapp.com/search/script/byName/')
        new_output = json.loads(output.text)
        for i in range(len(new_output)):
            click.echo('{}) {}'.format(i+1, new_output[i]['name']))
        
        click.echo('\n')
        click.echo('Input the names of the scripts you want to select, you can enter multiple names separated by commas.')
        choice = input('Enter choices: ').split(',')
        click.echo('Select 1 if you just want to see the scripts or 2 if you want to download it/them.')
        new_choice = int(input('Enter choice now: '))
        if new_choice == 1:
            for i in choice:
                for j in new_output:
                    if j['name'] == i:
                        click.echo("========{}=======".format(i))
                        click.echo((requests.get(j['url']).text))
                        click.echo("======== end =======")

        elif new_choice == 2:
            for i in choice:
                for j in new_output:
                    if j['name'] == i:
                        click.echo("========Downloading {}=======".format(i))
                        file = wget.download(j['url'])
                        click.echo("\n")
                         
    



if __name__ == '__main__':
    main_operation()