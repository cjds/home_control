from flask import escape
import functions_framework
from firebase_admin import firestore 


@functions_framework.http
def wise_lights(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    db = firebase_admin.firestore.client()

    doc_ref = db.collection(u'cities').document(u'SF')

    doc = doc_ref.get()
    if doc.exists:
        return (f'Document data: {doc.to_dict()}')
    else:
        return 'No such document!'

"""
import os
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

client = Client(email=os.environ['WYZE_EMAIL'], password=os.environ['WYZE_PASSWORD'])

try:
    response = client.devices_list()
    for device in client.devices_list():
        print(f"mac: {device.mac}")
        print(f"nickname: {device.nickname}")
        print(f"is_online: {device.is_online}")
        print(f"product model: {device.product.model}")
except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print(f"Got an error: {e}")
"""
