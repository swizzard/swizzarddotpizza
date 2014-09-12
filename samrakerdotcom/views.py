from django.shortcuts import render_to_response


def main(request):
    return render_to_response("new/main.html")


def load_etc(request):
    return render_to_response("new/else.html")


def load_cv(request):
    return render_to_response("new/cv.html")


def load_vst(request):
    return render_to_response("new/vst.html")
