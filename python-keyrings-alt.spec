%global srcname keyrings.alt
%global modname %(n=%{srcname}; echo ${n//./-})

Name:           python-keyrings-alt
Version:        3.1
Release:        2%{?dist}
Summary:        Alternate keyring implementations for python-keyring

# No license in archive nor in repo
# https://github.com/jaraco/keyrings.alt/issues/6
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Alternate keyring backend implementations for use with the python-keyring\
package.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
BuildRequires:  python-keyring
BuildRequires:  python-gdata
BuildRequires:  python-keyczar
BuildRequires:  python2-crypto
Recommends:     python-gdata
Recommends:     python-keyczar
Requires:       python2-crypto

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-keyring
BuildRequires:  python3-crypto
Requires:       python3-crypto

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} 

  echo -e '\nflake8-ignore = W191 W503 W504' >> pytest.ini

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py2_build
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py2_install
%py3_install

%files -n python2-%{modname}
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info/
%dir %{python2_sitelib}/keyrings/
%{python2_sitelib}/keyrings/alt/
%{python2_sitelib}/keyrings/__init__.py
%{python2_sitelib}/keyrings/__init__.pyc
%{python2_sitelib}/keyrings/__init__.pyo


%files -n python3-%{modname}
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%dir %{python3_sitelib}/keyrings/
%{python3_sitelib}/keyrings/alt/
%{python3_sitelib}/keyrings/__init__.py
%{python3_sitelib}/keyrings/__pycache__/__init__.cpython-*.opt-1.pyc
%{python3_sitelib}/keyrings/__pycache__/__init__.cpython-*.pyc

%changelog

* Fri Jul 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1-1
- Updated to 3.1

* Wed Sep 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.1-1
- Initial package
