from pathlib import Path
from os import system

# ADMINISTRADOR DE RECETAS

recipe_path = Path("Recetas")
recipe_quantity = len(list(Path(recipe_path).glob('*/**.txt')))
print(f"Bienvenido al administrador de recetas en python, la ruta de la carpeta de recetas se encuentra en: {recipe_path}, actualmente tienes {recipe_quantity} recetas")

def read_recipe(recipe_path):
    return Path(recipe_path).read_text()

def show_categories():
    return [category.name for category in recipe_path.glob('*')]

def show_recipes(cactegory_path: Path):
    return [recipe.name for recipe in cactegory_path.glob('*.txt')]


def select_category():
    system("cls")
    print("Categorias disponibles:")
    for index, category in enumerate(show_categories()):
        print(f"[{index + 1}] - {category}")
    return input("Escoge una categoria: ")

def select_recipe(category_index):
    system("cls")
    print("Recetas disponibles:")
    category_path = recipe_path / show_categories()[int(category_index) - 1]
    for index, recipe in enumerate(show_recipes(category_path)):
        print(f"[{index + 1}] - {recipe}")
    recipe_index = input("Escoge la receta a leer: ")
    selected_recipe = show_recipes(category_path)[int(recipe_index) - 1]
    print(Path(category_path / selected_recipe).read_text())

def remove_recipe(category_index):
    system("cls")
    print("Recetas disponibles:")
    category_path = recipe_path / show_categories()[int(category_index) - 1]
    for index, recipe in enumerate(show_recipes(category_path)):
        print(f"[{index + 1}] - {recipe}")
    recipe_index = input("Escoge la receta a eliminar: ")
    selected_recipe = show_recipes(category_path)[int(recipe_index) - 1]
    Path(category_path / selected_recipe).unlink()
    print(f"Receta {selected_recipe} eliminada exitosamente")

def create_file(category_index):
    category_path = recipe_path / show_categories()[int(category_index) - 1]
    file_name = input("Ingresa el nombre de la receta: ")
    recipe_content = input("Ingresa el contenido de la receta: ")
    Path(category_path, f"{file_name}.txt").write_text(recipe_content)
    print(f"Receta {file_name}.txt creada exitosamente")


def ask_option():
    option = input('''
    [1] - leer receta
    [2] - crear receta
    [3] - crear categoria
    [4] - eliminar receta
    [5] - eliminar categoria
    [6] - finalizar programa                                             
    Escoge una opcion: ''') 

    match option:
        case '1':
            selected_category_index = select_category()           
            select_recipe(selected_category_index)
            ask_option()
        case '2':
            selected_category_index = select_category()
            create_file(selected_category_index)
            ask_option()
        case '3':
            category_name = input("Ingresa el nombre de la categoria que quieres crear: ")
            Path(recipe_path, category_name).mkdir()         
            print(f"Categoria {category_name} creada exitosamente")
            ask_option()
        case '4':
            selected_category_index = select_category()   
            remove_recipe(selected_category_index)
            ask_option()        
        case '5':
            selected_category_index = select_category()
            Path(recipe_path / show_categories()[int(selected_category_index) - 1]).rmdir()
            print("Categoria eliminada exitosamente")
            ask_option()
        case '6':
            pass
        case _:
            system("cls")
            print("Opcion no valida, selecciona nuevamente una opcion valida")
            ask_option()

ask_option()