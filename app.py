from flask import Flask, request, redirect, render_template, jsonify, abort
from database import init_db, create_link, get_link, record_click, get_all_links

app = Flask(__name__)
