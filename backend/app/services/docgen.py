from jinja2 import Environment, FileSystemLoader
from pathlib import Path

template_dir = Path(__file__).resolve().parent.parent/ "templates" #I'm keeping it local in the fd for now since it's only a few templates
env = Environment(loader=FileSystemLoader(template_dir))

def render_legal_doc(template_name: str, fund_data: dict) -> str:
    template = env.get_template(template_name)
    return template.render(fund=fund_data)