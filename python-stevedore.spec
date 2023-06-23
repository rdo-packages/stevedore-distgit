%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx coverage

%global common_desc Manage dynamic plugins for Python applications

Name:           python-stevedore
Version:        XXX
Release:        XXX
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        Apache-2.0
URL:            https://github.com/openstack/stevedore
Source0:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source1:        https://tarballs.openstack.org/stevedore/stevedore-%{upstream_version}.tar.gz.asc
Source2:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
#BuildRequires:  python3-discover
#BuildRequires:  python3-oslotest

%description
%{common_desc}

%package -n python3-stevedore
Summary:        Manage dynamic plugins for Python applications
Group:          Development/Libraries



%description -n python3-stevedore
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q -n stevedore-%{upstream_version}


sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done
%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox -e %{default_toxenv}

%files -n python3-stevedore
%license LICENSE
%doc README.rst
%{python3_sitelib}/stevedore
%{python3_sitelib}/stevedore-*.dist-info

%changelog
