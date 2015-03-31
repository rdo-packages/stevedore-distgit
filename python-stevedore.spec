%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-stevedore
Version:        1.3.0
Release:        1%{?dist}
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
Requires:       python-pbr

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
Requires:       python3-six
Requires:       python3-pbr

%description -n python3-stevedore
Manage dynamic plugins for Python applications
%endif

%prep
%setup -q -n stevedore-%{version}

# Remove setuptools dep.  We'll supply the rpm on epel.
sed -i '/argparse/d' requirements.txt

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

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/stevedore
%{python2_sitelib}/stevedore-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-stevedore
%license LICENSE
%doc README.rst
%{python3_sitelib}/stevedore
%{python3_sitelib}/stevedore-%{version}-py?.?.egg-info
%endif

%changelog
* Tue Mar 31 2015 Alan Pevec <apevec@redhat.com> - 1.3.0-1
- new version

* Mon Mar 30 2015 Ralph Bean <rbean@redhat.com> - 1.2.0-3
- Remove erroneous setuptools runtime dep on python-argparse.

* Sun Mar 22 2015 Ralph Bean <rbean@redhat.com> - 1.2.0-2
- Require python-pbr at runtime now.

* Sat Feb 21 2015 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Wed Oct 29 2014 Pádraig Brady <pbrady@redhat.com> - 1.1.0-1
- Latest upstream

* Mon Sep 22 2014 Alan Pevec <alan.pevec@redhat.com> 1.0.0-1
- Update to upstream 1.0.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Apr 03 2014 Ralph Bean <rbean@redhat.com> - 0.15-1
- Latest upstream
- Package python3-stevedore subpackage
- Add Requires on python-setuptools.
- Added a %%check section.

* Mon Jan 27 2014 Pádraig Brady <pbrady@redhat.com> - 0.14-1
- Latest upstream

* Mon Nov 11 2013 Matthias Runge <mrunge@redhat.com> - 0.12-1
- update to version 0.12
- fix FTBFS (rhbz#993170)

* Thu Sep 12 2013 Pádraig Brady <pbrady@redhat.com> - 0.11-1
- update to version 0.11

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Pádraig Brady <P@draigBrady.com> - 0.8-1
- Update to version 0.8

* Mon Dec 10 2012 Dan Prince <dprince@redhat.com> - 0.7.2-1
- Initial package.
