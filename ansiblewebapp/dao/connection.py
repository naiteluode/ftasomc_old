# coding:utf-8
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
connection = sqlite3.connect(os.path.join(BASE_DIR, 'db/ansible_web.db'), check_same_thread=False)
