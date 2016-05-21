%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-stevedore
Version:        XXX
Release:        XXX
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/dreamhost/stevedore
Source0:        http://pypi.python.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  python-mock
BuildRequires:  python-six
BuildRequires:  python-testrepository
#BuildRequires:  python-discover
#BuildRequires:  python-oslotest

Requires:       python-setuptools
Requires:       python-six

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-mock
BuildRequires:  python3-six
#BuildRequires:  python3-testrepository
#BuildRequires:  python3-discover
#BuildRequires:  python3-oslotest
%endif

%description
Manage dynamic plugins for Python applications

%if 0%{?with_python3}
%package -n python3-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries

Requires:       python3-setuptools
Requires:       python-six

%description -n python3-stevedore
Manage dynamic plugins for Python applications
%endif

%prep
%setup -q -n stevedore-%{upstream_version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif

%{__python} setup.py install --skip-build --root %{buildroot}

%check
#TODO: reenable when commented test requirements above are available
#
#PYTHONPATH=. nosetests
#
#%if 0%{?with_python3}
#pushd %{py3dir}
#PYTHONPATH=. nosetests-%{python3_version}
#popd
#%endif

%files
%doc README.rst LICENSE
%{python_sitelib}/stevedore
%{python_sitelib}/stevedore-*.egg-info

%if 0%{?with_python3}
%files -n python3-stevedore
%doc README.rst LICENSE
%{python3_sitelib}/stevedore
%{python3_sitelib}/stevedore-*.egg-info
%endif

%changelog
