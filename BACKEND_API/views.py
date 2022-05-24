from django.http import JsonResponse

import json
import requests

API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/hd94/roberta-hindi"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def index(request):
    if request.method == 'POST':
        context = request.POST.get('context')
        question = request.POST.get('question')

        data = query({
                "inputs": {
                    "question": question,
                    "context": context,
                }
            }
        )

        return JsonResponse({'data' : data})
    return JsonResponse({'error' : 'ERROR!!!'})