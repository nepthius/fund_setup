from markdown import markdown
from weasyprint import HTML
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import io

template_dir = Path(__file__).resolve().parent.parent/ "templates" #I'm keeping it local in the fd for now since it's only a few templates
env = Environment(loader=FileSystemLoader(template_dir))

def render_legal_doc(template_name: str, fund_data: dict) -> str:
    template = env.get_template(template_name)
    temp = template.render(fund=fund_data) # this is text rn
    html = markdown(temp)
    pdf = HTML(string=html).write_pdf()  
    return pdf