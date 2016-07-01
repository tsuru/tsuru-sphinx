from docutils import nodes
from docutils.parsers import rst

import yaml


class HandlersNode(nodes.Element):
    pass


class HandlersDirective(rst.Directive):
    def run(self):
        return [HandlersNode()]


def read_yaml(app):
    if not hasattr(app.env, 'handlers_yaml'):
        try:
            f = open('handlers.yml')
        except IOError:
            raise Exception("handlers.yml file not found")

        data = yaml.load(f.read())
        f.close()
        app.env.handlers = data


def render_handler(handler):
    title = handler['title']
    handler_items = []
    handler_items.append(nodes.title(title, title))
    items = []
    items.append(nodes.list_item('', nodes.paragraph(text="path: {}".format(handler['path']))))
    if "produce" in handler:
        items.append(nodes.list_item('', nodes.paragraph(text="produce: {}".format(handler['produce']))))
    if "consume" in handler:
        items.append(nodes.list_item('', nodes.paragraph(text="consume: {}".format(handler['consume']))))
    if "method" in handler:
        items.append(nodes.list_item('', nodes.paragraph(text="method: {}".format(handler['method']))))
    for status, desc in handler.get("responses", {}).items():
        items.append(nodes.list_item('', nodes.paragraph(text="{}: {}".format(status, desc))))

    handler_items.append(nodes.bullet_list('', *items))
    return handler_items


def build_docs(app, doctree):
    for node in doctree.traverse(HandlersNode):
        section = nodes.section('', ids=["handlers"])

        for handler in app.env.handlers.get('handlers', []):
            for item in render_handler(handler):
                section.append(item)

        node.replace_self(section)


def setup(app):
    app.add_directive('tsuru-handlers', HandlersDirective)
    app.connect(str('builder-inited'), read_yaml)
    app.connect(str('doctree-read'), build_docs)
