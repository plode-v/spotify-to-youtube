from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()


client = os.environ.get("CLIENT_ID")

print(client)
