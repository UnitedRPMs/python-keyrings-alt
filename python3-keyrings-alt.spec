%global srcname keyrings.alt

Name:           python3-keyrings-alt
Version:        3.4.0
Release:        1%{?dist}
Summary:        Alternate keyring implementations for python-keyring

License:        MIT
URL:            https://pypi.python.org/pypi/keyrings.alt
Source0:        %pypi_source keyrings.alt

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-keyring
BuildRequires:  python3-crypto
Requires:       python3-crypto


%description
Alternate keyring backend implementations for use with the python-keyring\
package.


%prep
%autosetup -n %{srcname}-%{version} 

  echo -e '\nflake8-ignore = W191 W503 W504' >> pytest.ini

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%files 
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/keyrings/

%changelog

* Tue Feb 18 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.4.0-1
- Drop python2 package
- Updated to 3.4.0

* Tue Feb 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1.1-2
- Updated to 3.1.1

* Fri Jul 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1-1
- Updated to 3.1

* Wed Sep 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.1-1
- Initial package
