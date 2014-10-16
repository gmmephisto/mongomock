%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define pkgname mongomock

Summary:    Python mock library for PyMongo
Name:       python-%{pkgname}
Version:    2.0.0
Release:    CROC1
License:    BSD
Group:      Development/Languages
URL:        https://github.com/vmalloc/mongomock
Source0:    %{pkgname}-%{version}.tar.gz
Source1:    https://pypi.python.org/packages/source/m/mongomock/%{pkgname}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: python-devel, python-setuptools
Requires:      python-orderdict, python-six, python-sentinels

%description
Mongomock is a small library to help testing Python code that
interacts with MongoDB via Pymongo.


%prep
%setup -q -n %{pkgname}-%{version}

# TODO: Have the following handle multi line entries
sed -i '/setup_requires=/d; /install_requires=/d; /dependency_links=/d' setup.py


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

find $RPM_BUILD_ROOT/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


%clean
rm -rf %{buildroot}


%files
%defattr(0644,root,root,-)
%doc README.rst LICENSE
%{python2_sitelib}/mongomock*


%changelog
* Thu Oct 16 2014 Mikhail Ushanov <gm.mephisto@gmail.com> 2.0.0-CROC1
- Update to latest version.
- Changes in spec.

* Thu Apr 03 2014 Chris St. Pierre <chris.a.st.pierre@gmail.com> 1.2.0-1
- Initial build.
