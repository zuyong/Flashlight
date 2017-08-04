import urllib
import json
import re
import base64

settings = json.load(open('preferences.json'))

def results(parsed, original_query):
    search_specs = [
        ["jira", "~query", "/issues/"]
    ]
    for name, key, url in search_specs:
        if key in parsed:
            user = urllib.quote_plus(settings.get("user").encode('UTF-8'))
            password = urllib.quote_plus(settings.get("password").encode('UTF-8'))
            project = urllib.quote_plus(settings.get("project").encode('UTF-8')) +'-'
            auth = base64.b64encode(user+":"+password)
            basic = '?os_authType=basic'
            host = settings.get("host")

        regexJIRA = re.compile("^ *(?P<proj>\w+-)?(?P<jira>\d+) *$")
        searchJIRA = regexJIRA.search(parsed[key].encode('UTF-8'))
        if searchJIRA:
            if searchJIRA.group('proj'):
                project = searchJIRA.group('proj')
            ticket = project.upper() + urllib.quote_plus(searchJIRA.group('jira').encode('UTF-8'))
            search_url = host + "/browse/" + ticket + basic
        search_url = search_url.replace("a%26%23776%3B", "%C3%A4") \
            .replace("A%26%23776%3B", "%C3%84") \
            .replace("o%26%23776%3B","%C3%B6").replace("O%26%23776%3B","%C3%96") \
            .replace("u%26%23776%3B","%C3%BC").replace("U%26%23776%3B","%C3%9C") \
            .replace("%26%23223%3B","%C3%9F")

        # html = """%s""" % ((json.dumps(search_url)))
        html = (open("jira.html").read().decode('utf-8') .replace("<!--url-->", json.dumps(search_url)).replace("<!--ticket-->", ticket).replace("<!--auth--!>", auth).replace("<!--host--!>", host))

        if (settings.get("user", "") == "") or (settings.get("password","") == "") or (settings.get("host", "") == ""):
            html = "Please enter user information in flashlight in the settings of the jira plugin first"
        # return {
        #         "title": "title" + parsed[key].encode('UTF-8'),
        #         "run_args": ["search_url"],
        #         "html": "test668899",
        #         "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 " +
        #         "Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0" +
        #         " Mobile/11A465 Safari/9537.53",
        #         "webview_links_open_in_browser": True
        # }
        title = "Search {0} for '{1}'".format(name, parsed[key])

        return {
            "title": title,
            "run_args": [search_url],
            "html": html,
            "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
            "webview_links_open_in_browser": True
        }


def run(url):
    import os
    os.system('open "{0}"'.format(url))
