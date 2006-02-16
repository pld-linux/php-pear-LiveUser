%include	/usr/lib/rpm/macros.php
%define		_class		LiveUser
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - user authentication and permission management framework
Summary(pl):	%{_pearname} - uwierzytelnianie u�ytkownik�w i zarz�dzanie uprawnieniami
Name:		php-pear-%{_pearname}
Version:	0.16.6
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2bfdae81ed8be7f4d79238caadc88473
URL:		http://pear.php.net/package/LiveUser/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Perm_LiveUser to zestaw klas do uwierzytelniania u�ytkownik�w i
zarz�dzania uprawnieniami. Zasadniczo na ten pakiet sk�adaj� si� trzy
g��wne elementy:
- LoginManager (zarz�dca logowania),
- kontenery Auth (uwierzytelniania),
- kontenery Perm (uprawnie�.

Klasa LoginManager obs�uguje proces logowania i mo�e by�
skonfigurowana do u�ywania r�nych kontener�w uprawnie� oraz jednego
lub wi�kszej liczby kontener�w uwierzytelniania. Oznacza to, �e mo�na
mie� dane u�ytkownik�w rozproszone po r�nych kontenerach danych, a
LoginManager b�dzie pr�bowa� u�y� ka�dego zdefiniowanego kontenera a�
do znalezienia u�ytkownika. Na przyk�ad mo�na mie� wszystkich
u�ytkownik�w strony WWW, kt�rzy mog� zg�osi� si� po nowe konto ze
strony do lokalnej bazy danych serwera WWW. Mo�na te� chcie� umo�liwi�
wszystkim pracownikom firmy na logowanie do strony bez potrzeby
tworzenia im nowych kont. Aby to osi�gn��, mo�na zdefiniowa� drugi
kontener dla LoginManagera. Mo�na tak�e zdefiniowa� kontener
uprawnie�, kt�ry b�dzie zarz�dza� prawami dla ka�dego u�ytkownika.
Zale�nie od kontenera mo�na zaimplementowa� dowolne rodzaje schemat�w
uprawnie� dla aplikacji ca�y czas maj�c jedno sp�jne API. Przy u�yciu
r�nych kontener�w uprawnie� i uwierzytelniania mo�na �atwo
zintegrowa� nowo pisane aplikacje ze starszymi, kt�re mia�y w�asne
sposoby zapisywania uprawnie� i danych u�ytkownik�w - wystarczy
stworzy� nowy typ kontenera. Aktualnie dost�pne s� kontenery RDBMS
u�ywaj�ce PEAR::DB, wkr�tce b�dzie wi�cej.

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
