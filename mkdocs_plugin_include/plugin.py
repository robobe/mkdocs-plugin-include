# https://www.mkdocs.org/dev-guide/plugins/
import warnings
from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from jinja2 import Template
import os.path

class CodeInclude(BasePlugin):
    config_scheme = (
        ('base_path', config_options.Type(str, default='')),
    )

    def on_page_markdown(self, markdown, page, config, files):
        # warnings.warn("Hello world")
        # markdown = markdown.replace("{{include}}", "Hello World")
        md_template = Template(markdown)
        return md_template.render(include=self.include)

    def include(self, file_path, start=0, stop=None):
        f = None
        try:
            if not os.path.isabs(file_path):
                file_path = os.path.join(self.config["base_path"], file_path)

            if not os.path.exists():
                msg = "file not found {}".format(file_path)
                warnings.warn("file not found {}".format(file_path))
                return "file not found {}".format(file_path)

            f = open(file_path)
            content = f.readlines()

            if stop:
                return "".join(content[start:stop])
            else:
                return "".join(content[start:])
        finally:
            if f:
                f.close()


