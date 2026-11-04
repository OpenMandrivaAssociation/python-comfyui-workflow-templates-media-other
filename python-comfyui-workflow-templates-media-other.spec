Name:		python-comfyui-workflow-templates-media-other
Version:	0.3.229
Release:	1
Summary:	Audio and 3D workflow preview media for ComfyUI
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates-media-other/comfyui_workflow_templates_media_other-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Preview media for ComfyUI's audio, 3D, and other workflow
templates. These are upstream media assets, not model weights.

%files
%{py_sitedir}/comfyui_workflow_templates_media_other
%{py_sitedir}/comfyui_workflow_templates_media_other-*.*-info
