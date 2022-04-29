from flask import Flask, request, jsonify
from lxml import etree
import re

app = Flask(__name__)


@app.route('/', methods=['post'])
def index():
    xml = request.form['xml']
    xml_tree = etree.fromstring(xml)

    paths = []

    tree = etree.ElementTree(xml_tree)
    for e in xml_tree.iter():
        e_str = etree.tostring(e, pretty_print=True).decode('utf-8')
        line = re.search('\<.*?\>', e_str)

        xpath = str(tree.getpath(e)).replace('/schema', '')

        paths.append({
            'line': line[0],
            'xpath': xpath
        })

    return jsonify({'paths': paths})
