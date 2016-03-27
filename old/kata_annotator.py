import json
import os

def add_bunkai_annotation_for_movement(kata_uuid, start_movement_count, end_movement_count, annotation):
    with open("kata.json", mode="r") as kata:
        kata_list = json.load(kata)
        for kata in kata_list:
            if kata.get("uuid", "") == kata_uuid:
                relative_path_to_annotated = kata.get("relative_path_to_annotated", "")
    
    with open(relative_path_to_annotated, mode="r") as movements_in:
        movements = json.load(movements_in)
        
        current_count = start_movement_count
        while current_count <= end_movement_count:
            for movement in movements:
                if movement.get("count", "") == current_count and annotation not in movement.get("bunkai_annotations", ""):
                    movement["bunkai_annotations"].append(annotation)
            current_count += 1
    
        with open(relative_path_to_annotated, mode="w") as movements_out:
            movements_out.write(json.dumps(movements))

def add_bunkai_annotation_for_technique(technique_uuid, annotation):
    relative_paths_to_annotated = []
    with open("kata.json", mode="r") as kata:
        kata_list = json.load(kata)
        for kata in kata_list:
            relative_paths_to_annotated.append(kata.get("relative_path_to_annotated", ""))
    
    for relative_path_to_annotated in relative_paths_to_annotated:
        if os.path.isfile(relative_path_to_annotated):
            with open(relative_path_to_annotated, mode="r") as movements_in:
                movements = json.load(movements_in)
                
                for movement in movements:
                    for uuid in movement["technique_uuid"]:
                        if annotation not in movement.get("bunkai_annotations", ""):
                            movement["bunkai_annotations"].append(annotation)
            
                with open(relative_path_to_annotated, mode="w") as movements_out:
                    movements_out.write(json.dumps(movements))

def add_performance_annotation_for_movement(kata_uuid, start_movement_count, end_movement_count, annotation):
    with open("kata.json", mode="r") as kata:
        kata_list = json.load(kata)
        for kata in kata_list:
            if kata.get("uuid", "") == kata_uuid:
                relative_path_to_annotated = kata.get("relative_path_to_annotated", "")
    
    with open(relative_path_to_annotated, mode="r") as movements_in:
        movements = json.load(movements_in)
        
        current_count = start_movement_count
        while current_count <= end_movement_count:
            for movement in movements:
                if movement.get("count", "") == current_count and annotation not in movement.get("performance_annotations", ""):
                    movement["performance_annotations"].append(annotation)
            current_count += 1
                    
        with open(relative_path_to_annotated, mode="w") as movements_out:
            json.dump(movements, movements_out)

def add_performance_annotation_for_technique(technique_uuid, annotation):
    relative_paths_to_annotated = []
    with open("kata.json", mode="r") as kata:
        kata_list = json.load(kata)
        for kata in kata_list:
            relative_paths_to_annotated.append(kata.get("relative_path_to_annotated", ""))
    
    for relative_path_to_annotated in relative_paths_to_annotated:
        if os.path.isfile(relative_path_to_annotated):
            with open(relative_path_to_annotated, mode="r") as movements_in:
                movements = json.load(movements_in)
                
                for movement in movements:
                    for uuid in movement["technique_uuid"]:
                        if uuid == technique_uuid and annotation not in movement.get("performance_annotations", ""):
                            movement["performance_annotations"].append(annotation)
            
                with open(relative_path_to_annotated, mode="w") as movements_out:
                    movements_out.write(json.dumps(movements)) 
                