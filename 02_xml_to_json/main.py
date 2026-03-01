from pathlib import Path
import xml.etree.ElementTree as ET
import json

BASE_DIR = Path(__file__).resolve().parent

# Convert parsed XML tree into list of flat dictionaries
def convert(tree):

    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    root = tree.getroot()

   

    #print(dir(root))
    #print(help(root))
    #print(type(root))

    #print(f"root.tag: {root.tag}, root.text: {root.text}, root.attrib: {root.attrib}, root.iter: {root.iter}, root.findall: {root.findall}")

    data = []

    # decide records
    if all(len(child) == 0 for child in root):
        records = [root]          # single record XML
    else:
        records = root            # multiple records XML

    for record in records:
        d = {}
        for i in record:
            if len(i) == 0 and i.text:
                d[i.tag] = i.text.strip()
        data.append(d)


    file_path = output_dir / "data.json"

    # Save converted data into JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Json saved to {file_path} ({len(data)} records)")


while True:
    print()
    user_path = input("Enter full file path: (or 'q' to quit) ").strip()
    print()
    
    default_xml = BASE_DIR / "input" / "data.xml"

    if user_path.lower() == 'q':
        print("Exiting...")
        break

    if not user_path:
        path = Path(default_xml)
        if path.is_file():
            print("No path provided — using default XML file")
        else:
            print("No file path provided, and the default XML file is missing.")
            continue
    else:
        path = Path(user_path)

    if path.is_file():
        # Only xml file allow
        if path.suffix == ".xml":
            with path.open("r", encoding="utf-8") as file:
                try:
                    tree = ET.parse(file)
                    print("XML file loaded successfully")
                    try:
                        convert(tree)
                    except Exception as e:
                        print(f"Error during conversion: {e}")
                except ET.ParseError:
                    print("Failed to parse XML")
        else:
            print("Invalid file type. Only .xml files are allowed.")
    else:
        print("File not found")




