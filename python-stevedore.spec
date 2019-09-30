# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc Manage dynamic plugins for Python applications

Name:           python-stevedore
Version:        1.31.0
Release:        2%{?dist}
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/openstack/stevedore
Source0:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-six
BuildRequires:  python%{pyver}-testrepository
#BuildRequires:  python%{pyver}-discover
#BuildRequires:  python%{pyver}-oslotest

%description
%{common_desc}

%package -n python%{pyver}-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries
%{?python_provide:%python_provide python%{pyver}-stevedore}

Requires:       python%{pyver}-six
Requires:       python%{pyver}-pbr

%description -n python%{pyver}-stevedore
%{common_desc}

%prep
%setup -q -n stevedore-%{upstream_version}

# let RPM handle deps
rm -f requirements.txt

%build
%{pyver_build}

%install
%{pyver_install}

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

%files -n python%{pyver}-stevedore
%license LICENSE
%doc README.rst
%{pyver_sitelib}/stevedore
%{pyver_sitelib}/stevedore-*.egg-info

%changelog
* Thu Oct 03 2019 Joel Capitao <jcapitao@redhat.com> 1.31.0-2
- Removed python2 subpackages in no el7 distros

* Mon Sep 16 2019 RDO <dev@lists.rdoproject.org> 1.31.0-1
- Update to 1.31.0

