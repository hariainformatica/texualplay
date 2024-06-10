# Sunday Project with Textual

## Working with conda:
https://code.visualstudio.com/docs/python/environments

https://conda.io/projects/conda/en/latest/user-guide/getting-started.html
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

### Extensión para trabajar con conda
Extensión para gestionar los ambientes de conda
Environments in conda

    donjayamanne.python-environment-manager



### Comandos de conda

#### Actualizar
    conda   update conda
            update --force conda
            update --all

#### Listar
    conda   info --envs
    conda   env list

#### Crear
    conda   create --name <my-env>
    
    conda   env create -f environment.yml

    conda   create --prefix ./envs
#### Exportar    
    conda   env export > environment.yml
    conda   env export --from-history

#### Activar / Desactivar
    conda   activate ./.conda
    conda   deactivate

#### Eliminar
    conda   remove --name myenv --all

## Working with Poetry
https://medium.com/@silvinohenriqueteixeiramalta/conda-and-poetry-a-harmonious-fusion-8116895b6380

    conda install poetry
    poetry init

    poetry add textual
    poetry add textual-dev