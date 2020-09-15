
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc Manage dynamic plugins for Python applications

Name:           python-stevedore
Version:        XXX
Release:        XXX
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/openstack/stevedore
Source0:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?dlrn} == 0
Source1:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz.asc
Source2:        https://releases.openstack.org/_static/0x2426b928085a020d8a90d0d879ab7008d0896c8a.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?dlrn} == 0
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-mock
BuildRequires:  python3-testrepository
#BuildRequires:  python3-discover
#BuildRequires:  python3-oslotest

%description
%{common_desc}

%package -n python3-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries
%{?python_provide:%python_provide python3-stevedore}

Requires:       python3-pbr >= 2.0.0
Requires:       python3-importlib-metadata >= 1.7.0

%description -n python3-stevedore
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?dlrn} == 0
%{gpgverify}  --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q -n stevedore-%{upstream_version}

# let RPM handle deps
rm -f requirements.txt

%build
%{py3_build}

%install
%{py3_install}

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

%files -n python3-stevedore
%license LICENSE
%doc README.rst
%{python3_sitelib}/stevedore
%{python3_sitelib}/stevedore-*.egg-info

%changelog
