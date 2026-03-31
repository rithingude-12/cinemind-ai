import zipfile
import xml.etree.ElementTree as ET

def extract_text(docx_path):
    with zipfile.ZipFile(docx_path) as docx:
        tree = ET.fromstring(docx.read('word/document.xml'))
        texts = []
        for node in tree.iter():
            if node.tag.endswith('}t') and node.text:
                texts.append(node.text)
            elif node.tag.endswith('}p'):
                texts.append('\n')
        return "".join(texts)

with open('doc_output.txt', 'w', encoding='utf-8') as f:
    f.write(extract_text(r'C:\Users\RithinGude\Desktop\promptfords.docx'))
