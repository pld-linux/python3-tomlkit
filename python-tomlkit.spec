#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Style preserving TOML library
Summary(pl.UTF-8):	Biblioteka TOML zachowująca styl
Name:		python-tomlkit
# keep 0.7.x here for python2 support
Version:	0.7.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tomlkit/
Source0:	https://files.pythonhosted.org/packages/source/t/tomlkit/tomlkit-%{version}.tar.gz
# Source0-md5:	f754c55df5edfbb7395903061825e09e
URL:		https://pypi.org/project/tomlkit/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-enum34 >= 1.1
BuildRequires:	python-enum34 < 2
BuildRequires:	python-functools32 >= 3.2.3
BuildRequires:	python-functools32 < 4
BuildRequires:	python-pytest
BuildRequires:	python-typing >= 3.6
BuildRequires:	python-typing < 4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TOML Kit is a 1.0.0rc1-compliant TOML library.

It includes a parser that preserves all comments, indentations,
whitespace and internal element ordering, and makes them accessible
and editable via an intuitive API.

%description -l pl.UTF-8
TOML Kit to biblioteka TOML zgodna z 1.0.0rc1.

Zawiera parser zachowujący wszystkie komentarze, wcięcia, białe znaki
oraz kolejność elementów wewnętrznych i pozwalający na dostęp oraz
edycję poprzez intuicyjne API.

%package -n python3-tomlkit
Summary:	Style preserving TOML library
Summary(pl.UTF-8):	Biblioteka TOML zachowująca styl
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-tomlkit
TOML Kit is a 1.0.0rc1-compliant TOML library.

It includes a parser that preserves all comments, indentations,
whitespace and internal element ordering, and makes them accessible
and editable via an intuitive API.

%description -n python3-tomlkit -l pl.UTF-8
TOML Kit to biblioteka TOML zgodna z 1.0.0rc1.

Zawiera parser zachowujący wszystkie komentarze, wcięcia, białe znaki
oraz kolejność elementów wewnętrznych i pozwalający na dostęp oraz
edycję poprzez intuicyjne API.

%prep
%setup -q -n tomlkit-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/tomlkit
%{py_sitescriptdir}/tomlkit-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-tomlkit
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/tomlkit
%{py3_sitescriptdir}/tomlkit-%{version}-py*.egg-info
%endif
