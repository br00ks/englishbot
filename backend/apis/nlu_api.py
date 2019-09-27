import requests, re, json


class NLUApi:
    """A service to communicate with the NLU server."""

    def __init__(self, server_url, server_port, verbose=False):
        self.api_url = "http://{}:{}".format(server_url, server_port)
        self.verbose = verbose

    def parse(self, input_text):
        """
        Calls the parse endpoint, which detects the intent and entities of a message.
        """
        url = self.api_url + "/model/parse"
        payload = {'text': input_text}
        headers = {'content-type': 'application/json'}

        r = requests.post(url, data=json.dumps(payload), headers=headers)

        if r.status_code != 200:
            raise ValueError(r.text)

        response_body = r.json()

        if self.verbose:
            print(response_body)

        return response_body
