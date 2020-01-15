%global modname pydicom

Name:           python-%{modname}
Version:        1.3.0
Release:        2%{?dist}
Summary:        Read, modify and write DICOM files with python code

# There are generated data (private dict) in special format from GDCM
License:        MIT and BSD
URL:            https://github.com/darcymason/%{modname}
Source0:        https://github.com/darcymason/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
# Fixes python3.8 recursion error
# https://github.com/pydicom/pydicom/pull/938/commits/e6419c1fdad1db7ed1bbdab03a374b5aa27ce357
# https://github.com/pydicom/pydicom/issues/937
Patch0:         0001-Compatibility-fix-for-Python3.8.patch
BuildArch:      noarch
BuildRequires:  git-core

%description
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python-setuptools python-six
BuildRequires:  python-sphinx python-sphinx_rtd_theme python-numpydoc
# Test deps
BuildRequires:  python-numpy python-dateutil
#python-pytest
Requires:       python-dateutil
Recommends:     python-numpy
Recommends:     python-matplotlib
Recommends:     python-tkinter
Recommends:     python-pillow


%description -n python3-%{modname}
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -S git
# for docs:
git tag v%{version}


%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%license LICENSE
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/dicom.py
%{python3_sitelib}/__pycache__/dicom.*
