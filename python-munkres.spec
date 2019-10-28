#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Munkres algorithm for the Assignment Problem
Summary(pl.UTF-8):	Algorytm Munkresa rozwiązywania problemu przypisania
Name:		python-munkres
Version:	1.0.12
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0:	https://files.pythonhosted.org/packages/source/m/munkres/munkres-%{version}.tar.gz
#Source0Download: https://github.com/bmc/munkres/releases/
Source0:	https://github.com/bmc/munkres/archive/release-%{version}/munkres-%{version}.tar.gz
# Source0-md5:	81314d256b5e3de565b5143be333cdf2
URL:		https://pypi.python.org/pypi/munkres
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 2.0
%{?with_tests:BuildRequires:	python-nose >= 1.3.7}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%{?with_tests:BuildRequires:	python3-nose >= 1.3.7}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Munkres module provides an O(n^3) implementation of the Munkres
algorithm (also called the Hungarian algorithm or the Kuhn-Munkres
algorithm). The algorithm models an assignment problem as an NxM cost
matrix, where each element represents the cost of assigning the ith
worker to the jth job, and it figures out the least-cost solution,
choosing a single item from each row and column in the matrix, such
that no row and no column are used more than once.

%description -l pl.UTF-8
Moduł Munkres zawiera implementację O(n^3) algorytmu Munkresa (zwanego
także algorytmem węgierskim lub algorytmem Kuhna-Munkresa). Algorytm
modeluje problem przypisania jako macierz kosztu NxM, gdzie każdy
element reprezentuje koszt przypisania i-tego pracownika do j-tego
zadania i wyznacza rozwiązanie o najmniejszym koszcie, wybierając
pojedynczy element z każdego wiersza i kolumny macierzy tak, żeby
żaden wiersz ani kolumna nie były użyte więcej niż raz.

%package -n python3-munkres
Summary:	Munkres algorithm for the Assignment Problem
Summary(pl.UTF-8):	Algorytm Munkresa rozwiązywania problemu przypisania
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-munkres
The Munkres module provides an O(n^3) implementation of the Munkres
algorithm (also called the Hungarian algorithm or the Kuhn-Munkres
algorithm). The algorithm models an assignment problem as an NxM cost
matrix, where each element represents the cost of assigning the ith
worker to the jth job, and it figures out the least-cost solution,
choosing a single item from each row and column in the matrix, such
that no row and no column are used more than once.

%description -n python3-munkres -l pl.UTF-8
Moduł Munkres zawiera implementację O(n^3) algorytmu Munkresa (zwanego
także algorytmem węgierskim lub algorytmem Kuhna-Munkresa). Algorytm
modeluje problem przypisania jako macierz kosztu NxM, gdzie każdy
element reprezentuje koszt przypisania i-tego pracownika do j-tego
zadania i wyznacza rozwiązanie o najmniejszym koszcie, wybierając
pojedynczy element z każdego wiersza i kolumny macierzy tak, żeby
żaden wiersz ani kolumna nie były użyte więcej niż raz.

%prep
%setup -q -n munkres-release-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:nosetests-%{py_ver} test}
%endif

%if %{with python3}
%py3_build

%{?with_tests:nosetests-%{py3_ver} test}
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
%doc CHANGELOG.md LICENSE.md README.md
%{py_sitescriptdir}/munkres.py[co]
%{py_sitescriptdir}/munkres-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-munkres
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.md README.md
%{py3_sitescriptdir}/munkres.py
%{py3_sitescriptdir}/__pycache__/munkres.cpython-*.py[co]
%{py3_sitescriptdir}/munkres-%{version}-py*.egg-info
%endif
