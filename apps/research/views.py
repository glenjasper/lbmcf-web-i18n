from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    Project,
    Protocol,
    File
)

class ProjectView(ListView):
    model = Project
    queryset = Project.objects.all().filter(status = True)
    template_name = "research/projects.html"
    context_object_name = "context_projects"

class ProtocolView(ListView):
    template_name = "research/protocols.html"
    context_object_name = "context_protocols"

    def get_queryset(self):
        protocol_all = Protocol.objects.all().filter(status = True)

        _queryset = {}
        for item in protocol_all:
            protocol_type = item.type.name
            protocol_description = item.type.description

            protocol_item_name = item.name
            protocol_item_description = item.description
            protocol_item_pdf = item.pdf

            _protocol = {'name': protocol_item_name,
                        'description': protocol_item_description,
                        'pdf': protocol_item_pdf}

            if protocol_type not in _queryset:
                _queryset.update({protocol_type: {'description': protocol_description,
                                                  'items': [_protocol]}})
            else:
                _current = _queryset[protocol_type].copy()
                _current['items'].append(_protocol)
                _queryset.update({protocol_type: _current})

        return _queryset

class FileView(ListView):
    template_name = "research/files.html"
    context_object_name = "context_files"

    def get_queryset(self):
        file_all = File.objects.all().filter(status = True)

        _queryset = {}
        for item in file_all:
            file_type = item.type.name
            file_description = item.type.description

            file_item_name = item.name
            file_item_description = item.description
            file_item_pdf = item.pdf

            _file = {'name': file_item_name,
                     'description': file_item_description,
                     'pdf': file_item_pdf}

            if file_type not in _queryset:
                _queryset.update({file_type: {'description': file_description,
                                              'items': [_file]}})
            else:
                _current = _queryset[file_type].copy()
                _current['items'].append(_file)
                _queryset.update({file_type: _current})

        return _queryset
