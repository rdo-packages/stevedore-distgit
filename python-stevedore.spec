%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc Manage dynamic plugins for Python applications

Name:           python-stevedore
Version:        1.28.0
Release:        1%{?dist}
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/openstack/stevedore
Source0:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-mock
BuildRequires:  python2-six
BuildRequires:  python2-testrepository
#BuildRequires:  python2-discover
#BuildRequires:  python2-oslotest

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
%{common_desc}

%package -n python2-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries
%{?python_provide:%python_provide python2-stevedore}

Requires:       python2-six
Requires:       python2-pbr

%description -n python2-stevedore
%{common_desc}

%if 0%{?with_python3}
%package -n python3-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries
%{?python_provide:%python_provide python3-stevedore}

Requires:       python3-six
Requires:       python3-pbr

%description -n python3-stevedore
%{common_desc}
%endif

%prep
%setup -q -n stevedore-%{upstream_version}

# let RPM handle deps
rm -f requirements.txt

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build

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

%{__python2} setup.py install --skip-build --root %{buildroot}

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

%files -n python2-stevedore
%license LICENSE
%doc README.rst
%{python2_sitelib}/stevedore
%{python2_sitelib}/stevedore-*.egg-info

%if 0%{?with_python3}
%files -n python3-stevedore
%license LICENSE
%doc README.rst
%{python3_sitelib}/stevedore
%{python3_sitelib}/stevedore-*.egg-info
%endif

%changelog
* Fri Feb 09 2018 Alfredo Moralejo <amoralej@redhat.com> 1.28.0-1
- Update to 1.28.0

