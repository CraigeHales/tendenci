from django.http import HttpResponse
from django.template.loader import get_template, select_template
from time import perf_counter
from addons.forestHome.cacher import cache_by_,reportElapsed,green,red,blue,yellow

def _strip_content_above_doctype(html):
    """Strips any content above the doctype declaration out of the
    resulting template. If no doctype declaration, it returns the input.

    This was done because content above the doctype in IE8 triggers the
    browser to go into quirks mode which can break modern HTML5 and CSS3
    elements from the theme.
    """
    try:
        doctype_position = html.index('<!D')
        html = html[doctype_position:]
    except ValueError:
        pass

    return html


# Render a response with some context about the top-level template, and with any
# content above the doctype declaration removed.
# Note that context_processors have no access to the template itself, so a
# context_processor cannot be used to add this template-related context.
def themed_response(request, template_name, context={}, content_type=None, status=None, using=None):
    """
    This is a direct replacement for django.shortcuts.render() which should be
    used in all views by replacing:
    from django.shortcuts import render as render_to_resp
    With:
    from tendenci.apps.theme.shortcuts import themed_response as render_to_resp
    """

    t1_start = perf_counter()
    print(f"\n{'='*32}\n{__file__[-32:]} is rendering ",template_name) # wch

    if isinstance(template_name, (list, tuple)):
        template = select_template(template_name, using=using)
    else:
        template = get_template(template_name, using=using)

    context['TEMPLATE_NAME'] = template.origin.template_name
    context['TEMPLATE_THEME'] = getattr(template.origin, 'theme', None)
    rendered = template.render(context=context, request=request)
    t1_stop = perf_counter()
    reportElapsed(t1_stop-t1_start,f"template render {template_name}\n{'='*32}\n\n",__file__)
    # elapsed = t1_stop-t1_start
    # color="32" if elapsed<.001 else "34" if elapsed<.002 else "33" if elapsed < .005 else "31" # https://stackoverflow.com/questions/58030468/how-to-have-colors-in-terminal-with-python-in-vscode
    # #     green                     blue                       yellow                     red
    # print(f"\033[{color}m{elapsed:.4f}\033[0m seconds  tendenci/apps/theme/shortcuts.py")
    rendered = _strip_content_above_doctype(rendered)

    return HttpResponse(rendered, content_type=content_type, status=status)
