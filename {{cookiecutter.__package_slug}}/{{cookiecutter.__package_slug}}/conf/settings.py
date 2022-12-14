from pydantic import BaseSettings

{%- if cookiecutter.include_sqlalchemy == "y" %}
from .db import DatabaseSettings

class Settings(BaseSettings, DatabaseSettings):
{% else %}
class Settings(BaseSettings):
{% endif %}
    project_name: str = "{{ cookiecutter.package_name }}"
    debug: bool = False

