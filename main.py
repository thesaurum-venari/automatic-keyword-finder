import json
import src.keyfinder as keyfinder

destination_file = open("static-data/results.txt", "w+")

with open('static-data/data.json') as data_file:
    data = json.load(data_file)

metadata_array = data['metadata']
items_analyzed = 0

for item in metadata_array:
    if item["country"] == "Australia":
        text = item["english_description"]

        item_potential_keys = keyfinder.find_keywords(text)
        destination_file.write("The article with ID {0} and Catalog Record ID {1} has these potential keys:\n".format(item["id"], item["catalog_record_id"]))
        for key in item_potential_keys:
            destination_file.write(key + "\n")

        destination_file.write("\n*********\n\n\n")

