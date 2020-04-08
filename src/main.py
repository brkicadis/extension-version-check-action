from lastversion import lastversion
from collections import namedtuple
import os
import json
import subprocess
import sys
import git
import re


def json_file(json_file_name):
    with open(os.path.abspath(json_file_name)) as file_name:
        return json.load(file_name)


def json_decoder(extensions_parameters):
    return namedtuple('X', extensions_parameters.keys())(*extensions_parameters.values())


def json_content():
    json_string = json.dumps(json_file('.github/shop-extensions.json'), indent=4)
    return json.loads(json_string, object_hook=json_decoder)


def last_released_version():
    repository_to_clone = "brkicadis/" + sys.argv[2]
    print(lastversion.latest(repository_to_clone, output_format='version', pre_ok=True))
    return lastversion.latest(repository_to_clone, output_format='version', pre_ok=True)


def current_release_version():
    repo = git.Repo(search_parent_directories=True)
    branch = repo.active_branch
    print(re.sub('[^\d\.]', '', branch.name))
    return re.sub('[^\d\.]', '', branch.name)


def version_differences(file_name, content, version):
    #file_name = open('/Users/adis.brkic/IdeaProjects/woocommerce-ee/wirecard-woocommerce-extension/woocommerce-wirecard-payment-gateway.php', 'r')
    file_name = open(os.path.abspath(subprocess.check_output("find ../" + sys.argv[2] + " -name " + file_name, shell=True, text=True)).rstrip(), 'r')
    for file_line in file_name.readlines():
        if version in file_line and str(last_released_version()) in file_line:
            content.append(file_line.replace(str(last_released_version()), current_release_version()))
            # content.append(file_line.replace(str(last_released_version()), sys.argv[1]))
        else:
            content.append(file_line)
    return content


def update_lines():
    for extension_parameters in getattr(json_content().extensions, str(sys.argv[2]).replace("-ee", '')):
        content = []
        version_differences(extension_parameters.filename, content, extension_parameters.version)
        # file_name = open('/Users/adis.brkic/IdeaProjects/woocommerce-ee/wirecard-woocommerce-extension/woocommerce-wirecard-payment-gateway.php', 'w')
        file_name = open(os.path.abspath(subprocess.check_output("find ../" + sys.argv[2] + " -name " + extension_parameters.filename, shell=True, text=True)).rstrip(), 'w')
        for file_line in content:
            file_name.write(file_line)
        file_name.close()


if __name__ == "__main__":
    update_lines()
