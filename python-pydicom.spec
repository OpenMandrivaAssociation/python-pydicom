%global module pydicom
%global mod %(m=pydicom; echo ${m:0:1})

Summary:	Read, modify and write DICOM files with python code
Name:		python-pydicom
Version:	2.4.1
Release:	1
Group:          Development/Python
# There are generated data (private dict) in special format from GDCM
License:	MIT and BSD
URL:		https://github.com/darcymason/pydicom
Source0:	https://github.com/pydicom/pydicom/archive/refs/tags/v%{version}/pydicom-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/p/pydicom/pydicom-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)
# test
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(python-dateutil)

BuildArch:	noarch

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

%files
%license LICENSE
%doc README.md
%{_bindir}/pydicom
%{py_sitedir}/pydicom
%{py_sitedir}/pydicom-%{version}-py%{python_version}.*-info/

#-----------------------------------------------------------------------

%prep
%autosetup -n pydicom-%{version}

%build
%py_build

%install
%py_install

