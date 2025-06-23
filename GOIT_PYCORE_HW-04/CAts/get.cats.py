from pathlib import Path

path = Path(__file__).parent/"cat_path.txt"

def get_cats_info(path):
    new_cats_info = []
    try:
        with open (path, "r", encoding="utf-8") as file:
             cats = file.readlines()
             for cat in cats:
                formated_cat_info = cat.strip().split(",")
                
                cat_formated = {
                    "id" : formated_cat_info[0], 
                    "name" : formated_cat_info [1],
                    "age" : formated_cat_info [2]
                }  
                new_cats_info.append(cat_formated)     
        return new_cats_info       
    except FileNotFoundError:
        
        return("Не вдалося знайти файл")
    
cat = get_cats_info(path)
print(cat)