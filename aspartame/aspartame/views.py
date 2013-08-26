from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.utils import simplejson
import uuid

BASEDIR = 'sessions'

def get_session(sid):
    session_data = None
    try:
        session_file = open("{dir}/{fname}".format(dir=BASEDIR, fname=sid), 'r')
        session_data = simplejson.loads(session_file.read())
    except:
        pass

    return session_data

def save_session(sid, session_data):
    session_file = open("{dir}/{fname}".format(dir=BASEDIR, fname=sid), 'w')
    session_file.write(simplejson.dumps(session_data))
    session_file.close()


def home(request):
    etag = None
    if 'HTTP_IF_NONE_MATCH' in request.META:
        etag = request.META['HTTP_IF_NONE_MATCH']
    else:
        etag = uuid.uuid4()

    session_data = get_session(etag)
    if not session_data:
        session_data = {}
        session_data['visits'] = 1
    else:
        session_data['visits'] += 1

    save_session(etag, session_data)
    response = HttpResponse("Visits: {vnum}".format(vnum=session_data['visits']))
    response['ETag'] = etag
    response['Cache-Control'] = 'Cache-Control:private, must-revalidate, proxy-revalidate'
    return response

def redirect(request, id=None):
    if id is None:
        response = HttpResponsePermanentRedirect("/redirect/{id}/".format(id=uuid.uuid4()))
    else:
        response = render(request, "id_writer.html", {'id': id})

    return response

def redirect_container(request):
    return render(request, "redirect_tracking.html")
