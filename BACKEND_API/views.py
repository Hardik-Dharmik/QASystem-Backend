from django.http import JsonResponse

import json
import requests

API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/hd94/roberta-hindi"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    resp = json.loads(response.content.decode("utf-8"))
    return resp["answer"], response.status_code


def index(request):
    if request.method == 'POST':
        context = request.POST.get('context')
        question = request.POST.get('question')

        data, status_code = query({
                "inputs": {
                    "question": question,
                    "context": context,
                }
            }
        )

        if status_code == 500:
            return JsonResponse({'answer' : "Internal Server Error !!", 'status' : status_code, "error" : True})

        if status_code == 400:
            return JsonResponse({'answer' : "Bad Request from Client !!", 'status' : status_code, "error" : True})

        if status_code == 200:
            return JsonResponse({'answer' : data, 'status' : status_code, "error" : False})
            
    return JsonResponse({'error' : 'ERROR!!!'})