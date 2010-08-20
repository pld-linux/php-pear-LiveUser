%include	/usr/lib/rpm/macros.php
%define		_class		LiveUser
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - user authentication and permission management framework
Summary(pl.UTF-8):	%{_pearname} - uwierzytelnianie użytkowników i zarządzanie uprawnieniami
Name:		php-pear-%{_pearname}
Version:	0.16.13
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7a2bb3f2f4b0d3e4978dd00020690c74
URL:		http://pear.php.net/package/LiveUser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Event_Dispatcher
Requires:	php-pear-PEAR-core >= 1:1.3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Log.php)' 'pear(DB.*)' 'pear(MDB.*)' 'pear(MDB2.*)' 'pear(MDB2/Schema.*)' 'pear(XML/Tree.php)' 'pear(Crypt/RC4.*)'

%description
Perm_LiveUser is a set of classes for dealing with user authentication
and permission management. Basically, there are three main elements
that make up this package:
- The LoginManager,
- The Auth containers,
- The Perm containers.

The LoginManager class takes care of the login process and can be
configured to use a certain permission container and one or more
different auth containers. That means, you can have your users' data
scattered amongst many data containers and have the LoginManager try
each defined container until the user is found. For example, you can
have all website users who can apply for a new account online on the
webserver's local database. Also, you want to enable all your
company's employees to login to the site without the need to create
new accounts for all of them. To achieve that, a second container can
be defined to be used by the LoginManager. You can also define a
permission container of your choice that will manage the rights for
each user. Depending on the container, you can implement any kind of
permission schemes for your application while having one consistent
API. Using different permission and auth containers, it's easily
possible to integrate newly written applications with older ones that
have their own ways of storing permissions and user data. Just make a
new container type and you're ready to go! Currently available are
RDBMS containers using PEAR::DB. More are soon to follow.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Perm_LiveUser to zestaw klas do uwierzytelniania użytkowników i
zarządzania uprawnieniami. Zasadniczo na ten pakiet składają się trzy
główne elementy:
- LoginManager (zarządca logowania),
- kontenery Auth (uwierzytelniania),
- kontenery Perm (uprawnień.

Klasa LoginManager obsługuje proces logowania i może być
skonfigurowana do używania różnych kontenerów uprawnień oraz jednego
lub większej liczby kontenerów uwierzytelniania. Oznacza to, że można
mieć dane użytkowników rozproszone po różnych kontenerach danych, a
LoginManager będzie próbował użyć każdego zdefiniowanego kontenera aż
do znalezienia użytkownika. Na przykład można mieć wszystkich
użytkowników strony WWW, którzy mogą zgłosić się po nowe konto ze
strony do lokalnej bazy danych serwera WWW. Można też chcieć umożliwić
wszystkim pracownikom firmy na logowanie do strony bez potrzeby
tworzenia im nowych kont. Aby to osiągnąć, można zdefiniować drugi
kontener dla LoginManagera. Można także zdefiniować kontener
uprawnień, który będzie zarządzał prawami dla każdego użytkownika.
Zależnie od kontenera można zaimplementować dowolne rodzaje schematów
uprawnień dla aplikacji cały czas mając jedno spójne API. Przy użyciu
różnych kontenerów uprawnień i uwierzytelniania można łatwo
zintegrować nowo pisane aplikacje ze starszymi, które miały własne
sposoby zapisywania uprawnień i danych użytkowników - wystarczy
stworzyć nowy typ kontenera. Aktualnie dostępne są kontenery RDBMS
używające PEAR::DB, wkrótce będzie więcej.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}

%{php_pear_dir}/data/%{_pearname}
