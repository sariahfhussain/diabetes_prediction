import os
import jupytext
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

def create_notebook_from_python_file(file_path):
    # Read the Python script
    with open(file_path, 'r') as f:
        script_content = f.read()

    # Convert Python script to Jupyter notebook
    notebook = jupytext.reads(script_content, fmt='py')
    
    # Add a markdown cell with the file path
    file_path_cell = new_markdown_cell(f"### Converted from {file_path}")
    notebook.cells.insert(0, file_path_cell)
    
    return notebook

def create_notebook_for_csv(file_path):
    # Create a new Jupyter notebook
    notebook = new_notebook()
    
    # Add a markdown cell with the file path
    file_path_cell = new_markdown_cell(f"### Data from {file_path}")
    notebook.cells.append(file_path_cell)
    
    # Add a code cell to load the CSV file
    load_csv_cell = new_code_cell(f"import pandas as pd\ndf = pd.read_csv('{file_path}')\ndf.head()")
    notebook.cells.append(load_csv_cell)
    
    return notebook

def save_notebook(notebook, notebook_path):
    # Save the Jupyter notebook
    with open(notebook_path, 'w') as f:
        nbformat.write(notebook, f)

def convert_project_to_notebooks(project_dir):
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Determine the notebook path by changing the file extension
            if file.endswith('.py'):
                notebook_path = file_path.replace('.py', '.ipynb')
                notebook = create_notebook_from_python_file(file_path)
                save_notebook(notebook, notebook_path)
            elif file.endswith('.csv'):
                notebook_path = file_path.replace('.csv', '_csv.ipynb')
                notebook = create_notebook_for_csv(file_path)
                save_notebook(notebook, notebook_path)

# Specify the path to your project directory
project_dir = 'C:\\Users\\saria\\OneDrive\\Desktop\\projects\\acc_car'

# Convert the project files to Jupyter notebooks
convert_project_to_notebooks(project_dir)

