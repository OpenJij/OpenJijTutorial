# How to contribute

The OpenJij Tutorial is constantly changing and can grow with your help.

You can participate in this project from a simple issue submission or typo correction.

We are also looking forward to more documentation on the latest research results in quantum optimization and quantum annealing, so requests are welcome.

## Submit requests and issues.

The easiest way to contribute is to report an issue 
or submit a request for documentation
on [GitHub issues](https://github.com/OpenJij/OpenJijTutorial/issues).

You can use both English and 日本語 (Japanese) languages in GitHub issues.
Don't worry about the language barrier.

GitHub Issues of the OpenJij Tutorial allows you to not only report a problem, but also to request a tutorial that you need.

Requests can also be made for documents on quantum annealing, adiabatic quantum computations, and theories in quantum optimization.


## How to edit and contribute by yourself

### 1. Setup enviroment by pipenv

First, clone from [GitHub repository](https://github.com/OpenJij/OpenJijTutorial).



Environment reproduction by pipenv

```
$ pipenv update
```

If `pandoc` is not in your environment, you may be required to install it. 
In that case, please refer to the installation method from [this link](https://pandoc.org/installing.html).

> The `pipenv` environment includes `sphinx` and other Python environments required for document generation.
> Note, however, that it does not contain the `numpy` or `openjij` required to run the Notebook.

### 2. Edit project

Once your environment is in place, edit or add your notebook and make the changes you want to make to this document.

The source code of the document is located under the `source` directory.

When you edit or add a Jupyter notebook, please follow [the rules of Jupyter notebook](#rules), even if it's a small thing.

### 3. Compile documents

You can compile documents to HTML files by make command.
```shell
$ make html
```

This command also executes

```shell
$ python add_gcolab_link.py
```

before compiling `sphinx`.

This python code inserts a link after the first cell of every notebook that can open the Notebook in Google Colab.

As you can see, the Google Colab link is inserted with the script so you don't have to insert it into the Notebook yourself.

If the compilation is successful, the generated HTML will be in the `build/html/` directory.
Please check it by referring to it.

## 4. Pull requests

When you're done editing, make pull requests to your master branch.

With pull requests, you don't need to publish the compiled products under `build/`.

Also, if you make changes to Jupyter Notebooks, please state in the pull requests comment where in the Notebook you made the changes, what you made the changes to, and why you made the changes, as it's hard to see the differences in the git diff.


<div id="rules"></div>

## The rules of Jupyter notebook


1. You need to put an `h1` level heading in the first cell.
    ```
    # Title of Notebook
    ```
2. Do not write anything other than the `h1` level title in the first cell.


