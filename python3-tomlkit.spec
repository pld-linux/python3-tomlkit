#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Style preserving TOML library
Summary(pl.UTF-8):	Biblioteka TOML zachowująca styl
Name:		python3-tomlkit
Version:	0.13.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tomlkit/
Source0:	https://files.pythonhosted.org/packages/source/t/tomlkit/tomlkit-%{version}.tar.gz
# Source0-md5:	0db1a3750c64b141720f05430df9b433
URL:		https://pypi.org/project/tomlkit/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-build
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-furo >= 2021.9
# >= 2021.11.23 when available
BuildRequires:	sphinx-pdg >= 4.3.2
%endif
Requires:	python3-modules >= 1:3.6
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

%package apidocs
Summary:	API documentation for Python tomlkit module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona tomlkit
Group:		Documentation

%description apidocs
API documentation for Python tomlkit module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona tomlkit.

%prep
%setup -q -n tomlkit-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/tomlkit
%{py3_sitescriptdir}/tomlkit-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
