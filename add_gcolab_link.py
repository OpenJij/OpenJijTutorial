import json
import glob
import os
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO


logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler()
formatter = Formatter('{} - %(levelname)s - %(message)s'.format(__file__))
handler.setFormatter(formatter)
handler.setLevel(INFO)
logger.addHandler(handler)


# should include '/' at the end.
GITHUB_LINK = 'OpenJij/OpenJijTutorial/blob/master/'


def add_google_colab_link(nb_name, github_link, output_nb):
    with open(nb_name, "r", encoding='utf-8') as f:
        nb_json = json.load(f)

    # Check if the second cell has a Colab link
    def check_colab_link(cell):
        if cell['cell_type'] != 'markdown':
            return False
        elif '[![Open in Colab]' in cell['source'][0] or '<a href="https://colab' in cell['source'][0]:
            return True
        else:
            return False
    exist_colab_link = check_colab_link(nb_json['cells'][1])

    if exist_colab_link:
        logger.debug('\tThis notebook already has a colab link.')
        return None

    colab_img = 'https://colab.research.google.com/assets/colab-badge.svg' 
    colab_link = '[![Open in Colab]({img})](https://colab.research.google.com/github/{github})'
    colab_link = colab_link.format(github=github_link, img=colab_img)

    colab_cell = {
        'cell_type': 'markdown',
        'metadata': {'colab_type': 'text', 'id': 'view-in-github'},
        'source': [colab_link]
    }

    # insert colab link to the second cell in the notebook
    nb_json['cells'].insert(1, colab_cell)


    with open(output_nb, 'w') as fw:
        json.dump(nb_json, fw, indent=4)
    logger.info("add Colab Link to '{}'".format(output_nb))


def add_colablink_to_notebooks():
    nb_list = glob.glob('./source/**/*.ipynb')
    logger.debug('Find {} notebooks.'.format(len(nb_list)))
    for nb in nb_list:
        nb = nb.replace(os.path.sep, '/')
        logger.debug('Notebook: {}'.format(nb))
        add_google_colab_link(nb, github_link=GITHUB_LINK + nb[2:], output_nb=nb)




if __name__ == "__main__":
    add_colablink_to_notebooks()
