import json
import glob


def add_googleClab_link(nb_name, github_link):
    with open(nb_name, "r", encoding='utf-8') as f:
        nb_json = json.load(f)

    # Check if the second cell has a Colab link
    def check_colab_link(cell):
        if cell['cell_type'] != 'markdown':
            return False
        elif '<a href="https://colab' in cell['source'][0]:
            return True
        else:
            return False
    exist_colab_link = check_colab_link(nb_json['cells'][1])

    if exist_colab_link:
        return None

    colab_img = 'https://colab.research.google.com/assets/colab-badge.svg' 
    colab_link = '<a href="https://colab.research.google.com/github/{}" target="_parent"><img src="{}" alt="Open In Colab"/></a>'
    colab_link = colab_link.format(github_link, colab_img)

    colab_cell = {
        'cell_type': 'markdown',
        'metadata': {'colab_type': 'text', 'id': 'view-in-github'},
        'source': [colab_link]
    }

    # insert colab link to the second cell in the notebook
    nb_json['cells'].insert(1, colab_cell)


    with open('sample.ipynb', 'w') as fw:
        json.dump(nb_json, fw)


def add_colablink_to_notebooks():
    nb_list = glob.glob('./source/**/*.ipynb')
    print(nb_list)




if __name__ == "__main__":
    add_googleClab_link("source/ja/2-Evaluation_errorbar.ipynb", github_link='')
    add_all_notebooks()
