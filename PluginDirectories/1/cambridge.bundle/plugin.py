def results(fields, original_query):
    url = "http://dictionary.cambridge.org/dictionary/english/"
    if not fields:
        return dict(
            title="Open cambridge dictionary in browser",
            run_args=[url]
        )

    query = "-".join(fields['~query'].split())
    url = "{}{}".format(url, query)
    html = "<script>setTimeout(function() {{window.location = '{}'}}, 400);</script>".format(url)
    return {
        "title": "Cambridge search for {}".format(fields["~query"]),
        "run_args": [url],
        "html": html,
        "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"
    }


def run(url):
    import os
    os.system('open "{0}"'.format(url))
