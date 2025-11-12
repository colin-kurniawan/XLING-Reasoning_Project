import os
import json
import sacrebleu
import evaluate 

def main(): 
    #Folder path to access .jsonl files
    folder_path = "reasoning_json_files"
    
    #Different types of translation
    translations = ["direct_translation", "self-CoT-translation", "teacher-CoT-translation"]

    #translation_scores holds the sacrebleu score for each language pair and model
    translation_scores = {}

    empty_translation_count = 0
    sacrebleu = evaluate.load("sacrebleu")

    #Iterates through all .jsonl files
    for file in os.listdir(folder_path):
        if file.endswith(".jsonl"):
            file_path = os.path.join(folder_path, file)

            with open(file_path, "r", encoding="utf-8") as f:
                #Iterates through all files
                for line in f:
                    #Loads each json object as a dict
                    file_data = json.loads(line)

                    #Iterates through three different translations to find which translation that line uses
                    for translation in translations: 
                        #Conditional to check for which translation is used
                        if translation in file_data:
                            translation_value = file_data.get(translation)
                            
                            #Handles empty translations
                            if translation_value == "":
                                empty_translation_count += 1
                                break
                            else:
                                #predictions and references used for each sacrebleu test
                                predictions = []
                                references = []

                                lp = file_data["lp"]
                                model = file_data["model"]

                                #Initializes language pair and model
                                translation_scores.setdefault(lp, {})
                                translation_scores[lp].setdefault(model, {})
                                translation_scores[lp][model].setdefault(translation, {"scores": 0, "count": 0, "average_score": 0})

                                #Initializes predictions and references for test 
                                predictions.append(file_data[translation])
                                references.append(file_data["reference"]) 

                                #Runs sacrebelu test                             
                                result = sacrebleu.compute(predictions=predictions,references=references)
                                
                                #Adds to score and plus one for count
                                translation_scores[file_data["lp"]][file_data["model"]][translation]["scores"] += result["score"]
                                translation_scores[file_data["lp"]][file_data["model"]][translation]["count"] += 1
                                
                                #For second reference
                                references = []
                                references.append(file_data["reference2"])
                                result = sacrebleu.compute(predictions=predictions,references=references)
                                
                                #Adds to score and count field. Updates average score field for each lp and model
                                translation_scores[file_data["lp"]][file_data["model"]][translation]["scores"] += result["score"]
                                translation_scores[file_data["lp"]][file_data["model"]][translation]["count"] += 1
                                translation_scores[file_data["lp"]][file_data["model"]][translation]["average_score"] =  translation_scores[file_data["lp"]][file_data["model"]][translation]["scores"] / translation_scores[file_data["lp"]][file_data["model"]][translation]["count"]
                                break
    
    #Prints out all information for each lp and model
    for language_pair, models in translation_scores.items():
        print(f"------------------------------------------------------{language_pair}------------------------------------------------------")
        for model_name, translations_dict in models.items():
            print(f"Model: {model_name}")
            for translation in translations:
                if translation in translations_dict:
                    avg_score = translations_dict[translation]["average_score"]
                    print(f"  Method: {translation}, Average Score: {avg_score}")
        print("-----------------------------------------------------------------------------------------------------------------\n\n")


    print(f"Total Empty Translation: {empty_translation_count}\n")
    

if __name__ == "__main__":
    main()